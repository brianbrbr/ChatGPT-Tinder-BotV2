# ChatGPT Tinder Bot

中文 | [English](README.en.md)

[![license](https://img.shields.io/pypi/l/ansicolortags.svg)](LICENSE) [![Release](https://img.shields.io/github/v/release/TheExplainthis/ChatGPT-Tinder-Bot)](https://github.com/TheExplainthis/ChatGPT-Tinder-Bot/releases/)


## 更新
- 2023/03/03 模型換成 chat completion: `gpt-3.5-turbo`
- 2024/12/19 修復依賴問題，更新到最新版本
- 2024/12/19 支援 GPT-4 模型


## 介紹
ChatGPT 的強大，是否也想要把他串到各個聊天平台呢？這個 Repository 教你如何串到 Tinder 上，讓你忙碌時也能夠自動回覆訊息去交朋友，而這邊提供最基本的架構，只有從過去的聊天記錄去推測，會寫程式的工程師們，當然也可以把用戶的背景資訊，甚至去串圖像相關的模型，去偵測圖片，讓 ChatGPT 能夠回應的更適切。

![Demo](https://github.com/TheExplainthis/ChatGPT-Tinder-Bot/blob/main/demo/chatgpt-tinder-bot.gif)

## 快速開始

### 1. 克隆專案
```bash
git clone https://github.com/your-username/ChatGPT-Tinder-Bot.git
cd ChatGPT-Tinder-Bot
```

### 2. 安裝依賴
```bash
pip install -r requirements.txt
```

### 3. 設置環境變數
```bash
cp env.example .env
# 編輯 .env 文件，填入你的 API keys
```

### 4. 測試 API 連接
```bash
python test_gpt4.py
```

### 5. 運行專案
```bash
python main.py
```

## 詳細設置步驟

### Token 取得

#### 1. OpenAI API Token
1. 前往 [OpenAI Platform](https://platform.openai.com/)
2. 註冊/登入帳號
3. 點擊右上角頭像 → `View API keys`
4. 點擊 `Create new secret key` → 生成後即為 `OPENAI_API`
5. **重要**: 確保你的帳戶有 GPT-4 存取權限（可能需要付費帳戶）

#### 2. Tinder Token
1. 登入 [Tinder](https://tinder.com/)
2. 按 `F12` 開啟開發者工具
3. 切換到 `Network` 標籤
4. 在 Tinder 上執行任何操作（如滑動）
5. 在 Network 中找到 API 請求，查看 Request Headers 中的 `x-auth-token`

### 環境變數設置

創建 `.env` 文件：
```env
# OpenAI Configuration
OPENAI_API=sk-your-actual-api-key-here
OPENAI_MODEL_ENGINE=gpt-4

# Tinder Configuration
TINDER_TOKEN=your-tinder-token-here

# System Message
SYSTEM_MESSAGE=You are a helpful assistant.

# App Configuration
APP_PORT=8080
```

### 本地運行

#### 方法 1: 直接運行
```bash
python main.py
```

#### 方法 2: Docker 運行
```bash
docker-compose up --build
```

### 測試功能

#### 測試 API 連接
```bash
python test_gpt4.py
```

#### 運行單元測試
```bash
python tests/test_models.py
python tests/test_chatgpt.py
python tests/test_dialog.py
```

#### 運行所有測試
```bash
python tests/run_tests.py
```

## 部署到雲端

### Replit 部署
1. 前往 [replit.com](https://replit.com/)
2. 用 GitHub 帳號登入
3. 點擊 `Create` → `Import from Github`
4. 選擇你的 ChatGPT-Tinder-Bot 專案
5. 在 `Secrets` 中設置環境變數：
   - `OPENAI_API`: 你的 OpenAI API key
   - `OPENAI_MODEL_ENGINE`: `gpt-4`
   - `TINDER_TOKEN`: 你的 Tinder token
   - `SYSTEM_MESSAGE`: `You are a helpful assistant.`
6. 點擊 `Run` 開始執行

### 設置定時任務
1. 註冊 [cron-job.org](https://cron-job.org/)
2. 創建新的 cronjob
3. 設置每 5 分鐘執行一次
4. URL 設為你的 Replit 應用網址

## 功能說明

### 自動回覆機制
- **掃描頻率**: 每 5 分鐘檢查一次新訊息
- **回覆條件**: 
  - 對方發送新訊息
  - 或超過 24 小時未互動
- **回覆限制**: 每次回覆不超過 50 字，並以問題結尾

### 自定義設定

#### 調整掃描頻率
在 `main.py` 第 27 行：
```python
@scheduler.scheduled_job("cron", minute='*/5', second=0, id='reply_messages')
# 改為每 10 分鐘: minute='*/10'
# 改為每小時: minute=0
```

#### 調整回覆數量
在 `main.py` 第 34 行：
```python
for match in tinder_api.matches(limit=50):
# 改為 limit=10 只處理前 10 個配對
```

#### 自定義回覆風格
在 `src/dialog.py` 中修改 `PREFIX`：
```python
PREFIX = """
    You are now playing the role of [Sender] and your task is to respond to [Receiver] 
    in the conversation below. Your response should be friendly and engaging, 
    not exceed 50 words and end with a question. Please respond in the language used by [Sender].
"""
```

## 修復的問題
- ✅ 更新 OpenAI API 到最新版本 (v1.0+)
- ✅ 修復缺少的 `opencc` 依賴
- ✅ 更新 FastAPI 和 uvicorn 到最新版本
- ✅ 添加環境變數配置
- ✅ 修復 Docker 配置
- ✅ 支援 GPT-4 模型
- ✅ 添加完整的測試套件
- ✅ 改善錯誤處理和日誌記錄

## 故障排除

### 常見問題

#### 1. API 配額不足
```
Error: insufficient_quota
```
**解決方案**: 
- 檢查 OpenAI 帳戶餘額
- 升級到付費帳戶
- 等待下個月免費額度重置

#### 2. GPT-4 存取權限
```
Error: model_not_found
```
**解決方案**:
- 確認帳戶有 GPT-4 存取權限
- 可能需要付費帳戶

#### 3. Tinder Token 無效
```
Error: 401 Unauthorized
```
**解決方案**:
- 重新獲取 Tinder token
- 確認 token 沒有過期

#### 4. 依賴安裝失敗
```
Error: ModuleNotFoundError
```
**解決方案**:
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## 專案結構
```
ChatGPT-Tinder-Bot/
├── src/
│   ├── models.py      # OpenAI API 模型介面
│   ├── chatgpt.py     # ChatGPT 對話類
│   ├── tinder.py      # Tinder API 介面
│   ├── dialog.py      # 對話生成器
│   └── logger.py      # 日誌系統
├── tests/             # 測試檔案
├── main.py           # 主程式
├── config.py         # 配置管理
├── requirements.txt  # Python 依賴
├── Dockerfile        # Docker 配置
└── README.md         # 說明文件
```

## 支持我們
如果你喜歡這個專案，願意[支持我們](https://www.buymeacoffee.com/explainthis)，可以請我們喝一杯咖啡，這會成為我們繼續前進的動力！

[<a href="https://www.buymeacoffee.com/explainthis" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" height="45px" width="162px" alt="Buy Me A Coffee"></a>](https://www.buymeacoffee.com/explainthis)


## 相關專案
- [auto-tinder](https://github.com/joelbarmettlerUZH/auto-tinder/tree/master)
- [ChatGPT-Discord-Bot](https://github.com/TheExplainthis/ChatGPT-Discord-Bot)
- [ChatGPT-Line-Bot](https://github.com/TheExplainthis/ChatGPT-Line-Bot)

## 授權
[MIT](LICENSE)
