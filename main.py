import datetime
import os
from src.chatgpt import ChatGPT, DALLE
from src.models import OpenAIModel
from src.tinder import TinderAPI
from src.dialog import Dialog
from src.logger import logger
from opencc import OpenCC
import config

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from dotenv import load_dotenv
from fastapi import FastAPI
import uvicorn

# 載入環境變數
load_dotenv('.env')

# 檢查必要的環境變數
if not config.OPENAI_API:
    logger.error("❌ OPENAI_API 環境變數未設置！請在 Replit Secrets 中設置 OPENAI_API")
    raise ValueError("OPENAI_API 環境變數未設置")

if not config.TINDER_TOKEN:
    logger.warning("⚠️  TINDER_TOKEN 環境變數未設置，Tinder 功能將無法使用")

# 創建模型實例
try:
    models = OpenAIModel(api_key=config.OPENAI_API, model_engine=config.OPENAI_MODEL_ENGINE)
    logger.info(f"✅ OpenAI 模型初始化成功: {config.OPENAI_MODEL_ENGINE}")
except Exception as e:
    logger.error(f"❌ OpenAI 模型初始化失敗: {e}")
    raise

chatgpt = ChatGPT(models)
dalle = DALLE(models)
dialog = Dialog()
app = FastAPI()
scheduler = AsyncIOScheduler()
cc = OpenCC('s2t')
TINDER_TOKEN = config.TINDER_TOKEN


@scheduler.scheduled_job("cron", minute='*/5', second=0, id='reply_messages')
def reply_messages():
    tinder_api = TinderAPI(TINDER_TOKEN)
    profile = tinder_api.profile()

    user_id = profile.id

    for match in tinder_api.matches(limit=50):
        chatroom = tinder_api.get_messages(match.match_id)
        lastest_message = chatroom.get_lastest_message()
        if lastest_message:
            if lastest_message.from_id == user_id:
                from_user_id = lastest_message.from_id
                to_user_id = lastest_message.to_id
                last_message = 'me'
            else:
                from_user_id = lastest_message.to_id
                to_user_id = lastest_message.from_id
                last_message = 'other'
            sent_date = lastest_message.sent_date
            if last_message == 'other' or (sent_date + datetime.timedelta(days=1)) < datetime.datetime.now():
                content = dialog.generate_input(from_user_id, to_user_id, chatroom.messages[::-1])
                response = chatgpt.get_response(content)
                if response:
                    response = cc.convert(response)
                    if response.startswith('[Sender]'):
                        chatroom.send(response[8:], from_user_id, to_user_id)
                    else:
                        chatroom.send(response, from_user_id, to_user_id)
                logger.info(f'Content: {content}, Reply: {response}')


@app.on_event("startup")
async def startup():
    scheduler.start()


@app.on_event("shutdown")
async def shutdown():
    scheduler.remove_job('reply_messages')


@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run('main:app', host='0.0.0.0', port=config.APP_PORT)
