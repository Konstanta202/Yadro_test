import pytest
from unittest.mock import AsyncMock, patch # noqa
from app.services.user_service import UserService


@pytest.mark.integration
class TestUsersAPI:

    @pytest.mark.asyncio
    async def test_get_users_empty(self, client):
        response = await client.get("/api/users")
        assert response.status_code == 200
        assert response.json() == []

    @pytest.mark.asyncio
    async def test_get_user_not_found(self, client):
        response = await client.get("/api/users/99999")
        assert response.status_code == 404

    @pytest.mark.asyncio
    async def test_random_user_empty(self, client):
        response = await client.get("/api/users/random")
        assert response.status_code == 404

    @pytest.mark.asyncio
    async def test_load_users(self, client, db_session):
        from app.services.user_service import UserService

        with patch.object(UserService, "fetch_users_from_api") as mock_fetch:
            mock_fetch.return_value = [
                {
                    "first_name": "Тест",
                    "last_name": "Тестов",
                    "phone": "+7 (999) 000-00-00",
                    "email": "test@test.ru",
                    "address": "г. Москва"
                }
            ]

            response = await client.post("/api/users/load?count=1")
            assert response.status_code == 201
            assert response.json()["count"] == 1

        response = await client.get("/api/users")
        assert len(response.json()) == 1

    @pytest.mark.asyncio
    async def test_get_user_by_id(self, client, db_session):
        from app.services.user_service import UserService

        service = UserService(db_session)
        user = await service.repo.create({
            "first_name": "Анна",
            "last_name": "Петрова",
            "phone": "+7 (999) 111-11-11",
            "email": "anna@test.ru",
            "address": "г. Москва",
        })
        await db_session.commit()

        response = await client.get(f"/api/users/{user.id}")
        assert response.status_code == 200
        assert response.json()["first_name"] == "Анна"

    @pytest.mark.asyncio
    async def test_get_random_user(self, client, db_session):

        service = UserService(db_session)
        await service.repo.create({
            "first_name": "Петр",
            "last_name": "Сидоров",
        })
        await db_session.commit()

        response = await client.get("/api/users/random")
        assert response.status_code == 200
        assert response.json()["first_name"] == "Петр"
