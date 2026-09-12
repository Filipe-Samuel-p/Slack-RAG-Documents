from pydantic import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    github_url: str = model_config.env_file_values.get("GITHUB_URL", "")
    github_token: str = model_config.env_file_values.get("GITHUB_TOKEN", "")
    

def get_settings() -> Settings:
    return Settings()