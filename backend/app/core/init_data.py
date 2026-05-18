import logging
from app.core.db import (
    check_connection,
    create_missing_tables,
    AsyncSessionLocal
)
from app.services.user_service import UserService

logger = logging.getLogger(__name__)


async def init_database():

    if not await check_connection():
        logger.error("Cannot connect to database")
        return False

    await create_missing_tables()

    async with AsyncSessionLocal() as session:
        try:
            service = UserService(session)
            await service.load_initial_data(1000)
            logger.info("Database initialization completed successfully")
            return True
        except Exception as e:
            logger.error(f"Error loading initial data: {e}")
            return False
