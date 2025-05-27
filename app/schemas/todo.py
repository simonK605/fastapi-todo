from pydantic import BaseModel

class ToDoBase(BaseModel):
    title: str

class ToDoOut(ToDoBase):
    id: int
    checked: bool

    class Config:
        orm_mode = True