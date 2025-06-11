from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

# Load .env file manually
load_dotenv()

class Settings(BaseSettings):
    SECRET_KEY: str
    ALGORITHM: str
    
    class Config:
        env_file = ".env"  # still works if run locally without docker

settings = Settings()
