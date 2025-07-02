#!/usr/bin/env python3
"""
ChatGPT Tinder Bot 設置腳本
"""

import os
import sys
import subprocess
from pathlib import Path

def run_command(command, description):
    """執行命令並顯示結果"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} 完成")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} 失敗: {e}")
        print(f"錯誤輸出: {e.stderr}")
        return False

def check_python_version():
    """檢查 Python 版本"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ 需要 Python 3.8 或更高版本")
        print(f"當前版本: {version.major}.{version.minor}.{version.micro}")
        return False
    print(f"✅ Python 版本: {version.major}.{version.minor}.{version.micro}")
    return True

def create_env_file():
    """創建 .env 文件"""
    env_file = Path('.env')
    if env_file.exists():
        print("⚠️  .env 文件已存在")
        return True
    
    print("📝 創建 .env 文件...")
    env_content = """# OpenAI Configuration
OPENAI_API=your_openai_api_key_here
OPENAI_MODEL_ENGINE=gpt-4

# Tinder Configuration
TINDER_TOKEN=your_tinder_token_here

# System Message
SYSTEM_MESSAGE=You are a helpful assistant.

# App Configuration
APP_PORT=8080
"""
    
    try:
        with open('.env', 'w', encoding='utf-8') as f:
            f.write(env_content)
        print("✅ .env 文件創建成功")
        print("💡 請編輯 .env 文件，填入你的 API keys")
        return True
    except Exception as e:
        print(f"❌ 創建 .env 文件失敗: {e}")
        return False

def install_dependencies():
    """安裝依賴"""
    return run_command("pip install -r requirements.txt", "安裝 Python 依賴")

def test_installation():
    """測試安裝"""
    print("🧪 測試安裝...")
    
    # 測試導入
    try:
        import openai
        print(f"✅ OpenAI 版本: {openai.__version__}")
    except ImportError:
        print("❌ OpenAI 導入失敗")
        return False
    
    try:
        from opencc import OpenCC
        print("✅ OpenCC 導入成功")
    except ImportError:
        print("❌ OpenCC 導入失敗")
        return False
    
    try:
        import fastapi
        print(f"✅ FastAPI 版本: {fastapi.__version__}")
    except ImportError:
        print("❌ FastAPI 導入失敗")
        return False
    
    return True

def main():
    """主函數"""
    print("🚀 ChatGPT Tinder Bot 設置腳本")
    print("=" * 50)
    
    # 檢查 Python 版本
    if not check_python_version():
        sys.exit(1)
    
    # 創建 .env 文件
    if not create_env_file():
        sys.exit(1)
    
    # 安裝依賴
    if not install_dependencies():
        print("❌ 依賴安裝失敗，請手動執行: pip install -r requirements.txt")
        sys.exit(1)
    
    # 測試安裝
    if not test_installation():
        print("❌ 安裝測試失敗")
        sys.exit(1)
    
    print("\n🎉 設置完成！")
    print("\n📋 下一步:")
    print("1. 編輯 .env 文件，填入你的 API keys")
    print("2. 運行測試: python test_gpt4.py")
    print("3. 啟動應用: python main.py")
    print("\n📖 詳細說明請查看 README.md")

if __name__ == "__main__":
    main() 