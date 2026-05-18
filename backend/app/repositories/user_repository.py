from typing import Optional, List, Tuple
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func, desc # noqa
from app.models.user import User


class UserRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_id(self, user_id: int) -> Optional[User]:
        query = select(User).where(User.id == user_id)
        result = await self.session.execute(query)
        return result.scalar_one_or_none()

    async def get_random(self) -> Optional[User]:
        query = select(User).order_by(func.random()).limit(1)
        result = await self.session.execute(query)
        return result.scalar_one_or_none()

    async def get_paginated(
        self,
        page: int = 1,
        limit: int = 20
    ) -> Tuple[List[User], int]:
        count_query = select(func.count(User.id))
        total_result = await self.session.execute(count_query)
        total = total_result.scalar()

        offset = (page - 1) * limit
        query = (
            select(User)
            .order_by(User.id)
            .offset(offset)
            .limit(limit)
        )
        result = await self.session.execute(query)
        users = list(result.scalars().all())

        return users, total

    async def get_all(self) -> List[User]:
        """Получить всех пользователей"""
        query = select(User).order_by(User.id)
        result = await self.session.execute(query)
        return list(result.scalars().all())

    async def create(self, user_data: dict) -> User:
        user = User(**user_data)
        self.session.add(user)
        await self.session.flush()
        await self.session.refresh(user)
        return user

    async def bulk_create(self, users_data: List[dict]) -> List[User]:
        users = [User(**data) for data in users_data]
        self.session.add_all(users)
        await self.session.flush()
        for user in users:
            await self.session.refresh(user)
        return users

    async def count(self) -> int:
        query = select(func.count(User.id))
        result = await self.session.execute(query)
        return result.scalar()

    async def exists(self, user_id: int) -> bool:
        query = select(User).where(User.id == user_id)
        result = await self.session.execute(query)
        return result.scalar_one_or_none() is not None
