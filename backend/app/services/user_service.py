from typing import Optional, List
from sqlalchemy.ext.asyncio import AsyncSession
import httpx
import asyncio
import logging

from app.repositories.user_repository import UserRepository
from app.schemas.user import (
    UserTableResponse,
    UserDetailResponse,
    PaginatedResponse,
)
from app.core.config import settings

logger = logging.getLogger(__name__)


class UserService:

    def __init__(self, session: AsyncSession):
        self.session = session
        self.repo = UserRepository(session)

    async def get_all_users_for_table(self) -> List[UserTableResponse]:
        """Получить всех пользователей для таблицы (только основные поля)"""
        users = await self.repo.get_all()
        return [UserTableResponse.model_validate(user) for user in users]

    async def get_user_for_table(
        self,
        page: int = 1,
        limit: int = 20
    ) -> PaginatedResponse:
        users, total = await self.repo.get_paginated(page, limit)
        total_pages = max(1, (total + limit - 1) // limit)

        items = [UserTableResponse.model_validate(user) for user in users]

        return PaginatedResponse(
            items=items,
            total=total,
            page=page,
            limit=limit,
            total_pages=total_pages,
            has_next=page < total_pages,
            has_prev=page > 1
        )

    async def get_user_detail(self, user_id: int) -> Optional[UserDetailResponse]: # noqa
        user = await self.repo.get_by_id(user_id)
        if not user:
            return None
        return UserDetailResponse.model_validate(user)

    async def get_random_user_detail(self) -> Optional[UserDetailResponse]:

        user = await self.repo.get_random()
        if not user:
            return None
        return UserDetailResponse.model_validate(user)

    async def fetch_users_from_api(self, count: int = 100) -> List[dict]:
        # if count < 1 or count > settings.API_MAX_COUNT:
        #     raise ValueError(
        #         f"Count must be between 1 and {settings.API_MAX_COUNT}"
        #     )

        url = f"{settings.API_BASE_URL}?count={count}&unescaped=false"

        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.get(url)
            response.raise_for_status()
            data = response.json()

            if isinstance(data, dict):
                data = [data]

            users_data = []
            field_mapping = {
                "FirstName": "first_name",
                "LastName": "last_name",
                "FatherName": "father_name",
                "Gender": "gender",
                "GenderCode": "gender_code",
                "DateOfBirth": "date_of_birth",
                "YearsOld": "years_old",
                "Phone": "phone",
                "Email": "email",
                "Login": "login",
                "Password": "password",
                "PasportNum": "passport_num",
                "PasportSerial": "passport_serial",
                "PasportNumber": "passport_number",
                "PasportCode": "passport_code",
                "PasportOtd": "passport_issued",
                "PasportDate": "passport_date",
                "inn_fiz": "inn_fiz",
                "inn_ur": "inn_ur",
                "snils": "snils",
                "oms": "oms",
                "ogrn": "ogrn",
                "kpp": "kpp",
                "Address": "address",
                "AddressReg": "address_reg",
                "Country": "country",
                "Region": "region",
                "City": "city",
                "Street": "street",
                "House": "house",
                "Apartment": "apartment",
                "bankBIK": "bank_bik",
                "bankCorr": "bank_corr",
                "bankINN": "bank_inn",
                "bankKPP": "bank_kpp",
                "bankNum": "bank_num",
                "bankClient": "bank_client",
                "bankCard": "bank_card",
                "bankDate": "bank_date",
                "bankCVC": "bank_cvc",
                "EduSpecialty": "edu_specialty",
                "EduProgram": "edu_program",
                "EduName": "edu_name",
                "EduDocNum": "edu_doc_num",
                "EduRegNumber": "edu_reg_number",
                "EduYear": "edu_year",
                "CarBrand": "car_brand",
                "CarModel": "car_model",
                "CarYear": "car_year",
                "CarColor": "car_color",
                "CarNumber": "car_number",
                "CarVIN": "car_vin",
                "CarSTS": "car_sts",
                "CarSTSDate": "car_sts_date",
                "CarPTS": "car_pts",
                "CarPTSDate": "car_pts_date",
            }

            for item in data:
                user_dict = {
                    db_field: item.get(api_field)
                    for api_field, db_field in field_mapping.items()
                }
                users_data.append(user_dict)

            logger.info(f"Fetched {len(users_data)} users from API")
            return users_data


    async def load_users_from_api(self, count: int) -> int:

        total_loaded = 0
        
        while total_loaded < count:
            remaining = count - total_loaded
            batch_size = min(settings.API_LIMIT, remaining)
            
            try:
                users_data = await self.fetch_users_from_api(batch_size)
                if users_data:
                    await self.repo.bulk_create(users_data)
                    total_loaded += len(users_data)
                    logger.info(f"Loaded {len(users_data)} users (total: {total_loaded}/{count})")
                
                # Ждем 1 секунду между запросами (ограничение API)
                if total_loaded < count:
                    await asyncio.sleep(1)
                    
            except Exception as e:
                logger.error(f"Error loading batch: {e}")
                continue
        
        await self.session.commit()
        logger.info(f"Successfully loaded {total_loaded} users")
        return total_loaded



    async def load_initial_data(self, count: int = 1000):
        existing_count = await self.repo.count()

        if existing_count > 0:
            logger.info(f"Database has {existing_count} users, skip loading")
            return

        logger.info(f"Loading initial {count} users...")
        await self.load_users_from_api(count)
