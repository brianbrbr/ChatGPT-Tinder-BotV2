import os
from dotenv import load_dotenv

load_dotenv()

# OpenAI Configuration
OPENAI_API = os.getenv('OPENAI_API')
OPENAI_MODEL_ENGINE = os.getenv('OPENAI_MODEL_ENGINE', 'gpt-4')

# Tinder Configuration
TINDER_TOKEN = os.getenv('TINDER_TOKEN')

# System Message
SYSTEM_MESSAGE = os.getenv('SYSTEM_MESSAGE', 'You are a helpful assistant.')

# App Configuration
APP_PORT = int(os.getenv('APP_PORT', 8080))
