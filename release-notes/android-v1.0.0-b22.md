# Android 1.0.0 (22) — distribution baseline

This is the existing signed production APK already installed on the field-test
Android phone. It establishes the release channel baseline; it does not add an
in-app updater or include the later iOS source changes.

- Package: `com.voltraware.gateway_commissioning`
- Version: `1.0.0+22`
- Source commit: `a68cc3fdbf387f275c0921e70cc6d4e8493da62c`
- APK SHA-256: `4acbceedad33c46d379b8c0b850044fbdca00a6eb99b5327a4561f559ddcede2`
- MQTT accounts are provisioned before the app writes the new gateway identity.
- Release build tooling suppresses credential-bearing command output.

Validation: production APK signature v2/v3 verified; package/version checked;
installed Android APK hash matches this artifact. Previously recorded checks cover
production data viewing and cold start. Full commissioning interruption/resume
acceptance remains outstanding for this baseline.

Do not substitute the same-named validation-only APK; it has a different hash and
is not approved for installation. Keep this release as a private draft until the
distribution audience and publication are approved.
