import os
from pathlib import Path

from dotenv import load_dotenv
from vkbottle.bot import Message, Bot

from src.admin.repositories.user_repo import UserManager


env_path = Path('.') / 'config/.env'
load_dotenv(dotenv_path=env_path)

bot = Bot(os.environ["ACCESS_TOKEN"])


@bot.on.message(text=[';useradd <username>'])
async def handler(message: Message, username: str) -> str:
    manager = UserManager()
    u = await manager.create_user(name=username)
    return f'{u} username: {username}'

bot.run_forever()
