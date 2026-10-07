# APP 提交、發布與更新手冊

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

Older entries below are historical.

## Android Build64 active - 2026-10-06 21:39 Taiwan

- Version 1.0.11 Build64; source `bcd06eec4489b1af8fb05b226e5706781f0063a2`, tag `android-v1.0.11-b64`.
- Home heading now says Choose an action; duplicate subtitle removed. Includes Build63 fix: update dialog checks its own route visibility and keeps existing foreground/session/BLE guards, so it no longer disables its own update button.
- APK `app_bcd06ee_b64_prod.apk`, 61243812 bytes, SHA256 `d24cfe05a8eb253c37982347ab19af2966e3998bd2bf85e9101993204ff797a2`. Release build, official signature and version checks passed; home/update labels verified in all three APK architectures; Chinese manifest and production update notes verified.
- Draft/public complete downloads and production HTTPS readback passed. GitHub Release 404752600 stable/latest; run-id `20261006T133351Z`. Old Build62 assets preserved; all nine running containers unchanged during APP publication from the pre-publication baseline; no backend deployment/restart.
- Scoped Dart analysis checks passed. Functional tests not run per user request; physical phone update validation remains with user. No iOS publication.
- Evidence: `build64_unicode_verification.json`, `build64_draft_verification_2026-10-06.json`, `android_build64_public_channel_github_2026-10-06.json`, `android_build64_public_channel_post_2026-10-06.json`, `android_build64_rollout_pins.json`.
- Authorized APP rollback only: `py -3 -X utf8 tools/deployment/run_build64_rollout.py rollback` restores the pointer to62 and preserves assets; installed phones are not downgraded.

Next candidate Build: 65. Older entries below are historical.

## Android Build62 active - 2026-10-06 20:12 Taiwan

- Version 1.0.11 Build62; source `801a304c580537ce1b6ba346b79d7b65d5227666`, tag `android-v1.0.11-b62`.
- Recent data cards show vehicle type above power: same-sample PRU Type 1=E-Bike, 2=E-Scooter, missing/other=Unknown. Includes Build61 setup cleanup (duplicate data entry removed; environment badge in header).
- Backend d47c5e5 deployed at `/home/jerrywu/gateway-management-deployments/20261006T120623Z-pru-type`; only dashboard-api recreated with authorization. No schema/firmware change. Health/source/auth checks passed; production recent API returned pru_type=1 for 81/1 and 20/1. Other containers and gateway command counts unchanged.
- APK `app_801a304_b62_prod.apk`, 61243812 bytes, SHA256 `987bebf8833f3e3fcee2c83685bbd1931f89723add089ed45f666a93cea9e937`. Release build, official signature and version checks passed; vehicle labels verified in all three APK architectures; Chinese manifest and production update notes verified.
- Draft/public complete downloads and production HTTPS readback passed. GitHub Release 404663131 stable/latest; run-id `20261006T120116Z`. Old Build60 assets preserved; all nine running containers unchanged during APP publication after the backend deployment baseline.
- Scoped Dart analysis and backend Python syntax checks passed. Functional tests not run per user request; physical phone update validation remains with user. No iOS publication.
- Evidence: `docs/test_results/build62_backend_verification.json`, `build62_unicode_verification.json`, `build62_draft_verification_2026-10-06.json`, `android_build62_public_channel_github_2026-10-06.json`, `android_build62_public_channel_post_2026-10-06.json`, `android_build62_rollout_pins.json`.
- Authorized APP rollback only: `py -3 -X utf8 tools/deployment/run_build62_rollout.py rollback` restores the pointer to60 and preserves assets; installed phones are not downgraded. Backend rollback helper remains in the deployment stage; do not execute without authorization.

Next candidate Build: 63. Older entries below are historical.

## Android Build60 active - 2026-10-06 19:37 Taiwan

- Version1.0.11 Build60; source `54f3855ac96cbd9c6716790be22715d94ea7b3bf`, tag `android-v1.0.11-b60`.
- Added dual-entry home: Field Setup opens the existing commissioning preparation/resume flow; View Data opens the site/gateway list. Home retains environment and update/language/theme menu. Setup start back, leave-list and completion return home; configure-next stays in setup. Active setup keeps its existing end confirmation.
- APK `app_54f3855_b60_prod.apk`, 61243812 bytes, SHA256 `fb2638b9e88da429a856eec6017263d3554d7454e9e4c7f24ee8d2fe65a889f4`. Build/signature/version checks passed. Exact Unicode home/charging labels verified in all three APK architectures; manifest notes and production update API Chinese notes verified.
- Draft/public complete downloads and production HTTPS readback passed. GitHub Release 404633941 stable/latest; run-id `20261006T113203Z`. Old59 assets and all nine backend containers unchanged.
- Scoped static analysis had no errors; one braces style info was fixed. No functional tests or physical-device acceptance; user validates via phone update. No iOS publication.
- Evidence: docs/test_results/build60_unicode_verification.json, build60_draft_verification_2026-10-06.json, android_build60_public_channel_github_2026-10-06.json, android_build60_public_channel_post_2026-10-06.json, android_build60_rollout_pins.json.
- Authorized rollback only: `py -3 -X utf8 tools/deployment/run_build60_rollout.py rollback` restores the pointer to59, preserving assets; installed phones are not downgraded.

Next candidate Build: 61. Older entries below are historical.

## Android Build 59 published and active - 2026-10-06 19:02 Taiwan

