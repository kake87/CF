from sqlalchemy.orm import Session
from . import models, schemas

# Пользователи
def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(email=user.email, hashed_password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

# Преподаватели
def create_instructor(db: Session, instructor: schemas.InstructorCreate, user_id: int):
    db_instructor = models.Instructor(**instructor.dict(), user_id=user_id)
    db.add(db_instructor)
    db.commit()
    db.refresh(db_instructor)
    return db_instructor

# Курсы
def create_course(db: Session, course: schemas.CourseCreate):
    db_course = models.Course(**course.dict())
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

def get_courses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Course).offset(skip).limit(limit).all()

# Подписки
def create_subscription(db: Session, subscription: schemas.SubscriptionCreate):
    db_subscription = models.Subscription(**subscription.dict())
    db.add(db_subscription)
    db.commit()
    db.refresh(db_subscription)
    return db_subscription

def get_subscriptions(db: Session, user_id: int):
    return db.query(models.Subscription).filter(models.Subscription.user_id == user_id).all()

# Пополнение баланса пользователя
def top_up_balance(db: Session, user_id: int, amount: int):
    db_user = db.query(models.User).filter(models.User.id==user_id).first()
    if db_user:
        db_user_balance += amount
        db.commit()
        db.refresh(db_user)
        return db_user
    return None

# Покупка подписки на курс
def subscribe_to_course(db: Session, user_id: int, course_id: int):
    db_user = db.query(models.User).filter(models.User.id==user_id).first()
    db_course = db.query(models.Course).filter(models.Course.id == course_id).first()

    if db_user and db_course:
        if db_user.balance >= db_course.course_price:
            db_user.balance -= db_course.course_price
            db_user.courses.append(db_course) # Здесь может быть ошибка, потому что мы не определяем явно тип db_user.courses как массив
            db.commit()
            db.refresh(db_user)
            return db_user
    else:
        raise ValueError("Недостаточно средств на балансе")
    return None

