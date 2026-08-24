from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache


class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./test.db"
    MONGODB_URI: str = ""  
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )


@lru_cache()
def get_settings():
    return Settings()


settings = get_settings()