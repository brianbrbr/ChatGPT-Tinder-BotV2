#!/usr/bin/env python3
"""
測試真實 OpenAI API 回覆
"""

import os
from src.models import OpenAIModel
from src.chatgpt import ChatGPT
from dotenv import load_dotenv

# 載入環境變數
load_dotenv('.env')

def test_openai_api():
    """測試 OpenAI API 真實回覆"""
    
    # 從環境變數讀取 API key
    api_key = os.getenv('OPENAI_API')
    model_engine = os.getenv('OPENAI_MODEL_ENGINE') or 'gpt-4'
    
    if not api_key:
        print("❌ 請在 .env 文件中設置 OPENAI_API")
        return
    
    print(f"🔑 使用 API Key: {api_key[:10]}...")
    print(f"🤖 使用模型: {model_engine}")
    print("-" * 50)
    
    try:
        # 創建模型實例
        model = OpenAIModel(api_key, model_engine)
        chatgpt = ChatGPT(model)
        
        # 測試 1: 直接使用 models.py 的 chat_completion
        print("📝 測試 1: 直接呼叫 chat_completion")
        messages = [
            {'role': 'system', 'content': 'You are a helpful assistant.'},
            {'role': 'user', 'content': 'Hello! What is the capital of France?'}
        ]
        
        response = model.chat_completion(messages)
        print(f"✅ 回覆: {response.choices[0].message.content}")
        print("-" * 50)
        
        # 測試 2: 使用 ChatGPT 類的 get_response
        print("📝 測試 2: 使用 ChatGPT.get_response")
        user_message = "What is 2 + 2?"
        response = chatgpt.get_response(user_message)
        print(f"✅ 回覆: {response}")
        print("-" * 50)
        
        # 測試 3: 測試圖片生成 (DALLE)
        print("📝 測試 3: 圖片生成 (DALLE)")
        dalle = ChatGPT(model)  # 這裡應該用 DALLE 類，但為了簡化直接用 ChatGPT
        try:
            # 注意：圖片生成需要 DALLE 模型，這裡只是測試 API 連接
            print("⚠️  圖片生成測試跳過（需要 DALLE 模型）")
        except Exception as e:
            print(f"❌ 圖片生成錯誤: {e}")
        print("-" * 50)
        
        # 測試 4: 測試對話生成
        print("📝 測試 4: 對話生成")
        from src.dialog import Dialog
        dialog = Dialog()
        
        from_user_id = "user123"
        to_user_id = "user456"
        conversation = [
            f"{from_user_id}: Hi there!",
            f"{to_user_id}: Hello! How are you?",
            f"{from_user_id}: I'm good, thanks!"
        ]
        
        dialog_input = dialog.generate_input(from_user_id, to_user_id, conversation)
        print(f"📋 生成的對話輸入:")
        print(dialog_input)
        print("-" * 50)
        
        # 測試 5: 完整流程測試
        print("📝 測試 5: 完整流程測試")
        response = chatgpt.get_response(dialog_input)
        print(f"✅ 完整流程回覆: {response}")
        
        print("\n🎉 所有測試完成！")
        
    except Exception as e:
        print(f"❌ 錯誤: {e}")
        print("請檢查你的 API key 是否正確，以及網路連接是否正常。")

if __name__ == "__main__":
    test_openai_api() 