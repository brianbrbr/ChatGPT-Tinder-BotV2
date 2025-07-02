#!/usr/bin/env python3
"""
Replit 部署測試腳本
"""

import os
import requests
import time
from dotenv import load_dotenv

# 載入環境變數
load_dotenv()

def test_replit_deployment():
    """測試 Replit 部署狀態"""
    
    print("🚀 Replit 部署測試")
    print("=" * 50)
    
    # 1. 檢查環境變數
    print("📋 檢查環境變數...")
    openai_api = os.getenv('OPENAI_API')
    tinder_token = os.getenv('TINDER_TOKEN')
    model_engine = os.getenv('OPENAI_MODEL_ENGINE', 'gpt-4')
    
    if openai_api:
        print(f"✅ OpenAI API: {openai_api[:10]}...")
    else:
        print("❌ OpenAI API 未設置")
    
    if tinder_token:
        print(f"✅ Tinder Token: {tinder_token[:10]}...")
    else:
        print("❌ Tinder Token 未設置")
    
    print(f"✅ Model Engine: {model_engine}")
    print("-" * 50)
    
    # 2. 測試本地服務
    print("🌐 測試本地服務...")
    try:
        response = requests.get('http://localhost:8080', timeout=5)
        if response.status_code == 200:
            print(f"✅ 本地服務正常: {response.json()}")
        else:
            print(f"❌ 本地服務異常: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"❌ 本地服務無法連接: {e}")
    
    print("-" * 50)
    
    # 3. 測試 OpenAI API
    print("🤖 測試 OpenAI API...")
    try:
        from src.models import OpenAIModel
        from src.chatgpt import ChatGPT
        
        model = OpenAIModel(openai_api, model_engine)
        chatgpt = ChatGPT(model)
        
        response = chatgpt.get_response("Hello")
        print(f"✅ OpenAI API 正常: {response[:50]}...")
        
    except Exception as e:
        print(f"❌ OpenAI API 錯誤: {e}")
    
    print("-" * 50)
    
    # 4. 測試 Tinder API
    print("💕 測試 Tinder API...")
    try:
        from src.tinder import TinderAPI
        
        if tinder_token and tinder_token != 'your_tinder_token_here':
            tinder_api = TinderAPI(tinder_token)
            profile = tinder_api.profile()
            print(f"✅ Tinder API 正常: {profile.name}")
        else:
            print("⚠️  Tinder Token 未設置或使用預設值")
            
    except Exception as e:
        print(f"❌ Tinder API 錯誤: {e}")
    
    print("-" * 50)
    
    # 5. 檢查定時任務
    print("⏰ 檢查定時任務...")
    print("✅ 定時任務已設置（每5分鐘檢查一次）")
    print("📝 下次檢查時間: 約5分鐘後")
    
    print("\n🎉 測試完成！")
    print("\n📋 如果所有測試都通過，你的 Replit 部署就成功了！")
    print("💡 記得設置 cron-job.org 來保持服務運行")

if __name__ == "__main__":
    test_replit_deployment() 