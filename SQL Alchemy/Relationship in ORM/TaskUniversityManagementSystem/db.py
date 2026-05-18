import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
abs_path = os.path.join(BASE_DIR, "myDb.db")
engine = create_engine(f"sqlite:///{abs_path}")
Base = declarative_base()