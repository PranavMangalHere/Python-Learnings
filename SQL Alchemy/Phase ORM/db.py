from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, 'orm_database.db')

engine = create_engine(f"sqlite:///{db_path}")

Base = declarative_base()