- Version 1.0.11, Build 59; source `82437ddf8c238ae92ae602e9f0ea0ddac8269d64`, source tag `android-v1.0.11-b59`.
- Corrects the three Chinese charging labels and release notes that became question marks in Build58. Exact Chinese code points verified in source, generated localization, UTF8 notes, manifest and all three APK architectures. Evidence: docs/test_results/build59_unicode_verification.json.
- APK `app_82437dd_b59_prod.apk`, 61,243,812 bytes; SHA256 `0db28286ee3e7fcfd84489cf173f5e83b0f4707073b815958ca343379ba87e7b`. Production signer verified; metadata and full draft/public downloads passed.
- GitHub Release 404604347 public stable/latest; VPS run-id `20261006T105707Z`. Production HTTPS readback confirms Build59 and complete APK hash. Old58 assets and all nine services unchanged.
- No functional tests, ADB installation or iOS publication; user will validate via phone update.
- Signed build passed in70.6 seconds; no build-environment changes were needed for Build59.
- Evidence: docs/test_results/android_build59_rollout_pins.json, build59_draft_verification_2026-10-06.json, android_build59_public_channel_github_2026-10-06.json, android_build59_public_channel_post_2026-10-06.json.
- Authorized rollback only: `py -3 -X utf8 tools/deployment/run_build59_rollout.py rollback` restores pointer to58 using recorded run-id and preserves assets. It does not downgrade installed phones.

Next candidate Build: 60. Older status sections below are historical.

## Android Build 58 published and active ? 2026-10-06 18:53 Taiwan

- Version 1.0.11, Build 58; source `859fa0a232c1b0a54aeb6babbbf502e8f3bceb7e`, source tag `android-v1.0.11-b58`.
- Recent cards and history show PTU input power, PRU output power, overall efficiency, Battery Voltage, Charging Current, and System Status / Fault; abnormal samples show Fault Code. MACs, timestamps and auto-refresh preserved.
- APK `app_859fa0a_b58_prod.apk`, 61,243,812 bytes; SHA256 `3caf5239f5b73f84bf58e90b250b590c1fb4f5ef1af2654ac6bddd06640b16c3`. Production signer verified; metadata and full draft/public downloads passed.
- GitHub Release 404598541 public stable/latest; VPS run-id `20261006T104905Z`. Production HTTPS readback confirms Build58 and complete APK hash. Old57 assets and all nine services unchanged.
- No functional tests, ADB installation or iOS publication; user will validate via phone update.
- Initial build failed on stale company-machine caches; moving generated caches aside resolved it. Source/dependency versions unchanged. Cache backup remains APP_v2/.build58-cache (ignored).
- Evidence: docs/test_results/android_build58_rollout_pins.json, build58_draft_verification_2026-10-06.json, android_build58_public_channel_github_2026-10-06.json, android_build58_public_channel_post_2026-10-06.json.
- Authorized rollback only: `py -3 -X utf8 tools/deployment/run_build58_rollout.py rollback` restores pointer to57 using recorded run-id and preserves assets. It does not downgrade installed phones.

Next candidate Build: 59. Older status sections below are historical.

## Build 57 publication ? 2026-10-06 16:55 Taiwan

Android 1.0.11 Build 57 is public and active. Source `4a9fb3ce59e8e94226499881ba1f31c592b31263`, source tag `android-v1.0.11-b57`, shared version `1.0.11+57`; next candidate Build 58. Do not reuse 57.
Release ID `404499954`; run-id `20261006T084932Z`. Helpers: `tools/deployment/*build57*`, `verify_android57_public_channel.py`; pins: `docs/test_results/android_build57_rollout_pins.json`.
Backend dependency deployed at stage `20261006T085400Z-vbat-display`; raw Vbat API and display-only conversion. Evidence: workspace `docs/test_results/build57_publication_2026-10-06.md`. All previous status sections below are historical.


## 最新狀態：2026-10-06 16:20（優先於下方歷史範例）

Android **1.0.11 Build 56** 已公開並啟用更新。來源 `f2318faacc6dfc9526f5329a1e8f9e7fc0374b10`，來源 tag `android-v1.0.11-b56`，共享版號 `1.0.11+56`；下一候選 Build 57，不可重用 56。

本版將三區閘道器清單依站號分組，預設收合，顯示台數並保留原操作。依使用者要求未跑功能測試，由使用者透過更新安裝驗收。正式簽章、完整草稿／公開下載與正式 HTTPS 回讀通過，舊 Build 55 與服務保持不變。

本輪工具為工作區 `tools/deployment/*build56*`、`verify_android56_public_channel.py`；pins 為 `docs/test_results/android_build56_rollout_pins.json`，run-id `20261006T081905Z`。進度／回滾參數見 `CONTINUE_2026-10-06_BUILD56_PUBLICATION.md`。

## 最新狀態：2026-10-06 16:09（優先於下方 Build 54 歷史範例）

Android **1.0.11 Build 55** 已公開並啟用正式更新通道。來源 `131a1e8fca576b0d0ea55696b4c1984a1997caca`，來源標籤 `android-v1.0.11-b55`，共享版號 `1.0.11+55`；下一候選為 Build 56，不可重用 55。

本版最近資料前景每 2 秒自動刷新、資料年齡每秒更新，背景停止。依使用者要求未跑功能測試，手機由使用者更新後驗收。正式簽章、草稿／公開完整下載與正式 HTTPS 回讀核對通過；舊 Build 54 資產與服務保留。

本輪工具在工作區 `tools/deployment/*build55*` 與 `verify_android55_public_channel.py`；pins 為 `docs/test_results/android_build55_rollout_pins.json`，run-id `20261006T080749Z`，完整進度與回滾參數在 `CONTINUE_2026-10-06_BUILD55_PUBLICATION.md`。下方 Build 54 命令為歷史範例，後續發布須按最新來源與 Build 更新。

