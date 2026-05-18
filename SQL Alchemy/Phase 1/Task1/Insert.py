from sqlalchemy import insert
from models import engine, products
with engine.begin() as conn:
    conn.execute(
        insert(products),
        [
            {"name" : "Laptop", "price" : 50000, "Stock" : 10},
            {"name" : "mouse", "price" : 500, "Stock" : 100},
            {"name" : "Keyboard", "price" : 1000, "Stock" : 50},
            {"name" : "Monitor", "price" : 3000, "Stock" : 20}
        ]
    )