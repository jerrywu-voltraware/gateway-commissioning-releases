# GIOS Device Assistant Android Releases

This repository stores release metadata and signed Android APK release assets.
Application source remains in `jerrywu-voltraware/gateway-commissioning-app`.

See [APP submission, release and update manual](docs/APP_RELEASE_MANUAL.md) for
the fixed-version policy: keep **1.0.11** and increase **Build** for each update.

## Current status

This repository is public following the owner's decision on 2026-09-30. Field
staff can download published releases without a GitHub account.
The current release is **GIOS 設備助手 — Android 1.0.11 (Build 54)**, published on 2026-10-06 (2026-10-06T07:22:16Z).
The production in-app update channel is enabled for Build 54 (since about 2026-10-06 07:24 UTC).

- [Release details](https://github.com/jerrywu-voltraware/gateway-commissioning-releases/releases/tag/android-v1.0.11-b54)
- [Download the signed APK](https://github.com/jerrywu-voltraware/gateway-commissioning-releases/releases/download/android-v1.0.11-b54/app_549a3ff_b54_prod.apk)
- Application source: `549a3ff0bf0fb5314c2b6583086ddd593fedd239`, fixed by the source repository's `android-v1.0.11-b54` tag.
- APK `app_549a3ff_b54_prod.apk` (61,243,812 bytes) SHA-256: `56201d180ca8dec6bc0c31787d67dc4b066c77ff422d842e1ac0b0aa2bab585c`.
- `android-update.json` SHA-256: `87bf4651b3b483e43138dcd4d1a082c6189ae1f75cc0322ce0c47fa389d4d404`.
- `SHA256SUMS` SHA-256: `565c59fc4166b393b480f18e76123e563206cfb04c1e74141ddec47708421c8f`.
- Signer certificate SHA-256: `2ae194573a906afd0a4e3ce347a275551e3e5b27a6d4a2644d36d07d102f4b64`.

Build 54 changes the launcher icon to the Voltraware logo (Android adaptive
icon). There are no other application changes: the Build 53 recent uploaded
data page (receiver output current, separate transmitter/receiver temperatures,
efficiency, device error descriptions, receiver MAC; requires backend v1.37.0)
and the Build 52 Traditional Chinese / English language switch are unchanged.
Known issue (same as Build 53): on small screens with large text some pages need
scrolling, and English recent-data column headers may be truncated.

This production-signed APK was built from the tagged shared main source, whose
pubspec is `1.0.11+54`. Version, package, signer and all three asset hashes passed
independent review. Full draft and anonymous public GitHub downloads matched the
approved files. Authenticated production HTTPS downloads from the VPS matched both
new Build 54 and old Build 53 hashes, using the public address, trusted CA and
hostname checks. The old assets and running services remained unchanged by this
publication.

The user will install using the app's Check for updates menu. No ADB installation,
phone-driven upgrade or real BLE/PTU workflow was performed during publication.
No iOS archive/upload was made, and this publication did not deploy the backend.
Complete or cancel an active commissioning or temporary PTU replacement before
installing an update.

The previous release, [GIOS 設備助手 1.0.11 (Build 53)](https://github.com/jerrywu-voltraware/gateway-commissioning-releases/releases/tag/android-v1.0.11-b53)
(source `4de830202ad13414ca8cb380050a2e463a6ee87a`, APK SHA-256
`6517087ad1d2625480badd5cfef7a82c978204955cf8edfb96b3d574a8cc4a15`),
[GIOS 設備助手 1.0.11 (Build 52)](https://github.com/jerrywu-voltraware/gateway-commissioning-releases/releases/tag/android-v1.0.11-b52)
(source `0a94090d722d6dfe328706579fea0abf7b442ce0`, APK SHA-256
`c723b8cdec3691742372b32500cc2500bcc1e536de8962fd0f4fb70256a751ac`), and
[Android 1.0.11 (Build 51)](https://github.com/jerrywu-voltraware/gateway-commissioning-releases/releases/tag/android-v1.0.11-b51)
(source `3b320c7c60c1f772a709bd7c19cd7fe7eb719832`, APK SHA-256
`b77f129ce6b2207037998ba85bbccf6fc1b5ed36adcd980a8b1abd59491c6136`) retain their
original assets and fixed URLs.

The historical [Android 1.0.0 (Build 21) release](https://github.com/jerrywu-voltraware/gateway-commissioning-releases/releases/tag/android-v1.0.0-b21)
and [corrected Android 1.0.1 (Build 21) release](https://github.com/jerrywu-voltraware/gateway-commissioning-releases/releases/tag/android-v1.0.1-b21)
and [Android 1.0.2 (Build 22)](https://github.com/jerrywu-voltraware/gateway-commissioning-releases/releases/tag/android-v1.0.2-b22)
retain their original assets and fixed URLs. New installations should use Build 54.
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
Do not rebuild or replace the published Build 54 or earlier assets:

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
