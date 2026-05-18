from sqlalchemy import delete
from models import *

with engine.connect() as conn:
    stmt = delete(products).where(products.c.name == "mouse")
    conn.execute(stmt)
    conn.commit()