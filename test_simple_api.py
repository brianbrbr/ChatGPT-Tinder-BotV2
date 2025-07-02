#!/usr/bin/env python3
"""
簡單的 OpenAI API 測試
"""

import os
from src.models import OpenAIModel
from src.chatgpt import ChatGPT
from dotenv import load_dotenv

# 載入環境變數
load_dotenv('.env')

def test_simple_api():
    """簡單的 API 測試"""
    
    # 使用你的 API key
    api_key = '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'
    model_engine = 'gpt-3.5-turbo'
    
    print(f"🔑 API Key: {api_key[:10]}...")
    print(f"🤖 模型: {model_engine}")
    print("-" * 50)
    
    try:
        # 創建模型實例
        print("📝 創建模型實例...")
        model = OpenAIModel(api_key, model_engine)
        chatgpt = ChatGPT(model)
        print("✅ 模型實例創建成功")
        
        # 簡單測試
        print("\n📝 發送簡單問題...")
        user_message = "Say hello in one word"
        print(f"問題: {user_message}")
        
        response = chatgpt.get_response(user_message)
        print(f"✅ 回覆: {response}")
        
        print("\n🎉 測試成功！你的 OpenAI API 連接正常。")
        
    except Exception as e:
        print(f"❌ 錯誤: {e}")
        
        # 提供具體的錯誤建議
        if "insufficient_quota" in str(e):
            print("\n💡 建議:")
            print("1. 檢查你的 OpenAI 帳戶餘額")
            print("2. 前往 https://platform.openai.com/account/billing 查看配額")
            print("3. 如果是免費帳戶，可能已用完免費額度")
            print("4. 考慮升級到付費帳戶或等待下個月重置")
        elif "invalid_api_key" in str(e):
            print("\n💡 建議:")
            print("1. 檢查 API key 是否正確")
            print("2. 前往 https://platform.openai.com/api-keys 重新生成")
        elif "rate_limit" in str(e):
            print("\n💡 建議:")
            print("1. 你發送了太多請求，請稍等片刻再試")
        else:
            print("\n💡 建議:")
            print("1. 檢查網路連接")
            print("2. 確認 OpenAI 服務是否正常")

if __name__ == "__main__":
    test_simple_api() 