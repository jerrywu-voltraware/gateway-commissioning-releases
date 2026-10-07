# GIOS Device Assistant Android Releases

## Android Build67 active - 2026-10-07 14:48 Taiwan

- Version1.0.11 Build67; source2e416406b4ef786c482f14c8ee82dc7c91607abd, source tag android-v1.0.11-b67. Public release405461646; run20261007T064620Z.
- Gateway list exit moved to fixed bottom bar under search, labeled Back to home with home icon; confirmation wording aligned. Includes Build66 explicit Wi-Fi confirmation before station selection.
- Signed APK app_2e41640_b67_prod.apk,61243812 bytes,SHA256fd119b3ce378a8714177b266647c9b6f38d94c2bd97a7563f07f1f87bc6ac665. Release build133s; static analysis, independent source/artifact/pins review, signature/zipalign/three-ABI endpoint/localization checks passed.
- Full draft/public downloads and production HTTPS readback passed. Channel65->67; old65 assets and all nine running services unchanged. No backend/firmware deployment or iOS release.
- No functional tests or ADB install this round; user accepts by in-app update. Existing field-guide changes preserved. APK retained APP_v2/build/dist; isolated APP_build67 cleaned after artifact preservation checks.
- Evidence: workspace docs/test_results/build67_artifact_review_2026-10-07.json, android_build67_rollout_pins.json, build67_draft_verification_2026-10-07.json, android_build67_public_channel_github_2026-10-07.json, android_build67_public_channel_post_2026-10-07.json.
- Authorized rollback only: py -3 -X utf8 tools/deployment/run_build67_rollout.py rollback restores channel65, preserves assets; installed phones are not downgraded.
- Next candidate Build68; Build66 remains a local-only delivery already consumed.

Older entries below are historical.

This repository stores release metadata and signed Android APK release assets.
Application source remains in `jerrywu-voltraware/gateway-commissioning-app`.

See [APP submission, release and update manual](docs/APP_RELEASE_MANUAL.md) for
the fixed-version policy: keep **1.0.11** and increase **Build** for each update.

## Current status

## Android Build65 active - 2026-10-07 10:08 Taiwan

- Version1.0.11 Build65; source006ed1d048dab637c0c1c9c76ce44ebdff05ee12; source tag android-v1.0.11-b65. Public release405302333; run20261007T020614Z.
- Fixes Change Wi-Fi silently returning when station entry is empty/invalid. Opens existing Wi-Fi-first or Wi-Fi-only form before identity selection. Existing commissioned devices retain original site/gateway fields and clear swap selection; successful Wi-Fi configuration returns to station selection through existing flow.
- Initial source3793e97 artifact superseded before publication by reviewed006ed1d; never delivered or published. Independent source review found and resolved existing-station save conflict before final build.
- Signed APK app_006ed1d_b65_prod.apk,61243812 bytes,SHA2567731dcef8db842c1539d7330f7356a76945fe795f962791cb41d4eb13c7da4c8. Formal signer v2/v3,zipalign,package/version,three-ABI production endpoint and Chinese label checks passed. Final build91.3s; scoped Dart analysis no issues.
- Draft/public complete downloads and production HTTPS readback passed. Production metadata confirms65; notes Unicode verified. Old64 assets and all nine running services unchanged. No backend/firmware deployment.
- No functional tests or physical phone acceptance per user request. User installs through APP update; verify empty-site Change Wi-Fi opens form, save returns to site selection, and existing-device identity remains unchanged.
- Existing dirty field-guide documents/assets in APP_v2 preserved. Built from clean detached APP_build65, using existing ignored build inputs. APP main/source tag pushed.
- Evidence: docs/test_results/android_build65_rollout_pins.json,build65_unicode_verification.json,build65_draft_verification_2026-10-07.json,android_build65_public_channel_github_2026-10-07.json,android_build65_public_channel_post_2026-10-07.json.
- Authorized rollback only: py -3 -X utf8 tools/deployment/run_build65_rollout.py rollback restores pointer64,preserves assets; installed phones are not downgraded.

Next candidate Build:66.

## Previous Build 55 publication (historical)

Android **1.0.11 (Build 55)** was published and enabled for in-app updates on
2026-10-06 at approximately 16:09 Taiwan time (08:09 UTC).

- [Release details](https://github.com/jerrywu-voltraware/gateway-commissioning-releases/releases/tag/android-v1.0.11-b55)
- Source: `131a1e8fca576b0d0ea55696b4c1984a1997caca`, source tag `android-v1.0.11-b55`.
- APK: `app_131a1e8_b55_prod.apk`, 61,243,812 bytes.
- APK SHA-256: `1d26ad26d80fdb8201c90b55118b51ef5f48e611bbcc3499815e2b262d3d1b00`.
- Recent data refreshes every 2 seconds while visible in the foreground; data age updates every second. Background polling stops. Gateway upload policy is unchanged.
- Formal signature, artifact metadata, full draft/public downloads, and production HTTPS update-channel read-back passed. Build 54 assets and running services were preserved.
- Functional tests were not run at the user's request. Phone installation and functional acceptance remain with the user. No ADB installation or iOS publication.
- Shared source version: `1.0.11+55`; next candidate Build: 56.

## Previous Build 54 publication (historical)


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
