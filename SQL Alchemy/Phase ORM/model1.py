from sqlalchemy import Integer, String, Float, Column
from db import engine, Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable = False)
    price = Column(Float, nullable = False)
    stock = Column(Integer, default = 0)

Base.metadata.create_all(engine)
print("ORm Table is created")