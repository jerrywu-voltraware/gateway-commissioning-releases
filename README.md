# GIOS Device Assistant Android Releases

This repository stores release metadata and signed Android APK release assets.
Application source remains in `jerrywu-voltraware/gateway-commissioning-app`.

See [APP submission, release and update manual](docs/APP_RELEASE_MANUAL.md) for
the fixed-version policy: keep **1.0.11** and increase **Build** for each update.

## Current status

This repository is public following the owner's decision on 2026-09-30. Field
staff can download published releases without a GitHub account.
The current release is **GIOS 設備助手 — Android 1.0.11 (Build 51)**, published on 2026-10-03.
The production in-app update channel is enabled for Build 51.

- [Release details](https://github.com/jerrywu-voltraware/gateway-commissioning-releases/releases/tag/android-v1.0.11-b51)
- [Download the signed APK](https://github.com/jerrywu-voltraware/gateway-commissioning-releases/releases/download/android-v1.0.11-b51/app_3b320c7_b51_prod.apk)
- Application source: `3b320c7c60c1f772a709bd7c19cd7fe7eb719832`, fixed by the source repository's `android-v1.0.11-b51` tag.
- APK SHA-256: `b77f129ce6b2207037998ba85bbccf6fc1b5ed36adcd980a8b1abd59491c6136`.

Build 51 keeps rejected verification samples collapsed by default and labels the
remaining countdown clearly, without changing acceptance criteria. The help sheet
can show backend guidance and accept an explicit field response. Reports identify
the installed app version and distinguish idle waiting from an operation in progress.
An older backend falls back to telephone guidance without repeatedly polling an
unsupported reply endpoint. Existing Wi-Fi setup, remembered passwords, gold
next-action hints and the GIOS 設備助手 display name are retained.

This production-signed APK was built from the tagged shared main source, whose
pubspec is `1.0.11+51`. Version, package, signer and all three asset hashes passed
independent review. Focused app checks and offline publication guard checks passed.
Full draft and anonymous public GitHub downloads matched the approved files.
Authenticated production HTTPS downloads from the VPS matched both new Build 51
and old Build 50 hashes, using the public address, trusted CA and hostname checks.
The old assets and running services remained unchanged by this publication.

The user will install using the app's Check for updates menu. No ADB installation,
phone-driven upgrade, real BLE/PTU workflow or two-way rescue conversation was
performed during publication. No iOS archive/upload or backend deployment was made.
Complete or cancel an active commissioning or temporary PTU replacement before
installing an update.

The historical [Android 1.0.0 (Build 21) release](https://github.com/jerrywu-voltraware/gateway-commissioning-releases/releases/tag/android-v1.0.0-b21)
and [corrected Android 1.0.1 (Build 21) release](https://github.com/jerrywu-voltraware/gateway-commissioning-releases/releases/tag/android-v1.0.1-b21)
and [Android 1.0.2 (Build 22)](https://github.com/jerrywu-voltraware/gateway-commissioning-releases/releases/tag/android-v1.0.2-b22)
retain their original assets and fixed URLs. New installations should use Build 51.
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
Do not rebuild or replace the published Build 51 or earlier assets:

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
