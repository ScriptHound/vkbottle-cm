import logging

from src.admin.models.user import User
from src.utils.session_handlers import DBAdapter

logger = logging.getLogger()


class UserManager:
    def __init__(self) -> None:
        self._db_adapter = DBAdapter()

    async def create_user(self, **kwargs):
        async with self._db_adapter.get_session() as session:
            u = User(**kwargs)
            session.add(u)
            return u
