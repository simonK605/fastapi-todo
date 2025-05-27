from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.todo import ToDo
from app.schemas.todo import ToDoOut

router = APIRouter()

@router.get("/", response_model=list[ToDoOut])
def get_all_todos(db: Session = Depends(get_db)):
    todos = db.query(ToDo).all()
    return todos
