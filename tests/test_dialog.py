import sys
import os

# 讓 Python 找到 src 資料夾
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from src.dialog import Dialog


class TestDialog(unittest.TestCase):
    def setUp(self):
        self.dialog = Dialog()

    def test_generate_input(self):
        """測試對話輸入生成"""
        from_user_id = "user123"
        to_user_id = "user456"
        
        # 模擬對話記錄
        dialog = [
            f"{from_user_id}: Hello there!",
            f"{to_user_id}: Hi! How are you?",
            f"{from_user_id}: I'm good, thanks!"
        ]
        
        result = self.dialog.generate_input(from_user_id, to_user_id, dialog)
        
        # 驗證結果包含必要的元素
        self.assertIn('[Sender]', result)
        self.assertIn('[Receiver]', result)
        self.assertIn('Hello there!', result)
        self.assertIn('Hi! How are you?', result)
        self.assertIn('I\'m good, thanks!', result)
        self.assertIn('[Sender]:', result)
        
        # 驗證用戶ID被正確替換
        self.assertNotIn(from_user_id, result)
        self.assertNotIn(to_user_id, result)

    def test_prefix_content(self):
        """測試前綴內容"""
        self.assertIn('You are now playing the role of [Sender]', self.dialog.PREFIX)
        self.assertIn('respond to [Receiver]', self.dialog.PREFIX)
        self.assertIn('should not exceed 50 words', self.dialog.PREFIX)

    def test_empty_dialog(self):
        """測試空對話"""
        from_user_id = "user123"
        to_user_id = "user456"
        dialog = []
        
        result = self.dialog.generate_input(from_user_id, to_user_id, dialog)
        
        # 應該只包含前綴和發送者標記
        self.assertIn(self.dialog.PREFIX, result)
        self.assertIn('[Sender]:', result)
        self.assertNotIn('[Receiver]:', result)


if __name__ == '__main__':
    unittest.main(verbosity=2) 