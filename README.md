# Gateway Commissioning Android Releases

This repository stores release metadata and signed Android APK release assets.
Application source remains in `jerrywu-voltraware/gateway-commissioning-app`.

## Current status

This repository is public following the owner's decision on 2026-09-30. Field
staff can open it and download published releases without a GitHub account.
The current published and backend-enabled version is **Android 1.0.1 (Build 21)**:

- [Release details](https://github.com/jerrywu-voltraware/gateway-commissioning-releases/releases/tag/android-v1.0.1-b21)
- [Download the signed APK](https://github.com/jerrywu-voltraware/gateway-commissioning-releases/releases/download/android-v1.0.1-b21/app_f431a39_b21_prod.apk)

The corrected Build 20 baseline has passed download, signature verification,
unknown-source permission handling and the Android installer prompt on Android 9.
Final installation of Build 21 remains the user's acceptance step.

The previously published [Android 1.0.0 (Build 21) release](https://github.com/jerrywu-voltraware/gateway-commissioning-releases/releases/tag/android-v1.0.0-b21)
is retained as an immutable historical record, including its original assets and
URLs. **Do not install that original Build 21 for new use:** its Android 9 updater
cannot read the downloaded APK's signing information correctly. The backend
now points to the corrected 1.0.1 release; the original download URL is unchanged.

The correction preserves the requested **Android Build 20 -> Build 21** test and
the iOS **Build 21** already in TestFlight review. The shared pubspec, iOS version,
signing and build settings are unchanged. Android 9 must begin this test from the
patched Build 20 baseline containing the archive-signature fix; the original
updater-enabled Build 20 cannot complete this update by itself. Installing the
same-package, same-signature patched Build 20 over Build 20 retains app data.
Builds 20 and 22 remain draft test/inventory artifacts.

A phone already on the original Build 21 will **not** be offered versionCode 21
again merely because versionName changes to 1.0.1. Such phones need a later
release with a higher versionCode; that rollout is outside this 20-to-21 test.

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
$env:JAVA_HOME = 'C:\Program Files\Android\Android Studio\jbr'
py -3 -X utf8 tools/prepare_release.py --apk <signed-prod-apk> --source-commit <full-commit> --expected-apk-sha256 <verified-sha256> --notes-file release-notes/android-v1.0.1-b21.md --android-build-tools <Android-Sdk-build-tools-directory>
```

Use the appropriate release notes file for each new release. Review the generated
manifest and verify the originating source and device acceptance evidence.

For the requested Android test, run these from the clean application build
checkout containing the Android 9 fix. Both use the same source and production
signing key; these command-line overrides do not modify iOS or the shared pubspec:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File tools/build_apk.ps1 -Env prod -BuildNumber 20
powershell -NoProfile -ExecutionPolicy Bypass -File tools/build_apk.ps1 -Env prod -BuildNumber 21 -BuildName 1.0.1
```

## Upload a draft

Run with the repository owner's GitHub CLI account. Explicitly list the three
assets; do not upload a whole build directory. For the correction, verify the
prepared manifest first and use its exact APK filename:

```powershell
$releaseDir = 'dist/android-v1.0.1-b21'
$manifest = Get-Content -LiteralPath "$releaseDir/android-update.json" -Encoding utf8 | ConvertFrom-Json
$apkPath = Join-Path $releaseDir $manifest.apk.name
gh release create android-v1.0.1-b21 --repo jerrywu-voltraware/gateway-commissioning-releases --draft --title 'Android 1.0.1 (Build 21)' --notes-file release-notes/android-v1.0.1-b21.md $apkPath "$releaseDir/android-update.json" "$releaseDir/SHA256SUMS"
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
py -3 -X utf8 tools/stage_release.py --tag android-v1.0.1-b21 --destination dist/backend-delivery --android-build-tools <Android-Sdk-build-tools-directory> --activate
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
