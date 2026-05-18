from oneToManyModel import *
from sqlalchemy.orm import sessionmaker
from db import *

Session = sessionmaker(bind=engine)
session = Session()

# user1 = User(name = "Pranav")
#
# post1 = Post(title="SqlAlchemy basics")
# post2 = Post(title='Learning ORM ')
#
# user1.posts.append(post1)
# user1.posts.append(post2)
#
# session.add(user1)
# session.commit()
# session.close()

user = session.query(User).filter_by(name="Pranav").first()

for post in user.posts:
    print( post.title)

post = session.query(Post).first()
print(post.user.name)
