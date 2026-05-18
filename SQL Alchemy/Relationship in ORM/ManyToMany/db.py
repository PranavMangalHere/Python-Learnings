from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, 'relationshipDb.db')

engine = create_engine(f"sqlite:///relationshipDb.db")
# print(engine)
Base = declarative_base()