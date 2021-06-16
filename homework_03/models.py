"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""

import os
from sqlalchemy import (
    Table,
    MetaData,
    Column,
    Integer,
    String,
    Boolean,
    create_engine,
    ForeignKey,
)
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

SQLALCHEMY_CONN_URI = "postgresql+asyncpg://user:password@localhost/project"

engine = create_async_engine(SQLALCHEMY_CONN_URI, echo=True)

Base = declarative_base()

Session = sessionmaker(bind=engine)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(32), unique=True)
    username = Column(String(32), unique=True)
    email = Column(String(32), unique=True)
    posts = relationship("Post", back_populates="user")


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    title = Column(String(64), nullable=False, default="", server_default="")
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    body = Column(String(32), unique=True)
    user = relationship(User, back_populates="posts")
