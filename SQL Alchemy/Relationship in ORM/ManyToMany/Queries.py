from sqlalchemy.orm import sessionmaker
from Models import *

Session = sessionmaker(bind=engine)
session = Session()
# student1 = Student(name= "Pranav")
# course1 = Course(name = "Sql")
# course2 = Course(name = "Python")
#
# student1.courses.append(course1)
# student1.courses.append(course2)
#
# session.add(student1)
# session.commit()

students = session.query(Student).all()
for student in students:
    print(student.id, student.name)
    for course in student.courses:
        print("   Course:", course.name)

""" 
🧠 What Is Happening Internally
When you access:
student.courses
SQLAlchemy fires:

SELECT courses.* 
FROM courses
JOIN student_course 
ON courses.id = student_course.course_id
WHERE student_course.student_id = ? 
"""