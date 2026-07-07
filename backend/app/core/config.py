from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application configuration.
    Values are loaded automatically from the .env file.
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore",
    )

    # -------------------------------------------------
    # Application
    # -------------------------------------------------

    APP_NAME: str = "OptiRoute AI"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True
    ENVIRONMENT: str = "development"

    API_V1_PREFIX: str = "/api/v1"

    # -------------------------------------------------
    # Server
    # -------------------------------------------------

    HOST: str = "0.0.0.0"
    PORT: int = 8000

    # -------------------------------------------------
    # Security
    # -------------------------------------------------

    SECRET_KEY: str = Field(...)

    ALGORITHM: str = "HS256"

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 15

    REFRESH_TOKEN_EXPIRE_DAYS: int = 7

    # -------------------------------------------------
    # Database
    # -------------------------------------------------

    DATABASE_URL: str


    # -------------------------------------------------
    # Redis
    # -------------------------------------------------

    REDIS_URL: str

    # -------------------------------------------------
    # CORS
    # -------------------------------------------------

    ALLOWED_ORIGINS: str = (
        "http://localhost:3000,"
        "http://127.0.0.1:3000,"
        "http://localhost:5173,"
        "http://127.0.0.1:5173,"
        "http://localhost:5174,"
        "http://127.0.0.1:5174,"
        "http://localhost:5175,"
        "https://optirouteai-git-main-gpcsantoshs-projects.vercel.app,"
        "http://127.0.0.1:5175"
    )

    @property
    def cors_origins(self) -> list[str]:
        return [
            origin.strip()
            for origin in self.ALLOWED_ORIGINS.split(",")
            if origin.strip()
        ]

    # -------------------------------------------------
    # Pagination
    # -------------------------------------------------

    DEFAULT_PAGE_SIZE: int = 20

    MAX_PAGE_SIZE: int = 100

    # -------------------------------------------------
    # Logging
    # -------------------------------------------------

    LOG_LEVEL: str = "INFO"

    LOG_FILE: str = "logs/backend.log"

    # -------------------------------------------------
    # Upload
    # -------------------------------------------------

    MAX_UPLOAD_SIZE_MB: int = 20

    # -------------------------------------------------
    # Simulation
    # -------------------------------------------------

    DEFAULT_CITY_NAME: str = "OptiRoute City"

    DEFAULT_SIMULATION_SPEED: int = 1


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()