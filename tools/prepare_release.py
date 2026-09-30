"""Verify an existing production APK and prepare GitHub release assets locally."""

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess


REPOSITORY = "jerrywu-voltraware/gateway-commissioning-releases"
PACKAGE = "com.voltraware.gateway_commissioning"
SIGNER = "2ae194573a906afd0a4e3ce347a275551e3e5b27a6d4a2644d36d07d102f4b64"
MAX_APK_BYTES = 150 * 1024 * 1024
MAX_NOTES_UNITS = 20000


def sha256(path):
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def run_verified(command):
    env = os.environ.copy()
    env.pop("DEBUG", None)
    env.pop("GH_DEBUG", None)
    result = subprocess.run(command, capture_output=True, text=True,
                            encoding="utf-8", errors="replace", env=env)
    if result.returncode:
        raise ValueError(f"APK verification tool failed (exit {result.returncode})")
    return result.stdout


def prepare(args):
    apk = Path(args.apk).resolve(strict=True)
    if not 0 < apk.stat().st_size <= MAX_APK_BYTES:
        raise ValueError("APK size exceeds the mobile update limit")
    if not re.fullmatch(r"[0-9a-f]{40}", args.source_commit):
        raise ValueError("Provide a full lowercase source commit")
    if not re.fullmatch(rf"app_{args.source_commit[:7]}(?:_b[1-9][0-9]*)?_prod\.apk", apk.name):
        raise ValueError("APK must have the clean production build-helper filename")
    if not re.fullmatch(r"[0-9a-fA-F]{64}", args.expected_apk_sha256):
        raise ValueError("Provide the independently verified APK SHA-256")
    digest = sha256(apk)
    if digest != args.expected_apk_sha256.lower():
        raise ValueError("APK hash differs from the approved artifact")
    build_tools = Path(args.android_build_tools).resolve(strict=True)
    signer_text = run_verified([
        str(build_tools / "apksigner.bat"), "verify", "--verbose",
        "--print-certs", str(apk),
    ])
    signers = re.findall(r"Signer #\d+ certificate SHA-256 digest: ([0-9a-fA-F]+)",
                         signer_text)
    if [value.lower() for value in signers] != [SIGNER]:
        raise ValueError("APK is not signed by the approved production certificate")
    badging = run_verified([str(build_tools / "aapt2.exe"), "dump", "badging", str(apk)])
    match = re.search(r"^package: name='([^']+)' versionCode='(\d+)' versionName='([^']+)'",
                      badging, re.MULTILINE)
    if not match or match[1] != PACKAGE:
        raise ValueError("Unexpected APK package metadata")
    version_code, version_name = int(match[2]), match[3]
    if not 1 <= version_code <= 2100000000 or not re.fullmatch(r"\d+\.\d+\.\d+", version_name):
        raise ValueError("Unsupported release version")
    override = re.fullmatch(r"app_[0-9a-f]{7}_b([0-9]+)_prod\.apk", apk.name)
    if override and int(override[1]) != version_code:
        raise ValueError("APK filename build number differs from its Android versionCode")
    notes = Path(args.notes_file).read_text(encoding="utf-8-sig").strip()
    if not notes or len(notes.encode("utf-16-le")) // 2 > MAX_NOTES_UNITS:
        raise ValueError("Release notes must contain 1 to 20000 UTF-16 units")
    tag = f"android-v{version_name}-b{version_code}"
    output = Path(__file__).resolve().parents[1] / "dist" / tag
    if output.exists():
        raise ValueError("Release staging directory already exists; inspect it before proceeding")
    manifest = {
        "schema_version": 1,
        "platform": "android",
        "package_name": PACKAGE,
        "version_name": version_name,
        "version_code": version_code,
        "release_tag": tag,
        "source_commit": args.source_commit,
        "release_notes": notes,
        "apk": {
            "name": apk.name,
            "url": f"https://github.com/{REPOSITORY}/releases/download/{tag}/{apk.name}",
            "sha256": digest,
            "size_bytes": apk.stat().st_size,
            "signing_certificate_sha256": SIGNER,
        },
    }
    output.mkdir(parents=True)
    shutil.copy2(apk, output / apk.name)
    if sha256(output / apk.name) != digest:
        raise ValueError("Staged APK hash mismatch")
    manifest_path = output / "android-update.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
                             encoding="utf-8")
    (output / "SHA256SUMS").write_text(
        f"{digest}  {apk.name}\n{sha256(manifest_path)}  android-update.json\n",
        encoding="utf-8")
    print(json.dumps({"status": "prepared", "tag": tag,
                      "version_code": version_code, "apk_sha256": digest,
                      "output": str(output)}, ensure_ascii=True))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apk", required=True)
    parser.add_argument("--source-commit", required=True)
    parser.add_argument("--expected-apk-sha256", required=True)
    parser.add_argument("--notes-file", required=True)
    parser.add_argument("--android-build-tools", required=True)
    try:
        prepare(parser.parse_args())
    except (ValueError, OSError) as error:
        parser.exit(1, f"Preparation refused: {error}\n")


if __name__ == "__main__":
    main()
