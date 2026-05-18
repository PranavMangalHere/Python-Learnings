from sqlalchemy import Integer, Column, String
from db import engine, Base

class Category(Base):
    __tablename__ = "category"
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable = False)

Base.metadata.create_all(engine)

