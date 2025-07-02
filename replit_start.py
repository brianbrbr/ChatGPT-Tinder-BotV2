#!/usr/bin/env python3
"""
Replit 專用啟動腳本
"""

import os
import sys
from dotenv import load_dotenv

def check_environment():
    """檢查環境變數設置"""
    print("🔍 檢查環境變數...")
    
    # 載入環境變數
    load_dotenv('.env')
    
    # 檢查必要的環境變數
    openai_api = os.getenv('OPENAI_API')
    tinder_token = os.getenv('TINDER_TOKEN')
    model_engine = os.getenv('OPENAI_MODEL_ENGINE', 'gpt-4')
    
    print(f"🤖 Model Engine: {model_engine}")
    
    if openai_api:
        print(f"✅ OpenAI API: {openai_api[:10]}...")
    else:
        print("❌ OPENAI_API 未設置")
        print("💡 請在 Replit Secrets 中設置 OPENAI_API")
        return False
    
    if tinder_token and tinder_token != 'your_tinder_token_here':
        print(f"✅ Tinder Token: {tinder_token[:10]}...")
    else:
        print("⚠️  TINDER_TOKEN 未設置或使用預設值")
        print("💡 Tinder 功能將無法使用")
    
    return True

def main():
    """主函數"""
    print("🚀 ChatGPT Tinder Bot - Replit 啟動")
    print("=" * 50)
    
    # 檢查環境變數
    if not check_environment():
        print("\n❌ 環境變數檢查失敗，請設置必要的環境變數")
        print("📖 請查看 README.md 了解如何設置環境變數")
        sys.exit(1)
    
    print("\n✅ 環境變數檢查通過")
    print("🚀 啟動 FastAPI 服務...")
    
    # 啟動 FastAPI 服務
    try:
        import uvicorn
        uvicorn.run('main:app', host='0.0.0.0', port=8080)
    except Exception as e:
        print(f"❌ 服務啟動失敗: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 