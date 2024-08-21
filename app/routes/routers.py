from fastapi import APIRouter
from .users import router as users_router
from .courses import router as course_router


# Основной роутер, куда стекаются остальные роутеры
router = APIRouter()


# Блок подключения остальных роутеров
router.include_router(users_router, prefix='/users', tags=["users"])
router.include_router(course_router, prefix='/courses', tags=["courses"])

