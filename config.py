from typing import Any
from urllib.parse import urlparse

from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    model_config: dict[str, str] = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
        "extra": "ignore",
    }

    # Bot
    bot_token: str = Field(..., description="Telegram Bot API token")
    devel_chat_id: str | None = Field(
        None, description="Telegram chat ID for development logs (optional)"
    )

    # Database
    database_url: str = Field(..., description="PostgreSQL connection URL")

    @property
    def tortoise_config(self) -> dict[str, Any]:
        """Generate Tortoise ORM configuration from DATABASE_URL."""
        parsed = urlparse(self.database_url)

        return {
            "connections": {
                "default": {
                    "engine": "tortoise.backends.asyncpg",
                    "credentials": {
                        "host": parsed.hostname or "localhost",
                        "port": parsed.port or 5432,
                        "user": parsed.username,
                        "password": parsed.password,
                        "database": parsed.path.lstrip("/"),
                    },
                }
            },
            "apps": {
                "models": {
                    "models": ["bot.models", "aerich.models"],
                    "default_connection": "default",
                }
            },
            "use_tz": True,
            "timezone": "UTC",
        }


settings = Settings()  # pyright: ignore[reportCallIssue]

# For Aerich migrations
TORTOISE_CONFIG: dict[str, Any] = settings.tortoise_config
