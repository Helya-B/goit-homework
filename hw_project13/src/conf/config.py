from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    jwt_secret_key: str
    mail_username: str
    mail_password: str
    cloudinary_name: str
    cloudinary_api_key: str
    cloudinary_api_secret: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
