from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_USER: str = "postgres"
    DB_PASSWORD: str = "postgres"
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432
    DB_NAME: str = "nexus_db"
    SECRET_KEY: str = "super_secret_nexus_key_2026"

    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()