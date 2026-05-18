# app/schemas/user.py
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, List


class UserBase(BaseModel):
    first_name: str
    last_name: str
    father_name: Optional[str] = None
    gender: Optional[str] = None
    date_of_birth: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    address: Optional[str] = None


class UserTableResponse(UserBase):
    id: int
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class UserDetailResponse(BaseModel):
    id: int

    first_name: str
    last_name: str
    father_name: Optional[str] = None
    gender: Optional[str] = None
    gender_code: Optional[str] = None
    date_of_birth: Optional[str] = None
    years_old: Optional[int] = None

    phone: Optional[str] = None
    email: Optional[str] = None
    login: Optional[str] = None

    passport_num: Optional[str] = None
    passport_issued: Optional[str] = None
    passport_date: Optional[str] = None

    inn_fiz: Optional[str] = None
    snils: Optional[str] = None
    oms: Optional[int] = None

    address: Optional[str] = None
    country: Optional[str] = None
    region: Optional[str] = None
    city: Optional[str] = None
    street: Optional[str] = None
    house: Optional[int] = None
    apartment: Optional[int] = None

    bank_card: Optional[str] = None
    bank_client: Optional[str] = None

    edu_specialty: Optional[str] = None
    edu_name: Optional[str] = None
    edu_year: Optional[int] = None

    car_brand: Optional[str] = None
    car_model: Optional[str] = None
    car_year: Optional[int] = None
    car_number: Optional[str] = None

    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class PaginatedResponse(BaseModel):
    items: List[UserTableResponse]
    total: int
    page: int
    limit: int
    total_pages: int
    has_next: bool
    has_prev: bool


class LoadUsersRequest(BaseModel):
    count: int = Field(
        ...,
        ge=1,
        le=100,
        description="Количество пользователей для загрузки (1-100)"
    )
