from sqlalchemy.orm import sessionmaker
from unicodedata import category, name

from db import engine
from model2_task import Category

Session = sessionmaker(bind= engine)
session = Session()

# # Create object
# category1 = Category(name='Electronics')
# category2 = Category(name = 'Clothing')
#
# # add to session
# session.add(category1)
# session.add(category2)

# c1 = Category(name="C1")
# c2 = Category(name="C2")
# c3 = Category(name="C3")
#
# session.add_all([c1,c2,c3])
# OR
# session.add_all([category1, category2])

# session.commit()

# print("Categories inserted successfully")

# categories = session.query(Category).all()
# for category in categories:
#     print(category.name)
#
# cat = session.query(Category).filter_by(name = 'C1').delete()
# session.commit()
#
# categories = session.query(Category).all()
# for category in categories:
#     print(category.name)