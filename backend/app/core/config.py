from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

env_file = os.getenv("ENV_FILE", ".env")
load_dotenv(env_file)


class Settings(BaseSettings):
    PROJECT_NAME: str = "Подари мне"
    VERSION: str = "1.0.0"

    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
