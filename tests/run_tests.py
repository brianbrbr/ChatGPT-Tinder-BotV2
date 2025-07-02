#!/usr/bin/env python3
"""
測試運行器 - 運行所有測試
"""

import sys
import os
import unittest

# 添加項目根目錄到Python路徑
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def run_all_tests():
    """運行所有測試"""
    # 發現所有測試
    loader = unittest.TestLoader()
    start_dir = os.path.dirname(__file__)
    suite = loader.discover(start_dir, pattern='test_*.py')
    
    # 運行測試
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # 返回結果
    return result.wasSuccessful()

def run_specific_test(test_file):
    """運行特定測試文件"""
    if not test_file.endswith('.py'):
        test_file += '.py'
    
    test_path = os.path.join(os.path.dirname(__file__), test_file)
    
    if not os.path.exists(test_path):
        print(f"錯誤: 找不到測試文件 {test_file}")
        return False
    
    # 運行特定測試
    loader = unittest.TestLoader()
    suite = loader.discover(os.path.dirname(__file__), pattern=test_file)
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    return result.wasSuccessful()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        # 運行特定測試
        test_file = sys.argv[1]
        success = run_specific_test(test_file)
    else:
        # 運行所有測試
        success = run_all_tests()
    
    # 退出碼
    sys.exit(0 if success else 1) 