import sys
import os

# 讓 Python 找到 src 資料夾
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from unittest.mock import patch, MagicMock
from src.chatgpt import ChatGPT, DALLE
from src.models import OpenAIModel


class TestChatGPT(unittest.TestCase):
    def setUp(self):
        self.api_key = 'sk-test-key'
        self.model_engine = 'gpt-3.5-turbo'
        self.model = OpenAIModel(self.api_key, self.model_engine)
        self.chatgpt = ChatGPT(self.model)

    @patch('src.models.OpenAI')
    def test_get_response(self, mock_openai):
        # 設置mock
        mock_client = MagicMock()
        mock_openai.return_value = mock_client
        
        mock_response = MagicMock()
        mock_response.choices = [MagicMock()]
        mock_response.choices[0].message.content = 'Hello! How can I help you?'
        mock_client.chat.completions.create.return_value = mock_response
        
        # 測試
        result = self.chatgpt.get_response("Hello")
        
        # 驗證
        self.assertEqual(result, 'Hello! How can I help you?')
        mock_client.chat.completions.create.assert_called_once()


class TestDALLE(unittest.TestCase):
    def setUp(self):
        self.api_key = 'sk-test-key'
        self.model_engine = 'gpt-3.5-turbo'
        self.model = OpenAIModel(self.api_key, self.model_engine)
        self.dalle = DALLE(self.model)

    @patch('src.models.OpenAI')
    def test_generate(self, mock_openai):
        # 設置mock
        mock_client = MagicMock()
        mock_openai.return_value = mock_client
        
        mock_response = MagicMock()
        mock_response.data = [MagicMock()]
        mock_response.data[0].url = 'https://test-image-url.com/image.jpg'
        mock_client.images.generate.return_value = mock_response
        
        # 測試
        result = self.dalle.generate("A beautiful sunset")
        
        # 驗證
        self.assertEqual(result, 'https://test-image-url.com/image.jpg')
        mock_client.images.generate.assert_called_once()


if __name__ == '__main__':
    unittest.main(verbosity=2) 