適用專案：GIOS 設備助手（2026-10-03 更名，原為 GIOS 現場開通）；建立日期：2026-10-01。程式碼位於 `APP_v2`，Android 發布資料位於 `android_releases`，兩者是不同的 Git repository。以下 Windows 指令以 PowerShell 5.1、工作區家裡機 `E:\iot_gateway`（公司機為 `F:\iot_gateway`，內容同步）為例。

## 1. 固定版本規則：1.0.11 不變，只增加 Build

**依使用者決定，APP 版本號固定為 `1.0.11`，後續一般修正與更新不再增加版本號，只增加 Build。** 不得自行改成 `1.0.12`、`1.1.0`，也不得讓自動發布工具按照每次修正自動增加版本號。只有使用者明確改變這項決定時，才另行規劃版本變更。

目前已發布基準是 **`1.0.11 (Build 54)`**（2026-10-06 發布，原為 Build 53），正式更新通道已啟用。Android／iOS 統一在 `APP_v2` 的 `main` 主線開發；Build 54 的 APK 來源以 **APP 來源 repo** 的 `android-v1.0.11-b54` 標籤固定於 commit `549a3ff0bf0fb5314c2b6583086ddd593fedd239`。來源標籤與本發布 repo 的同名標籤用途不同；後續提交不改變原發布來源。主線 `pubspec.yaml` 目前為：

```yaml
version: 1.0.11+54
```

Build 54 由來源 549a3ff 建置（共享 pubspec `1.0.11+54`），三資產 pins 見工作區 `docs/test_results/android_build54_rollout_pins.json`。不得因為主線後續提交而移動來源標籤或替換公開 APK。

Build 54 包含：APP 圖示改為 Voltraware 標誌（Android 自適應圖示，背景白色、前景內縮 16%）；其餘程式不變，Build 53 的「查看上傳資料」PRU 欄位（需後台 v1.37.0）與 Build 52 的中英語系切換保留。已知問題同 Build 53：小螢幕大字體時部分頁面需捲動、英文最近資料表頭可能截斷。正式通道由 53→54，舊 53 資產與服務保持不變。**Build 40 的來源遺漏已由 Build 41 修正。**

Build 54 由使用者自行從 APP 內「檢查更新」安裝；發布輪沒有 ADB 安裝或手機內升級驗收。發布時只核對建置、正式簽章、版本、三資產完整下載雜湊及正式更新通道，不代表 Wi-Fi／BLE／PTU 實機驗收。iOS 未建置／上傳。

若兩平台都沒有占用更高的 Build，下一次只改為 `1.0.11+55`，再下一次為 `1.0.11+56`。發布前必須查詢 Android 已發布／已交付安裝的 Build，以及 App Store Connect 已上傳的 Build，確認本次數字尚未使用。**不可回退、重用已交付的 Build，或覆寫已公開的 Release 資產。** 既有早期 Build 21 修正例外不得當成日後重用 Build 的依據。

**同一核定來源、同一批次的 Android 與 iOS 可以共用相同 Build。** 例如 Android Build 39 已交付，仍可依同批核定來源製作 iOS Build 39；禁止的是同一平台重用該 Build 發布不同內容，不是禁止跨平台對齊。

| 用途 | 固定版本欄位 | 每次遞增欄位 |
|---|---|---|
| Flutter `pubspec.yaml` | `+` 前的 `1.0.11` | `+` 後的整數 |
| Android | `versionName = 1.0.11` | `versionCode = N` |
| iOS | `CFBundleShortVersionString = 1.0.11`／Xcode Version | `CFBundleVersion = N`／Xcode Build |
| Android Release tag | `android-v1.0.11` | 後綴 `-bN` |

