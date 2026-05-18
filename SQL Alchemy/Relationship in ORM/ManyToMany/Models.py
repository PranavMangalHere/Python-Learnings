from sqlalchemy import Column, Integer, String
from db import engine , Base
from AssociateTable import student_course
from sqlalchemy.orm import relationship


class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    name = Column(String)

    courses = relationship("Course", secondary=student_course, back_populates='students')

class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    students = relationship("Student", secondary= student_course, back_populates='courses')

Base.metadata.create_all(engine)