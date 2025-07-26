from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    """
    Configuration settings for the application.
    """
    # Database connection string
    database_url: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/population"
    population_source: str = "wiki"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")
config = Config()
