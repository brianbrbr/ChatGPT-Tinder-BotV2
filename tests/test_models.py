import sys
import os

# ✅ 讓 Python 找到 src 資料夾
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from unittest.mock import patch, MagicMock
from src.models import OpenAIModel


class TestOpenAIModel(unittest.TestCase):
    def setUp(self):
        self.api_key = 'sk-test-key-for-testing-only'
        self.model_engine = 'gpt-4'
        self.image_size = '512x512'

    @patch('src.models.OpenAI')
    def test_chat_completion(self, mock_openai):
        # 設置mock
        mock_client = MagicMock()
        mock_openai.return_value = mock_client
        
        mock_response = MagicMock()
        mock_response.choices = [MagicMock()]
        mock_response.choices[0].message.content = 'Test response'
        mock_client.chat.completions.create.return_value = mock_response
        
        # 創建模型實例（在mock之後）
        self.model = OpenAIModel(self.api_key, self.model_engine, self.image_size)
        
        # 測試數據
        messages = [
            {'role': 'system', 'content': 'You are a helpful assistant.'},
            {'role': 'user', 'content': 'Hello'}
        ]
        
        # 執行測試
        result = self.model.chat_completion(messages)
        
        # 驗證
        mock_client.chat.completions.create.assert_called_once_with(
            model=self.model_engine,
            messages=messages
        )
        self.assertEqual(result, mock_response)

    @patch('src.models.OpenAI')
    def test_image_generation(self, mock_openai):
        # 設置mock
        mock_client = MagicMock()
        mock_openai.return_value = mock_client
        
        mock_response = MagicMock()
        mock_response.data = [MagicMock()]
        mock_response.data[0].url = 'https://test-image-url.com/image.jpg'
        mock_client.images.generate.return_value = mock_response
        
        # 創建模型實例（在mock之後）
        self.model = OpenAIModel(self.api_key, self.model_engine, self.image_size)
        
        # 測試數據
        prompt = 'A beautiful sunset'
        
        # 執行測試
        result = self.model.image_generation(prompt)
        
        # 驗證
        mock_client.images.generate.assert_called_once_with(
            prompt=prompt,
            n=1,
            size=self.image_size
        )
        self.assertEqual(result, 'https://test-image-url.com/image.jpg')

    @patch('src.models.OpenAI')
    def test_model_initialization(self, mock_openai):
        """測試模型初始化"""
        mock_client = MagicMock()
        mock_openai.return_value = mock_client
        
        self.model = OpenAIModel(self.api_key, self.model_engine, self.image_size)
        
        self.assertEqual(self.model.model_engine, self.model_engine)
        self.assertEqual(self.model.image_size, self.image_size)
        self.assertIsNotNone(self.model.client)
        mock_openai.assert_called_once_with(api_key=self.api_key)


if __name__ == '__main__':
    unittest.main(verbosity=2)
