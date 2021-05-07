from dotenv import load_dotenv
from pathlib import Path
from os import getenv
import sqlalchemy

env_path = Path(__file__).resolve().parent.parent / 'config/.env'
load_dotenv(dotenv_path=env_path)

PASSWD = getenv('POSTGRES_PASSWORD')
HOST = getenv('POSTGRES_HOST')
USER = getenv('POSTGRES_USER')
NAME = getenv('POSTGRES_NAME')

engine = sqlalchemy.create_engine(
    f'postgresql://{USER}:{PASSWD}@{HOST}/{NAME}',
    execution_options={
        "isolation_level": "REPEATABLE_READ"
    }
)
