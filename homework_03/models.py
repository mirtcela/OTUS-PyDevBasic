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
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

engine = create_engine("sqlite:///example-01.db", echo=True)

PG_CONN_URI = os.environ.get("PG_CONN_URI") or "postgresql://postgres:password@localhost/postgres"

Base = declarative_base(bind=engine)
Session = sessionmaker(bind=engine)


class User(Base):
    __tablename__ = "users"

    name = Column(String(32), unique=True)
    username = Column(String(32), unique=True)
    email = Column(String(32), unique=True)

    posts = relationship("Post", back_populates="user")


class Post(Base):
    __tablename__ = "posts"

    user_id = Column(Integer, primary_key=True)
    title = Column(String(64), nullable=False, default="", server_default="")
    body = Column(String(32), unique=True)

    user_id = Column(Integer, ForeignKey(User.id), nullable=False)

    user = relationship(User, back_populates="posts")
