from sqlalchemy import Column, Integer, String, Boolean
from app.db.base import Base  # Base = declarative_base()

class ToDo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    checked = Column(Boolean, default=False)