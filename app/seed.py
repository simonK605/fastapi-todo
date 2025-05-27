from app.db.session import SessionLocal
from app.models.todo import ToDo
from app.db.base import Base
from app.db.session import engine

Base.metadata.create_all(bind=engine)

db = SessionLocal()

todo1 = ToDo(title="Buy groceries", checked=False)
todo2 = ToDo(title="Study FastAPI", checked=False)

db.add_all([todo1, todo2])
db.commit()

print("Seeded 2 todo items.")