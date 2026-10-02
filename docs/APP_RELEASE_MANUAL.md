# APP 提交、發布與更新手冊

適用專案：GIOS 現場開通；建立日期：2026-10-01。程式碼位於 `APP_v2`，Android 發布資料位於 `android_releases`，兩者是不同的 Git repository。以下 Windows 指令以 PowerShell 5.1、工作區 `F:\iot_gateway` 為例。

## 1. 固定版本規則：1.0.11 不變，只增加 Build

**依使用者決定，APP 版本號固定為 `1.0.11`，後續一般修正與更新不再增加版本號，只增加 Build。** 不得自行改成 `1.0.12`、`1.1.0`，也不得讓自動發布工具按照每次修正自動增加版本號。只有使用者明確改變這項決定時，才另行規劃版本變更。

本次基準是 **`1.0.11 (Build 39)`**，`APP_v2/pubspec.yaml` 為：

```yaml
version: 1.0.11+39
```

若兩平台都沒有占用更高的 Build，下一次只改為 `1.0.11+40`，再下一次為 `1.0.11+41`。發布前必須查詢 Android 已發布／已交付安裝的 Build，以及 App Store Connect 已上傳的 Build，確認本次數字尚未使用。**不可回退、重用已交付的 Build，或覆寫已公開的 Release 資產。** 既有早期 Build 21 修正例外不得當成日後重用 Build 的依據。

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

以下指令從同一個 PowerShell 工作階段依序執行。**`40` 只是 Build 39 後的下一版範例，不是永久預設值**；先依第 1 節核定實際 Build，再設定變數。範例不會修改目前 Build 39。

```powershell
$workspace = 'F:\iot_gateway'
$appRoot = Join-Path $workspace 'APP_v2'
$releaseRoot = Join-Path $workspace 'android_releases'
$releaseVersion = '1.0.11'
$releaseBuild = 40
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

確認暫存範圍完整後提交。Commit message 使用英文，例如 `Release Android 1.0.11 build 40`。接著確認工作樹乾淨並記錄完整 commit；不可為正式發布使用 `-AllowDirty`。

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

先確認 Java 路徑。Flutter 本身可能找到 Android Studio 的 Java，但獨立執行的 `apksigner` 仍需要正確 `JAVA_HOME`；缺少這一步會在簽章階段失敗。

```powershell
$env:JAVA_HOME = 'C:\Program Files\Android\Android Studio\jbr'
if (-not (Test-Path -LiteralPath (Join-Path $env:JAVA_HOME 'bin\java.exe'))) {
    throw 'Android Studio Java not found'
}
$androidTools = 'C:\Users\USER01\AppData\Local\Android\Sdk\build-tools\36.0.0'
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
gh release create $releaseTag --repo $releaseRepo --target $releaseCommit --draft --title "Android $releaseVersion (Build $releaseBuild)" --notes-file $notesPath $releaseApkPath $manifestPath $checksumsPath
if ($LASTEXITCODE -ne 0) { throw 'Draft upload failed' }
$draftReviewDir = Join-Path $releaseRoot "dist\draft-review-$releaseTag"
py -3 -X utf8 tools/stage_release.py --tag $releaseTag --destination $draftReviewDir --android-build-tools $androidTools --allow-draft
if ($LASTEXITCODE -ne 0) { throw 'Draft download verification failed' }
```

`stage_release.py` 會重新下載全部三檔，核對 asset 集合、manifest、實體 APK metadata／signer／大小／全檔 SHA、checksum。再將下載到 `$draftReviewDir/releases/$releaseTag/` 的**三檔 hash**與原始核定三檔逐一比對。HTTP 200、檔案存在、GitHub API digest 或只下載前幾個 bytes 都不足以代替完整下載驗證。網路慢時可以採用另經審查的分段下載，但必須核對每段 Range、重組全部 bytes 並計算完整 SHA。

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

本次使用工作區 `tools/deployment/android_build39_rollout.py`，**固定只做 `1.0.11 Build 32 → 39`**，並固定來源 `d9e4adbc7df9055b951ab22321b3fc2775ddbb5f`。它不是通用下一版發布器；**下次 Build 40 不可照抄 Build 39 的 helper、run-id、tag、source 或 hash，也不可修改舊 helper 來冒充新的核定流程。**

每次正式更新依序執行：

1. 唯讀記錄目前正式 latest、舊版本完整三資產 hash、API health、容器 ID／StartedAt／image／狀態、後台 commit、readonly mount；不讀出或記錄敏感環境值。
2. 以本次已驗證的 source commit、APK 名、三檔 SHA 建立核定 pins，使用唯一 UTC run-id；後續 stage、activate、rollback 必須使用同一組 pins 與 run-id。
3. 準備並獨立審查本次專用 rollout／verifier，固定「目前舊版 → 本次新版」，保持 Build 遞增、來源與三檔 hash、舊資產不可覆寫、publish lock、同 filesystem rename、history 備份與 atomic latest replace 等護欄。用離線 fixtures 驗證不相關／更高版本指標、壞 hash、非 public、draft、錯誤 source 等都會拒絕。
4. 執行本次 helper 的 `stage`：驗舊 pointer 和舊三檔 → 上傳精確三檔到唯一 incoming → 伺服器重算完整 hash。此時正式 latest 仍是舊版。
5. 確認 GitHub 已 public stable，重新完整下載與比對三檔；執行同 helper 的 `activate`：發布不可變目錄 → 備份舊 pointer 與 pins → 原子切換 latest。
6. 正式回讀確認最新版本／Build／source／APK route；以既有後台登入憑證完整下載新 APK，核對 bytes／SHA 及 `no-store`、`nosniff`，再核對舊 APK 固定 URL 與 hash 未變。未認證的 latest／APK 應為 401。驗證保留 HTTPS CA 與主機名稱檢查，不用關閉 TLS 驗證來求通過。
7. 與操作前基準比較容器／後台／mount 未變，獨立匿名確認 GitHub latest 與完整三資產下載。只宣告實際通過的項目。

Build 39 工具的參數介面如下，**僅供辨識，這是含 placeholder 的說明，不是可直接執行的命令**：

```text
py -3 -X utf8 tools/deployment/android_build39_rollout.py <stage|activate|rollback>
  --run-id <本次唯一UTC run-id>
  --assets <已核定Build39三資產目錄>
  --source-commit <固定Build39完整來源commit>
  --apk-name <固定Build39檔名>
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
