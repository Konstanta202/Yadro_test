import pytest
from unittest.mock import AsyncMock, MagicMock, patch
from app.services.user_service import UserService
from app.models.user import User
from app.schemas.user import UserTableResponse, UserDetailResponse


class TestUserService:

    @pytest.fixture
    def service(self, mock_db_session):
        return UserService(mock_db_session)

    def _mock_user(self, sample_user_data):
        mock = MagicMock(spec=User)
        for key, value in sample_user_data.items():
            setattr(mock, key, value)
        return mock

    @pytest.mark.asyncio
    async def test_get_all_users_for_table(self, service, sample_user_data):
        mock_user = self._mock_user(sample_user_data)
        service.repo.get_all = AsyncMock(return_value=[mock_user])
        result = await service.get_all_users_for_table()
        assert len(result) == 1
        assert isinstance(result[0], UserTableResponse)

    @pytest.mark.asyncio
    async def test_get_user_detail_found(self, service, sample_user_data):
        mock_user = self._mock_user(sample_user_data)
        service.repo.get_by_id = AsyncMock(return_value=mock_user)
        result = await service.get_user_detail(1)
        assert result is not None
        assert isinstance(result, UserDetailResponse)

    @pytest.mark.asyncio
    async def test_get_user_detail_not_found(self, service):
        service.repo.get_by_id = AsyncMock(return_value=None)
        result = await service.get_user_detail(999)
        assert result is None

    @pytest.mark.asyncio
    async def test_get_random_user(self, service, sample_user_data):
        mock_user = self._mock_user(sample_user_data)
        service.repo.get_random = AsyncMock(return_value=mock_user)
        result = await service.get_random_user_detail()
        assert result is not None

    @pytest.mark.asyncio
    async def test_fetch_users_from_api(self, service, sample_api_response):
        with patch("httpx.AsyncClient.get") as mock_get:
            mock_response = MagicMock()
            mock_response.json.return_value = sample_api_response
            mock_response.raise_for_status = MagicMock()
            mock_get.return_value = mock_response
            result = await service.fetch_users_from_api(count=1)
            assert len(result) == 1
            assert result[0]["first_name"] == "Иван"

    @pytest.mark.asyncio
    async def test_load_users_from_api(self, service):
        service.repo.bulk_create = AsyncMock()
        service.fetch_users_from_api = AsyncMock(return_value=[
            {"first_name": "Тест", "last_name": "Тестов"}
        ])
        result = await service.load_users_from_api(count=1)
        assert result == 1
