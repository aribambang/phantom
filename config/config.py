import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY: str = os.environ.get("SECRET_KEY")
    DB_HOST: str = os.environ.get("DB_HOST")
    DB_PORT: str = os.environ.get("DB_PORT")
    DB_NAME: str = os.environ.get("DB_NAME")
    DB_USER: str = os.environ.get("DB_USER")
    DB_PASSWORD: str = os.environ.get("DB_PASSWORD")
    SQLALCHEMY_DATABASE_URI: str = os.getenv('SQLALCHEMY_DATABASE_URI')