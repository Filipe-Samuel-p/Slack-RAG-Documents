from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    github_url: str = "GITHUB_URL"
    github_token: str = "GITHUB_TOKEN"
    

def get_settings() -> Settings:
    return Settings()