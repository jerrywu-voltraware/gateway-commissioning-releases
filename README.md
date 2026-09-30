# Gateway Commissioning Android Releases

This repository stores release metadata and signed Android APK release assets.
Application source remains in `jerrywu-voltraware/gateway-commissioning-app`.

## Current status

This repository is private. The initial Android `1.0.0+22` release is a draft
baseline corresponding to the existing installed production APK, not a new build.
It does not include an in-app updater. No stable latest release is available until
an operator explicitly publishes a reviewed draft.

The production APK includes a backend credential. Keep release access restricted
until the distribution policy is approved. Never commit signing keys, credential
files, build defines, or application source into this repository.

## Release contract

- Repository: `jerrywu-voltraware/gateway-commissioning-releases`
- Tag: `android-v<versionName>-b<versionCode>`
- Assets: `app_<sourceCommit7>_prod.apk`, `android-update.json`, `SHA256SUMS`
- Latest manifest: `https://github.com/jerrywu-voltraware/gateway-commissioning-releases/releases/latest/download/android-update.json`
- Manifest APK URLs point to a specific tag, never to `latest`.
- Publish only production APKs with the existing package and signing certificate.
- A new app release must increase Android `versionCode`; never replace assets
  under an already published release. The initial b22 is the known baseline.
- A draft is not an update and is not returned by the stable latest endpoint.

The manifest uses `schema_version: 1`, `platform: android`, `package_name`,
`version_name`, `version_code`, `release_tag`, `source_commit`, `release_notes`,
and an `apk` object containing `name`, `url`, `sha256`, `size_bytes`, and
`signing_certificate_sha256`. The consumer compares the installed Android
versionCode with the manifest version_code, then verifies the downloaded APK.

Private assets require authorized GitHub access. Never embed a GitHub token in
the mobile app. A private mobile distribution needs a controlled backend download
service or user authentication; anonymous direct download requires a public repo.

## Prepare a release on Windows

Build with the application repository's `tools/build_apk.ps1 -Env prod` first.
The preparation helper verifies the APK hash, metadata, and pinned production
signer, then writes assets into ignored `dist/<tag>/`. It does not build, install,
publish, or modify the application. Use an independently verified APK SHA-256.

```powershell
$env:JAVA_HOME = 'C:\Program Files\Android\Android Studio\jbr'
py -3 -X utf8 tools/prepare_release.py --apk <signed-prod-apk> --source-commit <full-commit> --expected-apk-sha256 <verified-sha256> --notes-file release-notes/android-v1.0.0-b22.md --android-build-tools <Android-Sdk-build-tools-directory>
```

Use the appropriate release notes file for each new release. Review the generated
manifest and verify the originating source and device acceptance evidence.

## Upload a draft

Run with the repository owner's GitHub CLI account. Explicitly list the three
assets; do not upload a whole build directory. Example for the initial baseline:

```powershell
gh release create android-v1.0.0-b22 --repo jerrywu-voltraware/gateway-commissioning-releases --draft --title 'Android 1.0.0 (22)' --notes-file release-notes/android-v1.0.0-b22.md dist/android-v1.0.0-b22/app_a68cc3f_prod.apk dist/android-v1.0.0-b22/android-update.json dist/android-v1.0.0-b22/SHA256SUMS
```

Download the draft assets into a separate directory and verify SHA256SUMS before
publishing. Confirm the intended audience before changing visibility or publishing.
Publishing a new release does not add update support to an existing installed app.

## Client integration acceptance

The Android updater must show only newer version codes; tolerate offline service,
missing releases, and malformed metadata; verify package/signature/hash; and defer
installation during commissioning. Initial installation of an updater-enabled
build remains necessary. Test upgrade in place and retained data on a real phone.
