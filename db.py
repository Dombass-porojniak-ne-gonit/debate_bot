import logging

from tortoise import Tortoise

from config import settings

logger = logging.getLogger(__name__)


async def init_db():
    """Initialize database connection"""
    await Tortoise.init(config=settings.tortoise_config)
    logger.info("Database initialized")


async def close_db():
    """Close database connections"""
    await Tortoise.close_connections()
    logger.info("Database closed")
