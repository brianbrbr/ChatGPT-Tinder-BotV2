#!/usr/bin/env python3
"""
測試 GPT-4 API
"""

import os
from src.models import OpenAIModel
from src.chatgpt import ChatGPT
from dotenv import load_dotenv

# 載入環境變數
load_dotenv('.env')

def test_gpt4():
    """測試 GPT-4 API"""
    
    # 使用 GPT-4
    api_key = os.getenv('OPENAI_API') or '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'
    model_engine = 'gpt-4'
    
    print(f"🔑 API Key: {api_key[:10]}...")
    print(f"🤖 使用模型: {model_engine}")
    print("-" * 50)
    
    try:
        # 創建模型實例
        print("📝 創建 GPT-4 模型實例...")
        model = OpenAIModel(api_key, model_engine)
        chatgpt = ChatGPT(model)
        print("✅ GPT-4 模型實例創建成功")
        
        # 測試 GPT-4
        print("\n📝 測試 GPT-4 回覆...")
        user_message = "請用繁體中文回答：什麼是人工智慧？"
        print(f"問題: {user_message}")
        
        response = chatgpt.get_response(user_message)
        print(f"✅ GPT-4 回覆: {response}")
        
        print("\n🎉 GPT-4 測試成功！")
        
    except Exception as e:
        print(f"❌ 錯誤: {e}")
        
        if "insufficient_quota" in str(e):
            print("\n💡 建議: 檢查 GPT-4 配額")
        elif "model_not_found" in str(e):
            print("\n💡 建議: 確認你的帳戶有 GPT-4 存取權限")

if __name__ == "__main__":
    test_gpt4() 