這是本專案降低 iOS 審查流程反覆變動的策略：讓後續測試留在同一個 Version 下，避免無必要地另開版本而增加審查等待。Apple 說明首次提交 TestFlight 外部測試的 Build 需要完整審查，同一 Version 的後續 Build **可能**不需完整審查；所以不能承諾「只增加 Build 一定免審」或保證審查時間。以 App Store Connect 實際狀態為準。[Apple：邀請外部測試人員](https://developer.apple.com/help/app-store-connect/test-a-beta-version/invite-external-testers/)

Apple 以 Bundle ID、Version 對應 App 與版本紀錄，以 Build 區分上傳產物；每次準備上傳新的 Archive 都應增加 Build。維持同一 Version 並增加 Build 是官方支援的流程。[Apple：上傳 Build](https://developer.apple.com/help/app-store-connect/manage-builds/upload-builds/)、[Xcode：設定 Version 與 Build](https://help.apple.com/xcode/mac/current/en.lproj/devba7f53ad4.html)

## 2. 發布前確認範圍

1. 確認這次要提交哪些功能／修正、目標 Build、發布平台及驗收方式。使用者已授權提交與發布時，沿用該次授權，不重複詢問。
2. 檢查工作樹，保留使用者原有修改；只提交本次已確認的檔案，不用 `git add .` 混入無關內容。
3. Android 提交、APK 公開發布、正式更新通道啟用，以及 iOS 上傳／外測分發是不同動作。Android 發布不代表 iOS 已建置、上傳或通過審查。
4. 查最新 `HANDBOOK_CODEX.md` 底部與發布紀錄。README 不是遠端服務狀態的替代品，必須讀取實際 GitHub latest 與正式 API。
5. APK 沿用現有 package `com.voltraware.gateway_commissioning` 與正式簽章，不能改用 debug key。密碼、token、API key、keystore 都不得放進 commit、release notes、手冊或原始 log。

Android 發布庫維持 **public**，現場人員下載已公開 APK 不需要 GitHub 帳號。維護者上傳 draft 仍需要有寫入權限的帳號。APP 內更新沿用正式後台驗證與轉送，手機不保存 GitHub token。正式 APK 已含既有後台存取憑證，公開 APK 的決定已由使用者確認；不要因此把任何額外憑證或原始碼放入發布庫。

## 3. 修改 Build、測試、提交 APP

以下指令從同一個 PowerShell 工作階段依序執行。**`55` 只是 Build 54 後的下一版範例，不是永久預設值**（2026-10-06 Build 54 發布後更新：原為 54）；先依第 1 節核定實際 Build 與來源工作樹，再設定變數。範例不會修改目前已發布的 Build 54。

```powershell
$workspace = 'E:\iot_gateway'   # company machine: F:\iot_gateway
$appRoot = Join-Path $workspace 'APP_v2'
$releaseRoot = Join-Path $workspace 'android_releases'
$releaseVersion = '1.0.11'
$releaseBuild = 55
$releaseTag = "android-v$releaseVersion-b$releaseBuild"
$releaseRepo = 'jerrywu-voltraware/gateway-commissioning-releases'
Set-Location -LiteralPath $appRoot
git status --short
git log -1 --oneline
```

將 `pubspec.yaml` 唯一的 `version:` 行改成已核定的 `1.0.11+N`，完成本次程式與回歸測試修改。Android helper 的 `-BuildName`／`-BuildNumber` 只覆寫當次 APK，不會回寫 `pubspec.yaml`，因此不能只改命令列而留下過時的共同預設值。

```powershell
flutter analyze
if ($LASTEXITCODE -ne 0) { throw 'Flutter analysis failed' }
flutter test
if ($LASTEXITCODE -ne 0) { throw 'Flutter tests failed' }
git diff --check
if ($LASTEXITCODE -ne 0) { throw 'Diff check failed' }
```

另由獨立審查者檢查實際變更、相關測試與結果。依改動驗證大字級、取消／晚到回覆、舊韌體相容性、斷線與續作等受影響行為。測試通過不等於已完成 BLE 實機架設；沒有實測的項目必須明寫。

使用明列檔名的 `git add -- ...` 暫存已核定修改，再檢查 `git diff --cached`。例如先加入版號檔，其他功能檔也必須逐一加入：

```powershell
git add -- pubspec.yaml
git diff --cached --stat
git diff --cached
```

確認暫存範圍完整後提交。Commit message 使用英文，例如 `Release Android 1.0.11 build 51`。接著確認工作樹乾淨並記錄完整 commit；不可為正式發布使用 `-AllowDirty`。

```powershell
git commit -m "Release Android $releaseVersion build $releaseBuild"
if ($LASTEXITCODE -ne 0) { throw 'Source commit failed' }
if (@(git status --porcelain).Count -ne 0) { throw 'Review uncommitted files before release' }
$sourceCommit = (git rev-parse HEAD).Trim()
$sourceShort = $sourceCommit.Substring(0, 7)
$sourceBranch = (git branch --show-current).Trim()
if (-not $sourceBranch) { throw 'A release source branch is required' }
```

## 4. 建置正式 APK，獨立核對產物

先確認 Java 路徑。Flutter 本身可能找到 Android Studio 的 Java，但獨立執行的 `apksigner` 仍需要正確 `JAVA_HOME`；缺少這一步會在簽章階段失敗。家裡機的 `C:\Program Files\Android\Android Studio\jbr` 缺 `lib\jvm.cfg`（Build 51 第一次簽章失敗原因），一定要用 `Android Studio1\jbr`；**公司機（USER01）相反**：`Android Studio\jbr` 完整、`Android Studio1\jbr` 缺 `lib\jvm.cfg`（Build 53、54 使用 `Android Studio\jbr`）。以含 `lib\jvm.cfg` 的那個為準；上面的檢查包含 `lib\jvm.cfg`。`$androidTools` 以 `$env:LOCALAPPDATA` 展開，家裡機（woo75）與公司機（USER01）都適用。

```powershell
$env:JAVA_HOME = 'C:\Program Files\Android\Android Studio1\jbr'
if (-not (Test-Path -LiteralPath (Join-Path $env:JAVA_HOME 'bin\java.exe'))) {
    throw 'Android Studio Java not found'
}
if (-not (Test-Path -LiteralPath (Join-Path $env:JAVA_HOME 'lib\jvm.cfg'))) {
    throw 'Android Studio Java is incomplete (jvm.cfg missing)'
}
$androidTools = Join-Path $env:LOCALAPPDATA 'Android\Sdk\build-tools\36.0.0'
foreach ($tool in 'aapt2.exe', 'apksigner.bat', 'zipalign.exe') {
    if (-not (Test-Path -LiteralPath (Join-Path $androidTools $tool))) {
        throw "Missing Android build tool: $tool"
    }
}
$expectedVersionLine = "version: $releaseVersion+$releaseBuild"
$versionLine = @(Get-Content -LiteralPath 'pubspec.yaml' -Encoding utf8 | Where-Object { $_ -match '^version:' })
if ($versionLine.Count -ne 1 -or $versionLine[0] -ne $expectedVersionLine) {
    throw 'pubspec version does not match the approved release'
}
powershell -NoProfile -ExecutionPolicy Bypass -File tools\build_apk.ps1 -Env prod -BuildNumber $releaseBuild -BuildName 1.0.11
if ($LASTEXITCODE -ne 0) { throw 'Signed production build failed' }
$apkName = "app_${sourceShort}_b${releaseBuild}_prod.apk"
$apkPath = Join-Path $appRoot "build\dist\$apkName"
```

使用既有 `APP_v2/.secrets/prod.env` 與 `APP_v2/android/key.properties`／既有簽章環境設定，不在命令列直接傳密碼。建置失敗時先排除原因再重新執行，不能把舊 APK 改檔名當作本次產物。

獨立核對同一個 `$apkPath`，不要只相信檔名或 build log：

```powershell
& (Join-Path $androidTools 'aapt2.exe') dump badging $apkPath
if ($LASTEXITCODE -ne 0) { throw 'APK metadata verification failed' }
& (Join-Path $androidTools 'apksigner.bat') verify --verbose --print-certs $apkPath
if ($LASTEXITCODE -ne 0) { throw 'APK signature verification failed' }
& (Join-Path $androidTools 'zipalign.exe') -c -P 16 4 $apkPath
if ($LASTEXITCODE -ne 0) { throw 'APK alignment verification failed' }
$apkSha256 = (Get-FileHash -LiteralPath $apkPath -Algorithm SHA256).Hash.ToLowerInvariant()
```

審查結果必須逐項符合：package 正確、`versionName=1.0.11`、`versionCode=N`、簽章驗證通過、正式 signer 為 `2ae194573a906afd0a4e3ce347a275551e3e5b27a6d4a2644d36d07d102f4b64`。記錄完整 source commit、APK 檔名、bytes、SHA-256、簽章與相容性檢查結果。`$apkSha256` 須經獨立審查確認後才能當作核定值。

若本次範圍含手機驗收，使用同 package／同 signer 的原位更新；不要卸載或清資料來掩蓋升級失敗。確認真實安裝版本、既有資料保留及本次功能。`adb install -r` 成功與 APP 內下載安裝成功是不同證據，不能互相代稱。

授權範圍內推送已建置的來源分支並確認遠端 commit。不要強制推送或順手更新未指定的其他分支：

```powershell
git push origin $sourceBranch
if ($LASTEXITCODE -ne 0) { throw 'Source push failed' }
git ls-remote origin "refs/heads/$sourceBranch"
```

## 5. 準備三份發布資產與發布文件

在 release repository 建立 `release-notes/android-v1.0.11-bN.md`，寫實際修改、限制與測試。README 先標示候選版／準備中，正式啟用後才改為目前公開版本。不要寫入敏感設定或未完成的實機結果。

```powershell
Set-Location -LiteralPath $releaseRoot
$notesPath = "release-notes/$releaseTag.md"
if (-not (Test-Path -LiteralPath $notesPath)) { throw 'Reviewed release notes are required' }
py -3 -X utf8 tools/prepare_release.py --apk $apkPath --source-commit $sourceCommit --expected-apk-sha256 $apkSha256 --notes-file $notesPath --android-build-tools $androidTools
if ($LASTEXITCODE -ne 0) { throw 'Release preparation failed' }
$assetsDir = Join-Path $releaseRoot "dist\$releaseTag"
$manifestPath = Join-Path $assetsDir 'android-update.json'
$checksumsPath = Join-Path $assetsDir 'SHA256SUMS'
$releaseApkPath = Join-Path $assetsDir $apkName
$manifest = Get-Content -LiteralPath $manifestPath -Encoding utf8 | ConvertFrom-Json
```

工具產出精確三檔：正式 APK、`android-update.json`、`SHA256SUMS`。核對 manifest 的版本、Build、source commit、package、檔名、大小、SHA、signer、固定 tag APK URL，以及 notes；`SHA256SUMS` 包含 APK 與 manifest 的兩筆 checksum，另外記錄 checksum 檔本身的 SHA。`dist` 保持 ignored，不提交 APK 到 Git tree。

若輸出目錄已存在，工具會拒絕覆寫。先查明是否為本次已核定產物，不能直接刪除後重建；一旦公開就不可換檔。

提交本次 notes／README／手冊變更後推送發布庫。只將實際有修改且已審查的文件放入暫存；以下文件清單可依當次範圍縮減：

```powershell
git add -- README.md $notesPath docs/APP_RELEASE_MANUAL.md
git diff --cached --check
if ($LASTEXITCODE -ne 0) { throw 'Release documentation check failed' }
git diff --cached --stat
git commit -m "Prepare Android $releaseVersion build $releaseBuild release"
if ($LASTEXITCODE -ne 0) { throw 'Release documentation commit failed' }
$releaseCommit = (git rev-parse HEAD).Trim()
git push git@github.com:jerrywu-voltraware/gateway-commissioning-releases.git main
if ($LASTEXITCODE -ne 0) { throw 'Release repository push failed' }
```

## 6. 草稿上傳、完整下載核對、公開發布

先以唯讀 `gh repo view` 確認目標庫是 public，並確定維護者有寫入權限。需要使用既有 owner 登入時，只在目前程序記憶體設定 token，完成後還原；不得列印 token、開啟 `GH_DEBUG` 或將 token 寫入文件。以下區塊內放入本節要執行的 `gh` 與下載驗證命令：

```powershell
$previousGhToken = $env:GH_TOKEN
$previousGhDebug = $env:GH_DEBUG
try {
    Remove-Item Env:\GH_DEBUG -ErrorAction SilentlyContinue
    $env:GH_TOKEN = gh auth token --hostname github.com --user jerrywu-voltraware
    if ($LASTEXITCODE -ne 0 -or -not $env:GH_TOKEN) { throw 'Release owner authentication failed' }
    gh repo view $releaseRepo --json nameWithOwner,isPrivate
    if ($LASTEXITCODE -ne 0) { throw 'Release repository lookup failed' }
    # Run the reviewed release commands here.
} finally {
    $env:GH_TOKEN = $previousGhToken
    $env:GH_DEBUG = $previousGhDebug
}
```

上傳時明列三個資產，不使用整個 build 目錄的萬用字元：

```powershell
gh release create $releaseTag --repo $releaseRepo --target $releaseCommit --draft --title "GIOS 設備助手 $releaseVersion (Build $releaseBuild)" --notes-file $notesPath $releaseApkPath $manifestPath $checksumsPath
if ($LASTEXITCODE -ne 0) { throw 'Draft upload failed' }
$draftReviewDir = Join-Path $releaseRoot "dist\draft-review-$releaseTag"
py -3 -X utf8 tools/stage_release.py --tag $releaseTag --destination $draftReviewDir --android-build-tools $androidTools --allow-draft
if ($LASTEXITCODE -ne 0) { throw 'Draft download verification failed' }
```

`stage_release.py` 會重新下載全部三檔，核對 asset 集合、manifest、實體 APK metadata／signer／大小／全檔 SHA、checksum。再將下載到 `$draftReviewDir/releases/$releaseTag/` 的**三檔 hash**與原始核定三檔逐一比對。HTTP 200、檔案存在、GitHub API digest 或只下載前幾個 bytes 都不足以代替完整下載驗證。網路慢時可以採用另經審查的分段下載，但必須核對每段 Range、重組全部 bytes 並計算完整 SHA。Build 51 起，草稿完整下載核對使用工作區 `tools/deployment/download_build5N_draft.py`（輸出 `docs/test_results/build5N_draft_verification_<date>.json`，owner token 只在程序記憶體）；`stage_release.py --allow-draft` 仍可作為等效替代。

草稿不可啟用 APP 更新。檔案、正式部署基準、發布說明與既有授權皆核對完成後，公開 stable 並指定 latest：

```powershell
gh release edit $releaseTag --repo $releaseRepo --draft=false --latest
if ($LASTEXITCODE -ne 0) { throw 'Stable publication failed' }
gh release view $releaseTag --repo $releaseRepo --json tagName,isDraft,isPrerelease,url,assets
if ($LASTEXITCODE -ne 0) { throw 'Published release read-back failed' }
```

使用不含 GitHub 憑證的獨立下載再驗一次三資產與 latest。公開 repo 不等於草稿公開；必須確認 `isDraft=false`、`isPrerelease=false`，且 release 最新指標指向本次 tag。

## 7. 啟用正式 APP 線上更新

**GitHub 公開發布與正式 APP 更新通道是兩個步驟。** 前者提供公開下載點；後者要將驗證過的三資產送到正式站，再切換 `latest.json`。只有兩者與回讀驗證都完成，才能宣告「已發布並啟用線上更新」。

通用 `tools/stage_release.py --activate` 只啟用 `--destination` 指定的**本機目錄**，不會自動 SSH 部署正式站。需要檢查 stable 下載時可執行：

```powershell
$localDeliveryDir = Join-Path $releaseRoot 'dist\backend-delivery'
py -3 -X utf8 tools/stage_release.py --tag $releaseTag --destination $localDeliveryDir --android-build-tools $androidTools --activate
if ($LASTEXITCODE -ne 0) { throw 'Local backend delivery verification failed' }
```

正式站資產根目錄為 `/home/jerrywu/android-app-releases`；不可變目錄為 `releases/<tag>/`。既有後台以 readonly mount 讀取它，提供驗證過的 `/api/app/updates/android/latest` 與 `/api/app/updates/android/<tag>/apk`。單純 APP 發布不需要重建或重啟後台容器。

2026-10-03 的 Build 50 使用工作區 `tools/deployment/android_build50_rollout.py`、`activate_build50_verified.py` 與 `verify_android50_public_channel.py`，只適用 42→50；唯一 run-id 為 `20261003T124729Z`，實際 source 為 c8e4ea1，完整 pins 與完成證據見工作區 `CONTINUE_2026-10-03_BUILD50_PUBLICATION.md`。公開資產不可覆寫；這些工具不可直接套用下一版。

2026-10-03 的 **Build 51 已發布並啟用正式通道**，本輪固定 50→51。使用工作區 `tools/deployment/android_build51_rollout.py`、`activate_build51_verified.py`、`verify_android51_public_channel.py`；唯一 run-id `20261003T153839Z`，來源 `3b320c7c60c1f772a709bd7c19cd7fe7eb719832`，共享 pubspec 為 `1.0.11+51`。三資產 pins 在工作區 `docs/test_results/android_build51_rollout_pins.json`；回復資料在 VPS `/home/jerrywu/android-app-releases/.rollout-1.0.11-b51-20261003T153839Z`。草稿、公開匿名完整下載與正式 HTTPS 新51／舊50 APK驗證均通過，正式服務保持本輪基準不變；完整紀錄見 `CONTINUE_2026-10-03_BUILD51_PUBLICATION.md`。使用者自行從 APP 更新，這輪沒有 ADB 安裝或手機內升級驗收。上述工具與公開資產皆固定於 Build 51，不可改寫冒充下一版。

2026-10-06 的 **Build 52 已發布並啟用正式通道**，本輪固定 51→52。使用工作區 `tools/deployment/android_build52_rollout.py`、`activate_build52_verified.py`、`verify_android52_public_channel.py`、`verify_build52_vps_https.py`、`download_build52_draft.py`（測試 `test_android_build52_rollout.py`）；唯一 run-id `20261005T181012Z`（`docs/test_results/build52_rollout_runid.json`），來源 `0a94090d722d6dfe328706579fea0abf7b442ce0`，共享 pubspec 為 `1.0.11+52`，GitHub Release ID 403991853。三資產 pins 在工作區 `docs/test_results/android_build52_rollout_pins.json`；回復資料在 VPS `/home/jerrywu/android-app-releases/.rollout-1.0.11-b52-20261005T181012Z`。正式指標約 2026-10-05 18:16 UTC（台灣 10-06 02:16）由 51 切換為 52。草稿、公開匿名完整下載與正式 HTTPS 新52／舊51 APK 驗證均通過，正式服務保持本輪基準不變；完整紀錄見工作區 `CONTINUE_2026-10-06_BUILD52_PUBLICATION.md` 與 `docs/test_results/build52_publication_2026-10-06.md`。使用者自行從 APP 更新，這輪沒有 ADB 安裝或手機內升級驗收。上述工具與公開資產皆固定於 Build 52，不可改寫冒充下一版。

2026-10-06 的 **Build 53 已發布並啟用正式通道**，本輪固定 52→53。使用工作區 `tools/deployment/android_build53_rollout.py`、`activate_build53_verified.py`、`verify_android53_public_channel.py`、`verify_build53_vps_https.py`、`download_build53_draft.py`（測試 `test_android_build53_rollout.py`，`py -3 -X utf8 -m unittest discover -s tools/deployment -p test_android_build53_rollout.py -v`）。來源 `4de830202ad13414ca8cb380050a2e463a6ee87a`。舊資產 pins 為 Build 52 三檔；新 pins 在工作區 `docs/test_results/android_build53_rollout_pins.json`；唯一 run-id `20261006T045041Z`（`docs/test_results/build53_rollout_runid.json`），GitHub Release ID 404325232。回復資料在 VPS `/home/jerrywu/android-app-releases/.rollout-1.0.11-b53-20261006T045041Z`。正式指標約 2026-10-06 04:53 UTC（台灣 12:53）由 52 切換為 53。草稿、公開匿名完整下載與正式 HTTPS 新53／舊52 APK 驗證均通過，正式服務保持本輪基準不變（後台 v1.37.0 已於基準前部署）；完整紀錄見工作區 `CONTINUE_2026-10-06_BUILD53_PUBLICATION.md` 與 `docs/test_results/build53_publication_2026-10-06.md`。使用者自行從 APP 更新，這輪沒有 ADB 安裝或手機內升級驗收。上述工具與公開資產皆固定於 Build 53，不可改寫冒充下一版。

2026-10-06 的 **Build 54 已發布並啟用正式通道**，本輪固定 53→54。使用工作區 `tools/deployment/android_build54_rollout.py`、`activate_build54_verified.py`、`verify_android54_public_channel.py`、`verify_build54_vps_https.py`、`download_build54_draft.py`（測試 `test_android_build54_rollout.py`，`py -3 -X utf8 -m unittest discover -s tools/deployment -p test_android_build54_rollout.py -v`）。來源 `549a3ff0bf0fb5314c2b6583086ddd593fedd239`。舊資產 pins 為 Build 53 三檔；新 pins 在工作區 `docs/test_results/android_build54_rollout_pins.json`；唯一 run-id `20261006T072143Z`（`docs/test_results/build54_rollout_runid.json`），GitHub Release ID 404426425。回復資料在 VPS `/home/jerrywu/android-app-releases/.rollout-1.0.11-b54-20261006T072143Z`。正式指標約 2026-10-06 07:24 UTC（台灣 15:24）由 53 切換為 54。草稿、公開匿名完整下載與正式 HTTPS 新54／舊53 APK 驗證均通過，正式服務保持本輪基準不變（後台 HEAD 4598fbc）；完整紀錄見工作區 `CONTINUE_2026-10-06_BUILD54_PUBLICATION.md` 與 `docs/test_results/build54_publication_2026-10-06.md`。使用者自行從 APP 更新，這輪沒有 ADB 安裝或手機內升級驗收。上述工具與公開資產皆固定於 Build 54，不可改寫冒充下一版。

以下保留 Build 42 的歷史工具說明：`tools/deployment/android_build42_rollout.py` **固定只做 `1.0.11 Build 41 → 42`**，來源 `b997b7b8e0dcba3169f9f78c732ed42746cc3ad1`。它不是通用下一版發布器；後續版本不可照抄舊 helper 的 run-id、tag、source 或 hash，也不可修改舊 helper 來冒充新的核定流程。

Build 42 的正式啟用使用已獨立審查的 `activate_build42_verified.py`：先完整匿名下載，再重查公開 stable/latest 及資產身分、重新計算三資產 hash，最後呼叫相同 rollout 的遠端原子切換。它固定核定 pins、helper hash 與 run-id，只適用此次 Build 42。

每次正式更新依序執行：

1. 唯讀記錄目前正式 latest、舊版本完整三資產 hash、API health、容器 ID／StartedAt／image／狀態、後台 commit、readonly mount；不讀出或記錄敏感環境值。
2. 以本次已驗證的 source commit、APK 名、三檔 SHA 建立核定 pins，使用唯一 UTC run-id；後續 stage、activate、rollback 必須使用同一組 pins 與 run-id。
3. 準備並獨立審查本次專用 rollout／verifier，固定「目前舊版 → 本次新版」，保持 Build 遞增、來源與三檔 hash、舊資產不可覆寫、publish lock、同 filesystem rename、history 備份與 atomic latest replace 等護欄。用離線 fixtures 驗證不相關／更高版本指標、壞 hash、非 public、draft、錯誤 source 等都會拒絕。
4. 執行本次 helper 的 `stage`：驗舊 pointer 和舊三檔 → 上傳精確三檔到唯一 incoming → 伺服器重算完整 hash。此時正式 latest 仍是舊版。
5. 確認 GitHub 已 public stable，重新完整下載與比對三檔；執行同 helper 的 `activate`：發布不可變目錄 → 備份舊 pointer 與 pins → 原子切換 latest。
6. 正式回讀確認最新版本／Build／source／APK route；以既有後台登入憑證完整下載新 APK，核對 bytes／SHA 及 `no-store`、`nosniff`，再核對舊 APK 固定 URL 與 hash 未變。未認證的 latest／APK 應為 401。驗證保留 HTTPS CA 與主機名稱檢查，不用關閉 TLS 驗證來求通過。
7. 與操作前基準比較容器／後台／mount 未變，獨立匿名確認 GitHub latest 與完整三資產下載。只宣告實際通過的項目。

Build 42 工具的參數介面如下，**僅供辨識，這是含 placeholder 的說明，不是可直接執行的命令**：

```text
py -3 -X utf8 tools/deployment/android_build42_rollout.py <stage|activate|rollback>
  --run-id <本次唯一UTC run-id>
  --assets <已核定Build42三資產目錄>
  --source-commit <固定Build42完整來源commit>
  --apk-name <固定Build42檔名>
  --apk-sha256 <已驗APK SHA-256>
  --manifest-sha256 <已驗manifest SHA-256>
  --checksums-sha256 <已驗SHA256SUMS SHA-256>
  --execute-authorized
```

`--execute-authorized` 是工具的執行護欄，不是新的使用者授權來源；本次發布及正式通道啟用必須已在使用者同意的範圍。現場實機測試中不得為了發布而重建、重啟或暫停容器。不要操作閘道器／PTU、修改 Wi-Fi 或上傳政策來驗證 APP 發布。

## 8. 失敗處理與完成紀錄

- 草稿驗證失敗：維持草稿和舊正式 latest，修正原因後重新驗證。已公開的資產不能替換；需要不同 APP bytes 時保留 `1.0.11`，增加新的 Build。
- 正式 pointer 啟用後發現問題：使用**當次**已審查的 rollback、原 run-id 與核定 pins，回復已備份的舊 latest，保留所有舊／新資產及證據。不要手改成不相關 tag、刪除 Release 或覆寫 APK。
- 回復更新指標只阻止繼續提供新版，**不會把已安裝新版 Build 的手機降版**。修正已安裝新版的問題，要提供更高 Build 的修正版；不使用強制降版、卸載或清資料代替更新。
- lock 存在時先查明是否還有發布程序運作；不能直接移除正在使用的 lock。中斷後依 history／pointer／hash 恢復，不憑檔名判斷完成。

完成後更新 README 為實際公開版與 APK 下載連結，提交並推送文件；記錄 APP source commit、release 文件 commit、tag、三資產 hash、APK signer、測試結果、正式通道回讀、run-id／history 位置。將逐步證據寫入工作區 `docs/test_results`，進度寫入 `CONTINUE_2026-09-24_HOME.md`，最新狀態追加至 `HANDBOOK_CODEX.md` 底部。不把憑證值放入任何紀錄。

**Git 提交、Git 推送、GitHub Release 公開、正式 latest 啟用、手機安裝／APP 內升級驗收要分別記錄。** 若手機沒有安裝或沒有實際跑完升級，就明寫未驗，不把下載驗證當成手機驗收。

## 9. iOS 同版本 Build 上傳至 TestFlight

Windows APK 發布不會建立 iOS Archive。iOS 必須在有既有 Apple signing／provisioning 設定的 Mac 上，以同一核定 source 建置，Version 維持 `1.0.11`，Build 使用核定的 `N`。若 App Store Connect 現有紀錄不符合此版本策略，先回報實際差異，不自行建立另一個 Version 或改掉審查中的提交。

1. 在 Mac 同步核定 commit，確認工作樹乾淨、`pubspec.yaml = 1.0.11+N`。確認 App Store Connect 此 Version 未使用該 Build；若已使用，兩平台下一輪統一採更高的未使用 Build，不重傳不同產物冒充同 Build。
2. 使用既有 `APP_v2/.secrets/prod.env`、`.secrets/ca.crt` 與簽章設定；不複製憑證內容到對話或報告。先在 `APP_v2` 執行 `ruby tools/build_ios.rb --check`，並在本次 iOS 建置授權範圍內執行 `ruby tools/build_ios.rb --configure`。
3. 此 Ruby helper 的 `--configure` 只準備本機 Flutter/Xcode 設定；`--build` 是 unsigned debug 檢查，**不是正式 Archive，也不會上傳 TestFlight**。用 Xcode 開啟 `ios/Runner.xcworkspace`，核對 Runner、Release Archive、既有 Team／Bundle ID 與簽章，執行 Product → Archive。
4. 從實際 Archive 的 `Products/Applications/Runner.app/Info.plist` 核對 `CFBundleShortVersionString=1.0.11`、`CFBundleVersion=N`、Bundle ID 與簽章，再透過 Organizer 驗證及上傳 App Store Connect。不要讓上傳工具自動把 Version 改掉，或悄悄把 Build 改成與本次核定不同的值。
5. 等待 Apple processing 完成，在 TestFlight 核對 `1.0.11 (N)`。依授權分配內部／外部測試群組、填寫本次 What to Test 與必要資訊；有外測審查需求時依實際狀態提交。Apple 同一 Version 同時只允許一個 Build 在 TestFlight 審查中，前一個尚未完成時不要為搶時間另開 Version。[Apple：外部測試流程](https://developer.apple.com/help/app-store-connect/test-a-beta-version/invite-external-testers/)
6. 使用 iPhone 透過 TestFlight 更新，驗證實際 Version／Build、既有資料及本次功能；記錄處理、審查、可測試及實機結果，各狀態不可混稱。

**只為 TestFlight 上傳新 Build，不代表授權撤回、替換既有審查提交或正式送 App Store 發布。** 保留既有審查中的版本與所選 Build；若需要替換該提交或做新的 App Store 正式版本發布，另外取得使用者明確決定。固定 `1.0.11` 是目前 Android／TestFlight 更新策略，不是承諾 Apple 永遠允許已正式上架的同版本再作另一筆商店版本更新。
