from pydantic_settings import BaseSettings  # ✅ Correct for Pydantic v2

class Settings(BaseSettings):
    DATABASE_URL: str = "mysql+pymysql://root:111111@localhost/fast_api_todo"

    class Config:
        env_file = ".env"

settings = Settings()
