import sys
from pathlib import Path
import pytest
from unittest.mock import AsyncMock, MagicMock
from datetime import datetime
from typing import Any, Dict
import asyncio
from sqlalchemy.ext.asyncio import AsyncSession


root_dir = Path(__file__).parent.parent
sys.path.insert(0, str(root_dir))


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture
def mock_db_session():
    session = AsyncMock(spec=AsyncSession)
    session.execute = AsyncMock()
    session.commit = AsyncMock()
    session.rollback = AsyncMock()
    session.add = MagicMock()
    session.delete = MagicMock()
    session.refresh = AsyncMock()
    session.flush = AsyncMock()
    return session


@pytest.fixture
def sample_user_data() -> Dict[str, Any]:
    return {
        "id": 1,
        "first_name": "Иван",
        "last_name": "Иванов",
        "father_name": "Иванович",
        "gender": "Мужчина",
        "gender_code": "man",
        "date_of_birth": "01.01.1990",
        "years_old": 35,
        "phone": "+7 (999) 123-45-67",
        "email": "ivan@example.com",
        "login": "ivan",
        "password": "pass123",
        "address": "Россия, г. Москва",
        "address_reg": None,
        "country": "Россия",
        "region": "Московская область",
        "city": "г. Москва",
        "street": "ул. Пушкина",
        "house": 1,
        "apartment": 10,
        "passport_num": "1234 567890",
        "passport_serial": "1234",
        "passport_number": 567890,
        "passport_code": "770-001",
        "passport_issued": "УФМС России",
        "passport_date": "01.01.2015",
        "inn_fiz": "123456789012",
        "inn_ur": None,
        "snils": "123-456-789 01",
        "oms": 1234567890123456,
        "ogrn": None,
        "kpp": None,
        "bank_bik": None,
        "bank_corr": None,
        "bank_inn": None,
        "bank_kpp": None,
        "bank_num": None,
        "bank_client": None,
        "bank_card": None,
        "bank_date": None,
        "bank_cvc": None,
        "edu_specialty": None,
        "edu_program": None,
        "edu_name": None,
        "edu_doc_num": None,
        "edu_reg_number": None,
        "edu_year": None,
        "car_brand": None,
        "car_model": None,
        "car_year": None,
        "car_color": None,
        "car_number": None,
        "car_vin": None,
        "car_sts": None,
        "car_sts_date": None,
        "car_pts": None,
        "car_pts_date": None,
        "created_at": datetime.now(),
        "updated_at": datetime.now(),
    }


@pytest.fixture
def sample_api_response():
    return [
        {
            "FirstName": "Иван",
            "LastName": "Иванов",
            "Gender": "Мужчина",
            "Phone": "+7 (999) 123-45-67",
            "Email": "ivan@example.com",
            "Address": "Россия, г. Москва",
        }
    ]
