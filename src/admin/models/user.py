from sqlalchemy import Column, Integer, String, Boolean, Date, Text

from src.admin.models.base import Base


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    vk_id = Column(String)
    name = Column(Text)
    surname = Column(Text)
    is_admin = Column(Boolean, default=False)
    is_whitelisted = Column(Boolean, default=False)
    join_date = Column(Date)
