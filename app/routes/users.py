from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas, models
from ..database import get_db

# Создаем маршрутизатор для пользователей
router = APIRouter()

@router.post("/", response_model=schemas.UserResponse, description="User create function")
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)

@router.get("/{user_id}", response_model=schemas.UserResponse, description="User read function")
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.post("/{user_id}/balance", response_model=schemas.UserResponse, description="User balance change function")
def top_up_balance(user_id: int, balance_top_up: schemas.BalanceTopUp, db: Session = Depends(get_db)):
    user = crud.top_up_balance(db, user_id, balance_top_up.amount)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/{user_id}/subscribe", response_model=schemas.UserResponse, description="Course subscribe function")
def subscribe_to_course(user_id: int, subscription: schemas.CourseSubscription, db: Session = Depends(get_db)):
    try:
        user = crud.subscribe_to_course(db, user_id, subscription.course_id)
        if user is None:
            raise HTTPException(status_code=404, detail="User or Course not found")
        return user
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))