import logging
from app.core.db import (
    check_connection,
    AsyncSessionLocal
)
from app.core.config import settings
from app.services.user_service import UserService

logger = logging.getLogger(__name__)


async def init_users():
    if not await check_connection():
        logger.error("Cannot connect to database")
        return False

    async with AsyncSessionLocal() as session:
        try:
            service = UserService(session)

            current_count = await service.get_count_users()
            target_count = settings.COUNT_USERS_INIT

            if current_count >= target_count:
                logger.info("Database has enough users, no need to load more")
                return True

            users_to_load = target_count - current_count
            logger.info(f"Need to load {users_to_load} more users")

            loaded = await service.load_users_from_api(users_to_load)
            logger.info(f"Successfully loaded {loaded} users")

            return True

        except Exception as e:
            logger.error(f"Error ensuring minimum users: {e}")
            await session.rollback()
            return False
