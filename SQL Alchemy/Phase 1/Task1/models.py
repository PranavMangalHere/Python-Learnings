from sqlalchemy import MetaData, Table, Column, Integer, String, Float
from db_connection import engine

metadata = MetaData()
products = Table(
    "products",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(200), nullable=False),
    Column("price", Float, nullable=False),
    Column("Stock", Integer, default=0)
)
#
# print(metadata.tables.keys())

metadata.create_all(engine)
