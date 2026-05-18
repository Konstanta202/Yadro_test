import pytest
from unittest.mock import MagicMock
from datetime import datetime # noqa
from app.repositories.user_repository import UserRepository
from app.models.user import User


class TestUserRepository:

    @pytest.fixture
    def repo(self, mock_db_session):
        return UserRepository(mock_db_session)

    def _mock_user(self):
        mock = MagicMock(spec=User)
        mock.id = 1
        mock.first_name = "Иван"
        mock.last_name = "Иванов"
        return mock

    @pytest.mark.asyncio
    async def test_get_by_id_found(self, repo, mock_db_session):
        mock_result = MagicMock()
        mock_result.scalar_one_or_none.return_value = self._mock_user()
        mock_db_session.execute.return_value = mock_result
        result = await repo.get_by_id(1)
        assert result.first_name == "Иван"

    @pytest.mark.asyncio
    async def test_get_by_id_not_found(self, repo, mock_db_session):
        mock_result = MagicMock()
        mock_result.scalar_one_or_none.return_value = None
        mock_db_session.execute.return_value = mock_result
        result = await repo.get_by_id(999)
        assert result is None

    @pytest.mark.asyncio
    async def test_get_random(self, repo, mock_db_session):
        mock_result = MagicMock()
        mock_result.scalar_one_or_none.return_value = self._mock_user()
        mock_db_session.execute.return_value = mock_result
        result = await repo.get_random()
        assert result is not None

    @pytest.mark.asyncio
    async def test_count(self, repo, mock_db_session):
        mock_result = MagicMock()
        mock_result.scalar.return_value = 100
        mock_db_session.execute.return_value = mock_result
        result = await repo.count()
        assert result == 100

    @pytest.mark.asyncio
    async def test_create(self, repo, mock_db_session):
        user_data = {"first_name": "Петр", "last_name": "Петров"}
        result = await repo.create(user_data)
        mock_db_session.add.assert_called_once()
        assert result.first_name == "Петр"
