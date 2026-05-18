from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_db
from app.services.user_service import UserService
from app.schemas.user import (
    UserTableResponse,
    UserDetailResponse,
)
from typing import List

router = APIRouter(tags=["users"])


@router.get("/users", response_model=List[UserTableResponse])
async def get_users(
    db: AsyncSession = Depends(get_db)
):
    service = UserService(db)
    return await service.get_all_users_for_table()


@router.get("/users/random", response_model=UserDetailResponse)
async def get_random_user(
    db: AsyncSession = Depends(get_db)
):
    service = UserService(db)
    user = await service.get_random_user_detail()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There are no users in the database"
        )

    return user


@router.get("/users/{user_id}", response_model=UserDetailResponse)
async def get_user(
    user_id: int,
    db: AsyncSession = Depends(get_db)
):
    service = UserService(db)
    user = await service.get_user_detail(user_id)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {user_id} not found"
        )

    return user


@router.post("/users/load", status_code=status.HTTP_201_CREATED)
async def load_users(
    count: int = Query(..., ge=1),
    db: AsyncSession = Depends(get_db)
):
    service = UserService(db)
    loaded_count = await service.load_users_from_api(count)

    return {
        "message": f"Successfully uploaded users: {loaded_count}",
        "count": loaded_count
    }
