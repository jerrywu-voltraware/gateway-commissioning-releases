"""Download a GitHub release and verify a backend delivery directory."""

import argparse
import json
import os
from pathlib import Path
import re
import shutil
import tempfile
from contextlib import contextmanager

from prepare_release import PACKAGE, REPOSITORY, SIGNER, MAX_APK_BYTES, MAX_NOTES_UNITS, run_verified, sha256


@contextmanager
def destination_lock(destination):
    """Serialize staging and activation; a stale lock requires operator review."""
    path = destination / ".release-stage.lock"
    try:
        fd = os.open(path, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    except FileExistsError:
        raise ValueError("Another release stage holds this directory; inspect its lock before retrying")
    try:
        with os.fdopen(fd, "w", encoding="ascii") as stream:
            stream.write(str(os.getpid()) + "\n")
        yield
    finally:
        path.unlink()


def stage(args):
    if not re.fullmatch(r"android-v\d+\.\d+\.\d+-b[1-9][0-9]*", args.tag):
        raise ValueError("Invalid Android release tag")
    if args.allow_draft and args.activate:
        raise ValueError("Draft staging cannot activate a backend update")
    release = json.loads(run_verified([
        "gh", "release", "view", args.tag, "--repo", REPOSITORY,
        "--json", "tagName,isDraft,isPrerelease,assets",
    ]))
    if release["tagName"] != args.tag or release["isPrerelease"]:
        raise ValueError("Only the requested stable release is accepted")
    if release["isDraft"] and not args.allow_draft:
        raise ValueError("Release is a draft; use staging-only review or publish it first")
    assets = {item["name"]: item for item in release["assets"]}
    apk_names = [name for name in assets if name.endswith(".apk")]
    if len(apk_names) != 1 or set(assets) != {apk_names[0], "android-update.json", "SHA256SUMS"}:
        raise ValueError("Release must contain exactly the approved three assets")
    if not re.fullmatch(r"app_[0-9a-f]{7}(?:_b[1-9][0-9]*)?_prod\.apk", apk_names[0]):
        raise ValueError("Unexpected APK asset filename")
    destination = Path(args.destination).resolve()
    destination.mkdir(parents=True, exist_ok=True)
    with destination_lock(destination), tempfile.TemporaryDirectory(prefix=".download-", dir=destination) as scratch:
        scratch = Path(scratch)
        run_verified(["gh", "release", "download", args.tag, "--repo", REPOSITORY,
                      "--dir", str(scratch)])
        downloaded = list(scratch.iterdir())
        if ({path.name for path in downloaded} != set(assets)
                or any(not path.is_file() or path.is_symlink() for path in downloaded)):
            raise ValueError("Downloaded asset set changed or contains non-regular files")
        manifest = json.loads((scratch / "android-update.json").read_text(encoding="utf-8"))
        apk_data = manifest.get("apk", {})
        name = apk_data.get("name", "")
        if name != apk_names[0] or not re.fullmatch(r"app_[0-9a-f]{7}(?:_b[1-9][0-9]*)?_prod\.apk", name):
            raise ValueError("Unexpected APK filename")
        apk = scratch / name
        code, version = manifest.get("version_code"), manifest.get("version_name")
        commit = manifest.get("source_commit", "")
        if (manifest.get("schema_version") != 1 or manifest.get("platform") != "android"
                or manifest.get("package_name") != PACKAGE
                or type(code) is not int or not 1 <= code <= 2100000000
                or not isinstance(version, str) or not re.fullmatch(r"\d+\.\d+\.\d+", version)
                or manifest.get("release_tag") != args.tag
                or args.tag != f"android-v{version}-b{code}"
                or not re.fullmatch(r"[0-9a-f]{40}", commit)
                or not name.startswith(f"app_{commit[:7]}")
                or apk_data.get("signing_certificate_sha256") != SIGNER
                or apk_data.get("url") != f"https://github.com/{REPOSITORY}/releases/download/{args.tag}/{name}"
                or not isinstance(manifest.get("release_notes"), str)):
            raise ValueError("Invalid release manifest")
        if (len(manifest["release_notes"].encode("utf-16-le")) // 2 > MAX_NOTES_UNITS
                or type(apk_data.get("size_bytes")) is not int
                or not 0 < apk_data["size_bytes"] <= MAX_APK_BYTES):
            raise ValueError("Release exceeds mobile update limits")
        build_suffix = re.fullmatch(r"app_[0-9a-f]{7}_b([1-9][0-9]*)_prod\.apk", name)
        if build_suffix and int(build_suffix[1]) != code:
            raise ValueError("APK filename build number differs from the manifest")
        digest = sha256(apk)
        if digest != apk_data.get("sha256") or apk.stat().st_size != apk_data.get("size_bytes"):
            raise ValueError("Downloaded APK integrity mismatch")
        expected_sums = {name: digest, "android-update.json": sha256(scratch / "android-update.json")}
        checksum_lines = (scratch / "SHA256SUMS").read_text(encoding="utf-8").splitlines()
        if len(checksum_lines) != 2:
            raise ValueError("Invalid checksum list")
        sums = {}
        for line in checksum_lines:
            checksum, filename = line.split("  ", 1)
            if filename in sums:
                raise ValueError("Duplicate checksum entry")
            sums[filename] = checksum
        if sums != expected_sums:
            raise ValueError("Release checksums do not match downloaded files")
        build_tools = Path(args.android_build_tools).resolve(strict=True)
        text = run_verified([str(build_tools / "apksigner.bat"), "verify", "--print-certs", str(apk)])
        pins = re.findall(r"Signer #\d+ certificate SHA-256 digest: ([0-9a-fA-F]+)", text)
        if [pin.lower() for pin in pins] != [SIGNER]:
            raise ValueError("Downloaded APK signer mismatch")
        text = run_verified([str(build_tools / "aapt2.exe"), "dump", "badging", str(apk)])
        found = re.search(r"^package: name='([^']+)' versionCode='(\d+)' versionName='([^']+)'", text, re.MULTILINE)
        if not found or (found[1], int(found[2]), found[3]) != (PACKAGE, code, version):
            raise ValueError("Downloaded APK metadata mismatch")
        output = destination / "releases" / args.tag
        output.parent.mkdir(exist_ok=True)
        if output.exists():
            if set(p.name for p in output.iterdir()) != set(assets):
                raise ValueError("Existing release directory differs; refusing overwrite")
            if any(sha256(output / name) != sha256(scratch / name) for name in assets):
                raise ValueError("Existing release assets differ; refusing overwrite")
        else:
            # Directory rename publishes the immutable asset set as one operation.
            shutil.move(str(scratch), str(output))
        if args.activate:
            pointer = destination / "latest.json"
            if pointer.exists():
                old_tag = json.loads(pointer.read_text(encoding="utf-8")).get("release_tag", "")
                old_match = re.fullmatch(r"android-v\d+\.\d+\.\d+-b([1-9][0-9]*)", old_tag)
                if not old_match or int(old_match[1]) > code:
                    raise ValueError("Refusing to reduce the active Android version code")
                if int(old_match[1]) == code and old_tag != args.tag:
                    raise ValueError("A different release must use a higher Android version code")
            fd, temporary = tempfile.mkstemp(prefix=".latest-", dir=destination)
            with os.fdopen(fd, "w", encoding="utf-8") as stream:
                json.dump({"release_tag": args.tag}, stream)
                stream.write("\n")
            os.replace(temporary, pointer)
        print(json.dumps({"status": "activated" if args.activate else "staged",
                          "tag": args.tag, "draft": release["isDraft"], "apk_sha256": digest,
                          "directory": str(output)}, ensure_ascii=True))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tag", required=True)
    parser.add_argument("--destination", required=True)
    parser.add_argument("--android-build-tools", required=True)
    parser.add_argument("--allow-draft", action="store_true")
    parser.add_argument("--activate", action="store_true")
    try:
        stage(parser.parse_args())
    except (ValueError, OSError, KeyError, TypeError) as error:
        parser.exit(1, f"Staging refused: {error}\n")


if __name__ == "__main__":
    main()
