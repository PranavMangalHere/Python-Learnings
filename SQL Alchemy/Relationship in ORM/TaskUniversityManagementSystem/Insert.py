from Model import *
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind = engine)
session = Session()
"""
instructorA = Instructor(name="A")
instructorB = Instructor(name= "B")

student1 = Student(name="Pranav")
student2 = Student(name="Ayush")

course1 = Course(title ="Python")
course2 = Course(title ="Sql")
course3 = Course(title = "AI")

instructorA.courses.append(course1)
instructorA.courses.append(course2)
instructorB.courses.append(course3)

student1.courses.append(course1)
student1.courses.append(course2)
student2.courses.append(course3)

session.add(instructorA)
session.add(instructorB)
session.add(student1)
session.add(student2)
session.commit()
"""

"""students = session.query(Student).all()
for student in students:
    print(student.id, student.name)
    for course in student.courses:
        print("Courses :" , course.id, course.title)
    print("----------")
print("Intructors -------->")
instructors = session.query(Instructor).all()
for instructor in instructors:
    print(instructor.id, instructor.name)
    for course in instructor.courses:
        print("Courses :" , course.id, course.title)
    print("----------")

"""

## Advanced Queries filter vs filter_by

# students = session.query(Student).filter_by(name='Pranav').all()
#
# for student in students:
#     print(student.id, student.name)
#     for course in student.courses:
#         print("Courses :" , course.id, course.title)

# students = session.query(Student).join(Student.courses).filter(
#     Course.title == "Python"
# ).all()
#
# for student in students:
#     print(student.name)

# courses = session.query(Course).join(Course.instructor).filter(
#     Instructor.name == "A"
# ).all()
#
# for course in courses:
#     print(course.id, course.title)

