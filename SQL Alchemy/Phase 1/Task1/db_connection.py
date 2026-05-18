"""from sqlalchemy import create_engine
url = "sqlite:///C:\\Users\PranavMangal\Desktop\sqlalchemy_db\learning_sqlalchemy.db"

engine = create_engine(url)

with engine.connect() as conn:
    print(conn)"""

from sqlalchemy import (
create_engine,
MetaData,
Table,
Column,
Integer,
String,
Float
)
# engine = create_engine("sqlite:///learning-sqlalchemy.db")
#
# metadata = MetaData()
#
# users = Table(
#     "users",             # Table name
#     metadata,           # Metadata container
#     Column("id", Integer, primary_key=True),
#     Column("name", String(100), nullable=False),
#     Column("age", Integer)
# )
#
# # 4. Create table in database
# metadata.create_all(engine)
#
# print("Users table created successfully!")


## TASK 2
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "learning_sqlalchemy.db")

engine = create_engine(f"sqlite:///{db_path}")
# metadata = MetaData()
# products = Table(
#     "products",
#     metadata,
#     Column("id", Integer, primary_key=True),
#     Column("name", String(200), nullable=False),
#     Column("price", Float, nullable=False),
#     Column("Stock", Integer, default=0)
# )
#
# print(metadata.tables.keys())
#
# metadata.create_all(engine)




