from pydantic import BaseModel

class ToDoBase(BaseModel):
    title: str

class ToDoCreate(ToDoBase):
    checked: bool = False

class ToDoOut(ToDoBase):
    id: int
    checked: bool

    class Config:
        orm_mode = True