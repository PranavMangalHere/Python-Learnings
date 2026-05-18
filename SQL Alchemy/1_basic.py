from sqlalchemy import create_engine

engine = create_engine("sqlite:///mydatabase.db")

"""What does this mean?
sqlite → database type
:/// → relative path
mydatabase.db → database file
📌 If file doesn’t exist → SQLAlchemy creates it"""

with engine.connect() as connection:
    print("Connected successfully")

