from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas, models
from ..database import get_db
from typing import List

# Создаем маршрутизатор для курсов
router = APIRouter()

@router.post("/", response_model=schemas.CourseResponse, description="Course create function")
def create_course(course: schemas.CourseCreate, db: Session = Depends(get_db)):
    return crud.create_course(db, course)

@router.get("/", response_model=List[schemas.CourseResponse], description="Course read function")
# int, limit - пагинаторы выдач
def read_courses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    courses = crud.get_courses(db, skip=skip, limit=limit)
    return courses

@router.get("/{course_id}", response_model=schemas.CourseResponse, description="Single course read function")
def read_course(course_id: int, db: Session = Depends(get_db)):
    course = crud.get_course(db, course_id=course_id)
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return course

@router.delete("/{course_id}", response_model=schemas.CourseResponse, description="Delete course function")
def delete_course(course_id: int, db: Session = Depends(get_db)):
    course = crud.delete_course(db, course_id=course_id)
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return course