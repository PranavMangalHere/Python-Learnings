from sqlalchemy import update, select
from models import *

with engine.connect() as conn:
    stmt = (
        update(products)
        .where(products.c.name == 'Keyboard')
        .values(price = 1200)
    )
    conn.execute(stmt)
    conn.commit()

with engine.connect() as conn:
    stmt = select(products)
    result = conn.execute(stmt)

    for row in result:
        print(row)