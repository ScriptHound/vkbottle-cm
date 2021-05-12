from os import getenv
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine

env_path = Path(__file__).resolve().parent.parent / "config/.env"
load_dotenv(dotenv_path=env_path)

PASSWD = getenv("POSTGRES_PASSWORD")
HOST = getenv("POSTGRES_HOST")
USER = getenv("POSTGRES_USER")
NAME = getenv("POSTGRES_NAME")

engine = create_async_engine(
    f"postgresql+asyncpg://{USER}:{PASSWD}@{HOST}/{NAME}",
    execution_options={"isolation_level": "REPEATABLE_READ"},
    echo=True,
)
