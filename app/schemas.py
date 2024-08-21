from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional
from datetime import date


# Базовая схема пользователя
class UserBase(BaseModel): 
    email: EmailStr
    is_active: bool = True
    is_instructor: bool = False
    city: Optional[str] = None


# Схема создания пользователя (регистрация)
class UserCreate(UserBase):
    password: str
    phone: Optional[str] = Field(None, pattern=r"^\+?[1-9]\d{1,14}$")  # Поле для номера телефона


# Схема отображения пользователя (при ответе на запрос)
class UserResponse(UserBase):
    id: int

    class Config:
        orm_mode = True


# Схема преподавателя
class InstructorCreate(BaseModel):
    bio: Optional[str] = None
    qualifications: List[str] = []
    rating: Optional[float] = 0.0
    experience_years: Optional[int] = 0


# Схема курса
class CourseBase(BaseModel):
    title: str
    description: Optional[str] = None
    price: float
    start_date: date
    end_date: Optional[date] = None


class CourseCreate(CourseBase):
    instructor_id: int


class CourseResponse(CourseBase):
    id: int
    instructor_id: int

    class Config:
        orm_mode = True


# Схема подписки на курс
class SubscriptionBase(BaseModel):
    user_id: int
    course_id: int
    is_active: bool = True


class SubscriptionCreate(SubscriptionBase):
    pass


class SubscriptionResponse(SubscriptionBase):
    id: int
    subscription_date: date

    class Config:
        orm_mode = True


# Схема для отображения всех курсов преподавателя
class InstructorWithCourses(InstructorCreate):
    id: int
    user_id: int
    courses: List[CourseResponse] = []

    class Config:
        orm_mode = True

class BalanceTopUp(BaseModel):
    amount:int


class CourseSubscription(BaseModel):
    course_id:int

    class Config:
        orm_mode = True

