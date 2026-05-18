
from sqlalchemy import select
from models import *

with engine.connect() as conn:
    stmt = select(products)
    result = conn.execute(stmt)

    for row in result:
        print(row.name)