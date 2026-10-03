# GIOS Device Assistant Android Releases

This repository stores release metadata and signed Android APK release assets.
Application source remains in `jerrywu-voltraware/gateway-commissioning-app`.

See [APP submission, release and update manual](docs/APP_RELEASE_MANUAL.md) for
the fixed-version policy: keep **1.0.11** and increase **Build** for each update.

## Current status

This repository is public following the owner's decision on 2026-09-30. Field
staff can download published releases without a GitHub account.
The current release is **GIOS 設備助手 — Android 1.0.11 (Build 50)**, published on 2026-10-03.
The production in-app update channel is enabled for Build 50.

- [Release details](https://github.com/jerrywu-voltraware/gateway-commissioning-releases/releases/tag/android-v1.0.11-b50)
- [Download the signed APK](https://github.com/jerrywu-voltraware/gateway-commissioning-releases/releases/download/android-v1.0.11-b50/app_c8e4ea1_b50_prod.apk)
- Application source: `c8e4ea10c54f5b3e3a1bf344d36e5900a7d2e3a9`, fixed by the source repository's `android-v1.0.11-b50` tag.
- APK SHA-256: `b700bb8b40d8f06825fb3e678b4535d3d2fd21069de5df11804c3e8d6b8f2375`.

The project version remains **1.0.11**. Build 50 unifies the launcher and app
header as **GIOS 設備助手**, adds softly pulsing gold next-action captions,
presents both station choices clearly, and shows neutral upload progress after
Wi-Fi reset. It retains the current-phone Wi-Fi flow, remembered passwords and
password visibility toggle from Build 42.

This release uses the exact production-signed APK already installed on the field
phone. It was built from the tagged source with `-BuildNumber 50`; that source's
pubspec still says `1.0.11+42`. Main's shared default was subsequently aligned to
`1.0.11+50` in `54943b3`, without rebuilding or replacing the approved APK.

Version, production signer and full asset hashes were verified. Draft and public
anonymous GitHub downloads matched the approved files. Authenticated production
HTTPS downloads from the VPS matched both new Build 50 and old Build 42 hashes,
using the public address, trusted CA and hostname validation. Old Build 42 assets
and running services remained unchanged. Per the user's request, no functional
tests were run for Builds 43–50; these release checks do not establish device
workflow acceptance or a phone-driven in-app upgrade. No iOS archive or upload
was performed; its display name was updated in source only.
Complete or cancel an active commissioning or temporary PTU replacement before
installing an update.

The historical [Android 1.0.0 (Build 21) release](https://github.com/jerrywu-voltraware/gateway-commissioning-releases/releases/tag/android-v1.0.0-b21)
and [corrected Android 1.0.1 (Build 21) release](https://github.com/jerrywu-voltraware/gateway-commissioning-releases/releases/tag/android-v1.0.1-b21)
and [Android 1.0.2 (Build 22)](https://github.com/jerrywu-voltraware/gateway-commissioning-releases/releases/tag/android-v1.0.2-b22)
retain their original assets and fixed URLs. New installations should use Build 50.
The original 1.0.0 updater on Android 9 cannot inspect the downloaded APK signing
information correctly; a manual same-package, same-signature APK installation is
needed for affected devices. Patched Build 20 and corrected 1.0.1 Build 21 can use
the authenticated update channel. Old 1.0.0 Build 20/22 inventory drafts remain
separate from published production releases.

Future updates require an operator to publish a reviewed release and activate its
verified backend delivery directory. Published release assets are immutable.

The production APK includes a backend credential. Publishing an APK here makes
its embedded contents available to anyone who downloads it. The owner has chosen
public repository visibility; release publication remains a separate step. Never
commit signing keys, credential files, build defines, or application source into
this repository.

## Release contract

- Repository: `jerrywu-voltraware/gateway-commissioning-releases`
- Tag: `android-v<versionName>-b<versionCode>`
- Assets: `app_<sourceCommit7>[_b<versionCode>]_prod.apk`, `android-update.json`, `SHA256SUMS`
- Latest manifest: `https://github.com/jerrywu-voltraware/gateway-commissioning-releases/releases/latest/download/android-update.json`
- Manifest APK URLs point to a specific tag, never to `latest`.
- Publish only production APKs with the existing package and signing certificate.
- A new app release must increase Android `versionCode`; never replace assets
  under an already published release. A phone already on b22 cannot normally be
  updated in place to b20. Use a separate test phone or an explicitly approved
  reinstall before the requested b20-to-b21 test.
- One bounded exception was made for the incomplete 20-to-21 acceptance
  test: corrected versionName `1.0.1` retains versionCode `21` under the new tag
  `android-v1.0.1-b21`. It supersedes the flawed test target for patched Build 20
  clients; it is not a same-code update for existing Build 21 clients. This does
  not establish a policy allowing future releases to reuse a versionCode.
- A draft is not an update and is not returned by the stable latest endpoint.

The manifest uses `schema_version: 1`, `platform: android`, `package_name`,
`version_name`, `version_code`, `release_tag`, `source_commit`, `release_notes`,
and an `apk` object containing `name`, `url`, `sha256`, `size_bytes`, and
`signing_certificate_sha256`. The consumer compares the installed Android
versionCode with the manifest version_code, then verifies the downloaded APK.
APK size is limited to 150 MiB and notes to 20,000 UTF-16 units, matching both
the backend and the Android client.

Draft assets require authorized GitHub access; published releases are public.
Never embed a GitHub token in the mobile app. The in-app distribution path remains
the authenticated backend: the release
operator downloads and verifies GitHub assets, synchronizes the immutable release
directory to the server, and activates its latest pointer. Mobile clients use
their existing backend session. The server does not need a GitHub credential.

## Prepare a release on Windows

Build with the application repository's `tools/build_apk.ps1 -Env prod` first.
The preparation helper verifies the APK hash, metadata, and pinned production
signer, then writes assets into ignored `dist/<tag>/`. It does not build, install,
publish, or modify the application. Use an independently verified APK SHA-256.

```powershell
$env:JAVA_HOME = 'C:\Program Files\Android\Android Studio1\jbr'
py -3 -X utf8 tools/prepare_release.py --apk <signed-prod-apk> --source-commit <full-commit> --expected-apk-sha256 <verified-sha256> --notes-file <release-notes-file> --android-build-tools <Android-Sdk-build-tools-directory>
```

Use the appropriate release notes file for each new release. Review the generated
manifest and verify the originating source and device acceptance evidence.

For a new release, use the approved, unused Build number and a clean checkout.
Do not rebuild or replace the published Build 50 assets:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File tools/build_apk.ps1 -Env prod -BuildNumber <approved-build-number> -BuildName 1.0.11
```

## Upload a draft

Run with the repository owner's GitHub CLI account. Explicitly list the three
assets; do not upload a whole build directory. Verify the
prepared manifest first and use its exact APK filename. Set `$releaseTag` to the
approved new tag, not an already published tag:

```powershell
$releaseDir = Join-Path 'dist' $releaseTag
$manifest = Get-Content -LiteralPath "$releaseDir/android-update.json" -Encoding utf8 | ConvertFrom-Json
$apkPath = Join-Path $releaseDir $manifest.apk.name
gh release create $releaseTag --repo jerrywu-voltraware/gateway-commissioning-releases --draft --title $releaseTitle --notes-file "release-notes/$releaseTag.md" $apkPath "$releaseDir/android-update.json" "$releaseDir/SHA256SUMS"
```

Download the draft assets into a separate directory and verify SHA256SUMS before
publishing. Confirm the intended audience before changing visibility or publishing.
Publishing a new release does not add update support to an existing installed app.

## Client integration acceptance

The Android updater must show only newer version codes; tolerate offline service,
missing releases, and malformed metadata; verify package/signature/hash; and defer
installation during commissioning. Initial installation of an updater-enabled
build remains necessary. Test upgrade in place and retained data on a real phone.

## Stage the release for backend delivery

The release operator uses their authenticated local GitHub CLI; field staff do
not need a GitHub account to access a published release in their browser.
This validates package, version, production signer, hash and checksums again:

```powershell
py -3 -X utf8 tools/stage_release.py --tag $releaseTag --destination dist/backend-delivery --android-build-tools <Android-Sdk-build-tools-directory> --activate
```

For draft review only, replace `--activate` with `--allow-draft`. Drafts cannot
activate updates. Re-running an identical immutable release is safe; altered
assets or a decreasing latest version code are refused. The one-time switch from
`android-v1.0.0-b21` to `android-v1.0.1-b21` must be explicitly reviewed as the
bounded exception above; do not weaken the normal version-increase rule or reuse
the old tag. Keep the old release directory and URLs intact.

Staging uses `.release-stage.lock` to serialize publishers. If a process was
interrupted, first confirm no publisher is still running and inspect the staged
files before manually removing a stale lock. Do not remove an active lock.

The resulting directory contains `releases/<tag>/` and, only after activation,
`latest.json`. Synchronize release files before atomically switching the server's
latest.json. Keep credentials and mutable metadata out of GitHub download URLs.
The authenticated API serves `/api/app/updates/android/latest` and a same-server
APK route; the mobile app never needs a GitHub account.
