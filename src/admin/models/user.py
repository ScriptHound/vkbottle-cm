from sqlalchemy import Boolean, Column, Date, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from src.admin.models.base import Base


class User(Base):
    __tablename__ = "auth_user"
    id = Column(Integer, primary_key=True)
    vk_id = Column(String)
    name = Column(Text)
    surname = Column(Text)
    is_admin = Column(Boolean, default=False)
    is_whitelisted = Column(Boolean, default=False)
    join_date = Column(Date)

    conversation_id = Column(Integer, ForeignKey("auth_conversation.id"))


class Conversation(Base):
    __tablename__ = "auth_conversation"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    participants_number = Column(Integer)

    users = relationship("User")
