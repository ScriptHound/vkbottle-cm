import os
from pathlib import Path

from dotenv import load_dotenv
from vkbottle import Bot

env_path = Path('.') / 'config/.env'
load_dotenv(dotenv_path=env_path)

bot = Bot(os.environ["ACCESS_TOKEN"])


@bot.on.message()
async def handler(_) -> str:
    return "Да дорогой)"

bot.run_forever()
