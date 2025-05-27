from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

DB_USER = "root"
DB_PASSWORD = "111111"
DB_HOST = "localhost"
DB_PORT = "3306"
DB_NAME = "fast_api_todo"

SQLALCHEMY_DATABASE_URL = (
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()