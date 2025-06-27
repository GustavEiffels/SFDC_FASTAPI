from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROJECT_NAME: str = "FastApi For SFDC"
    API_STR: str = "/test"
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()