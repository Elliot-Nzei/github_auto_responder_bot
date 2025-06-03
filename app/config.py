from pydantic import BaseSettings

class Settings(BaseSettings):
    github_token: str
    webhook_secret: str

    class Config:
        env_file = ".env"

settings = Settings()
