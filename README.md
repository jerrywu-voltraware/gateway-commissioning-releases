# Gateway Commissioning Android Releases

This repository stores release metadata and signed Android APK release assets.
Application source remains in `jerrywu-voltraware/gateway-commissioning-app`.

See [APP submission, release and update manual](docs/APP_RELEASE_MANUAL.md) for
the fixed-version policy: keep **1.0.11** and increase **Build** for each update.

## Current status

This repository is public following the owner's decision on 2026-09-30. Field
staff can download published releases without a GitHub account.
The current release is **Android 1.0.11 (Build 40)**, published on 2026-10-03.
The production in-app update channel is enabled for Build 40.

Android **1.0.11 (Build 41)** is approved and being prepared for publication
from source `63688a7c29bf59e4176b57982f026691b055dd20`. It restores the latest
shared iOS/Android changes, uses the phone's connected Wi-Fi name with manual
entry as a fallback, and removes the Wi-Fi scan entry. Build 40 remains the
active channel until the Build 41 public assets and delivery checks complete.

- [Release details](https://github.com/jerrywu-voltraware/gateway-commissioning-releases/releases/tag/android-v1.0.11-b40)
- [Download the signed APK](https://github.com/jerrywu-voltraware/gateway-commissioning-releases/releases/download/android-v1.0.11-b40/app_167dfc7_b40_prod.apk)
- Application source: `167dfc7acaca18ca23781e2c47abf5ea9a67f968`.

The project version remains **1.0.11**; the approved source uses `1.0.11+40`.
Build 40 aligns the gateway connection badge with the configuration and backend
status chips, retaining a separate MAC row and wrapping on narrow screens or
larger text sizes. BLE behavior is unchanged from Build 39.

Known scope gap reported on 2026-10-03: Build 40 was prepared from the Build 39
source and does not include the later shared iOS/Android changes in `f2f4ea0`,
including the phone's current Wi-Fi form and compact commissioning/data pages.
A corrected Android candidate is being prepared from that newer source. It is
not yet published; the immutable Build 40 assets will not be replaced.

All 1,473 Flutter tests passed and analysis found no issues. The production
signer, Android 9 compatibility, 16K alignment and complete APK hash were
independently verified. The same APK was installed over Build 39 on the test
phone and launched successfully. This release does not claim a new physical
BLE/PTU commissioning acceptance test or an Android 133 fix.

Three release assets were downloaded and verified before publication. Anonymous
GitHub downloads and authenticated production HTTPS downloads from the VPS
matched the approved hashes. A Windows production full-download probe exceeded
its deadline and is not counted as passed; production health, metadata and small
reads worked. Build 39 assets remain unchanged. No iOS archive or upload was performed.
Complete or cancel an active commissioning or temporary PTU replacement before
installing an update.

The historical [Android 1.0.0 (Build 21) release](https://github.com/jerrywu-voltraware/gateway-commissioning-releases/releases/tag/android-v1.0.0-b21)
and [corrected Android 1.0.1 (Build 21) release](https://github.com/jerrywu-voltraware/gateway-commissioning-releases/releases/tag/android-v1.0.1-b21)
and [Android 1.0.2 (Build 22)](https://github.com/jerrywu-voltraware/gateway-commissioning-releases/releases/tag/android-v1.0.2-b22)
retain their original assets and fixed URLs. New installations should use Build 40.
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
py -3 -X utf8 tools/prepare_release.py --apk <signed-prod-apk> --source-commit <full-commit> --expected-apk-sha256 <verified-sha256> --notes-file release-notes/android-v1.0.11-b40.md --android-build-tools <Android-Sdk-build-tools-directory>
```

Use the appropriate release notes file for each new release. Review the generated
manifest and verify the originating source and device acceptance evidence.

Build the current release from the clean application checkout with:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File tools/build_apk.ps1 -Env prod -BuildNumber 40 -BuildName 1.0.11
```

## Upload a draft

Run with the repository owner's GitHub CLI account. Explicitly list the three
assets; do not upload a whole build directory. Verify the
prepared manifest first and use its exact APK filename:

```powershell
$releaseDir = 'dist/android-v1.0.11-b40'
$manifest = Get-Content -LiteralPath "$releaseDir/android-update.json" -Encoding utf8 | ConvertFrom-Json
$apkPath = Join-Path $releaseDir $manifest.apk.name
gh release create android-v1.0.11-b40 --repo jerrywu-voltraware/gateway-commissioning-releases --draft --title 'Android 1.0.11 (Build 40)' --notes-file release-notes/android-v1.0.11-b40.md $apkPath "$releaseDir/android-update.json" "$releaseDir/SHA256SUMS"
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
py -3 -X utf8 tools/stage_release.py --tag android-v1.0.11-b40 --destination dist/backend-delivery --android-build-tools <Android-Sdk-build-tools-directory> --activate
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
