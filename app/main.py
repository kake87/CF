from fastapi import FastAPI
from app.routes.routers import router


app = FastAPI()

# Подключаем маршруты
app.include_router(router)

@app.get("/")
def read_root():
    return "Hello:world"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)