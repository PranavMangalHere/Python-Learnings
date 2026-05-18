from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db import engine, Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    posts = relationship('Post', back_populates='user')

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key = True)
    title = Column(String(100))
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship('User', back_populates='posts')

Base.metadata.create_all(engine)