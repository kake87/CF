from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Table
from sqlalchemy.orm import relationship
from .database import Base

# Ассоциативная таблица для связи "многие ко многим"
association_table = Table(
    'subscriptions', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('course_id', Integer, ForeignKey('courses.id')), extend_existing=True 
)

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_instructor = Column(Boolean, default=False)
    balance = Column(Integer, default=0)
    courses = relationship("Course", secondary=association_table, back_populates="users")

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    instructor_id = Column(Integer, ForeignKey('users.id'))
    course_price = Column(Integer)
    users = relationship("User", secondary=association_table, back_populates="courses")

class Instructor(Base):
    __tablename__ = 'instructors'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    courses = relationship("Course", back_populates="instructor")