from fastapi import FastAPI
from app.api.v1 import todo

app = FastAPI(title="ToDo API")

@app.get("/")
def read_root():
    return {"message": "Welcome to the ToDo API"}

app.include_router(todo.router, prefix="/api/v1/todos", tags=["todos"])