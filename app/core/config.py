import os

from dataclasses import dataclass


def csv_env(name: str, default: list[str]) -> list[str]:
    value = os.getenv(name)
    if not value:
        return default
    return [item.strip() for item in value.split(",") if item.strip()]


@dataclass(frozen=True)
class Settings:
    environment: str = os.getenv("ENVIRONMENT", "development").lower()
    database_url: str = os.getenv("DATABASE_URL", "sqlite:///./db/test.db")
    allow_credentials: bool = os.getenv("ALLOW_CREDENTIALS", default="false").lower() == "true"
    roblox_api_secret = os.getenv("ROBLOX_API_SECRET")

    @property
    def is_production(self) -> bool:
        return self.environment == "production"

    @property
    def allowed_hosts(self) -> list[str]:
        default = ["api.yourdomain.com", "yourdomain.com"] if self.is_production else ["localhost", "127.0.0.1"]
        return csv_env("ALLOWED_HOSTS", default)

    @property
    def allowed_origins(self) -> list[str]:
        default = (
            ["https://yourdomain.com", "https://app.yourdomain.com"]
            if self.is_production
            else ["http://localhost", "http://localhost:8000", "http://127.0.0.1", "http://127.0.0.1:8000"]
        )
        return csv_env("ALLOWED_ORIGINS", default)

    def validate(self) -> None:
        if not self.roblox_api_secret:
            raise RuntimeError("ROBLOX_API_SECRET is required")


settings = Settings()
settings.validate()
