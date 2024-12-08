from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    mail_username: str
    mail_password: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
