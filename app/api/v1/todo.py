from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.todo import ToDo
from app.schemas.todo import ToDoOut
from app.schemas.todo import ToDoCreate

router = APIRouter()

@router.get("/", response_model=list[ToDoOut])
def get_all_todos(db: Session = Depends(get_db)):
    todos = db.query(ToDo).all()
    return todos


@router.post("/", response_model=ToDoOut, status_code=status.HTTP_201_CREATED)
def create_todo(todo: ToDoCreate, db: Session = Depends(get_db)):
    db_todo = ToDo(title=todo.title, checked=todo.checked)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo