# 安全部署指南

## 🔒 API Key 安全

### 重要提醒
- **永遠不要**將 API keys 提交到 Git 倉庫
- **永遠不要**在公開代碼中硬編碼敏感資訊
- **永遠不要**分享你的 API keys

### 安全做法

#### 1. 本地開發
```bash
# 創建 .env 文件（已在 .gitignore 中）
cp env.example .env

# 編輯 .env 文件，填入真實的 API keys
# 但不要提交到 Git
```

#### 2. Replit 部署
1. 在 Replit 中設置 Secrets（環境變數）
2. 不要在任何代碼文件中寫入真實 API keys
3. 使用 `os.getenv()` 從環境變數讀取

#### 3. GitHub Actions（如果使用）
```yaml
# 在 GitHub Secrets 中設置
# 不要在任何 yaml 文件中寫入真實 keys
```

### 檢查清單

#### 提交前檢查
- [ ] `.env` 文件沒有被提交
- [ ] 沒有硬編碼的 API keys
- [ ] 測試文件使用 mock 或環境變數
- [ ] `env.example` 只包含範例值

#### 部署前檢查
- [ ] 環境變數正確設置
- [ ] API keys 沒有出現在日誌中
- [ ] 錯誤訊息不洩露敏感資訊

### 如果 API Key 已洩露

1. **立即撤銷**：前往 OpenAI/Tinder 平台撤銷舊的 key
2. **生成新的**：創建新的 API key
3. **更新環境變數**：在所有部署環境中更新
4. **檢查使用量**：監控是否有異常使用

### 安全最佳實踐

1. **最小權限原則**：只給必要的權限
2. **定期輪換**：定期更換 API keys
3. **監控使用**：定期檢查 API 使用量
4. **錯誤處理**：不要在錯誤訊息中洩露敏感資訊

### 環境變數範例

```env
# ✅ 正確做法
OPENAI_API=sk-your-actual-key-here
TINDER_TOKEN=your-actual-token-here

# ❌ 錯誤做法 - 不要這樣做
OPENAI_API=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
```

### 測試安全

```python
# ✅ 正確做法 - 使用環境變數
api_key = os.getenv('OPENAI_API')

# ✅ 正確做法 - 使用 mock 測試
@patch('src.models.OpenAI')
def test_api(self, mock_openai):
    # 測試邏輯

# ❌ 錯誤做法 - 不要硬編碼
api_key = 'sk-real-key-here'
``` 