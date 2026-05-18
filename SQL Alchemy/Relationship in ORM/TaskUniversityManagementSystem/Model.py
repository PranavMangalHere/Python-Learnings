from db import engine, Base
from sqlalchemy import Integer, Column, String, ForeignKey, Table
from sqlalchemy.orm import relationship

student_course = Table(
    "student_course",
    Base.metadata,
    Column("student_id", ForeignKey("students.id"), primary_key=True),
    Column("course_id", ForeignKey("courses.id"), primary_key=True)
)


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    courses = relationship("Course", secondary=student_course, back_populates='students')


class Instructor(Base):
    __tablename__ = "instructors"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    dept = Column(String)

    courses = relationship('Course', back_populates='instructor')

class Course(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    instructor_id = Column(Integer, ForeignKey("instructors.id"))

    instructor = relationship("Instructor", back_populates="courses")

    students = relationship("Student", secondary=student_course, back_populates='courses')

Base.metadata.create_all(engine)
