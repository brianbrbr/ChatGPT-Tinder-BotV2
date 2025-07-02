# Replit 部署指南

## 🚀 快速部署到 Replit

### 1. 創建 Replit 專案
1. 前往 [replit.com](https://replit.com/)
2. 點擊 "Create Repl"
3. 選擇 "Import from GitHub"
4. 輸入你的 GitHub 倉庫 URL
5. 點擊 "Import from GitHub"

### 2. 設置環境變數
1. 在 Replit 左側面板點擊 "Tools" → "Secrets"
2. 添加以下環境變數：

```
Key: OPENAI_API
Value: sk-your-actual-openai-api-key-here

Key: OPENAI_MODEL_ENGINE  
Value: gpt-4

Key: TINDER_TOKEN
Value: your-actual-tinder-token-here

Key: SYSTEM_MESSAGE
Value: You are a helpful assistant.

Key: APP_PORT
Value: 8080
```

### 3. 運行專案
1. 點擊 "Run" 按鈕
2. 等待依賴安裝完成
3. 查看 Console 輸出

### 4. 檢查部署狀態
- **成功**: 看到 "✅ 環境變數檢查通過" 和 "INFO: Uvicorn running"
- **失敗**: 查看錯誤訊息並修復

## 🔧 故障排除

### 常見錯誤

#### 1. "OPENAI_API 環境變數未設置"
**解決方案**:
- 檢查 Replit Secrets 是否正確設置
- 確認 Key 名稱是 `OPENAI_API`（大寫）
- 重新啟動 Replit

#### 2. "ModuleNotFoundError"
**解決方案**:
- 等待依賴安裝完成
- 手動運行 `pip install -r requirements.txt`
- 檢查 `requirements.txt` 是否正確

#### 3. "Port already in use"
**解決方案**:
- 停止其他正在運行的服務
- 修改 `APP_PORT` 為其他端口（如 8081）

### 測試部署

#### 1. 本地測試
```bash
python replit_start.py
```

#### 2. API 測試
```bash
python test_replit.py
```

#### 3. 外部訪問
- 複製 Replit 提供的 URL
- 在瀏覽器中訪問
- 應該看到 `{"message": "Hello World"}`

## 📊 監控和維護

### 查看日誌
- 在 Replit Console 中查看實時日誌
- 檢查是否有錯誤訊息
- 監控 API 使用量

### 更新部署
1. 在本地修改代碼
2. 推送到 GitHub
3. 在 Replit 中點擊 "Sync"
4. 重新運行

### 設置定時任務
1. 註冊 [cron-job.org](https://cron-job.org/)
2. 創建新的 cronjob
3. URL 設為你的 Replit 應用網址
4. 設置每 5 分鐘執行一次

## 🔒 安全注意事項

### 環境變數安全
- ✅ 在 Replit Secrets 中設置敏感資訊
- ❌ 不要在代碼中硬編碼 API keys
- ❌ 不要分享你的 Secrets

### 訪問控制
- 考慮設置 Replit 專案為私有
- 定期更換 API keys
- 監控異常使用

## 📞 支援

如果遇到問題：
1. 檢查 Console 錯誤訊息
2. 運行 `python test_replit.py` 診斷
3. 查看 `SECURITY.md` 安全指南
4. 檢查 `README.md` 詳細說明 