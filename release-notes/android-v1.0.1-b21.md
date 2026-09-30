Android 1.0.1（Build 21）— Android 9 更新相容性修正。

- 修正 Android 9 下載更新後無法正確讀取安裝檔簽章的問題。
- 維持從已修補的 Android Build 20 更新到 Build 21；iOS Build 21 與 TestFlight 設定不變。
- 更新前繼續核對安裝檔完整性與正式簽章，並交由 Android 系統確認安裝。
- 閘道器配置期間不啟動更新；下載失敗可以重試。

Android 9 測試前須先安裝含修正的 Build 20。原 Android 1.0.0（Build 21）保留供歷史核對，請勿再安裝使用。
已經安裝原 Build 21 的手機不會收到相同 Build 21 的更新提示，需另待較高 Build 的版本。
