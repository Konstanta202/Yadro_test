import pytest
from unittest.mock import AsyncMock, MagicMock, patch
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException
from app.core.db import get_db, check_connection


class TestGetDB:

    @pytest.mark.asyncio
    async def test_get_db_success(self):
        with patch("app.core.db.AsyncSessionLocal") as mock_session_local:
            mock_session = AsyncMock()
            mock_session.__aenter__.return_value = mock_session
            mock_session_local.return_value = mock_session

            async for session in get_db():
                assert session == mock_session
                break

    @pytest.mark.asyncio
    async def test_get_db_sqlalchemy_error(self):
        with patch("app.core.db.AsyncSessionLocal") as mock_session_local:
            mock_session = AsyncMock()
            mock_session.__aenter__.return_value = mock_session
            mock_session.commit = AsyncMock(
                side_effect=SQLAlchemyError("DB error")
            )
            mock_session_local.return_value = mock_session

            with pytest.raises(HTTPException) as exc_info:
                async for _ in get_db():
                    pass

            assert exc_info.value.status_code == 500
            assert "Database error" in str(exc_info.value.detail)


class TestCheckConnection:

    @pytest.mark.asyncio
    async def test_check_connection_success(self):
        with patch("app.core.db.async_engine") as mock_engine:
            mock_conn = AsyncMock()
            mock_result = MagicMock()
            mock_result.scalar.return_value = 1
            mock_conn.execute.return_value = mock_result
            mock_engine.begin.return_value.__aenter__.return_value = mock_conn

            result = await check_connection()
            assert result is True

    @pytest.mark.asyncio
    async def test_check_connection_failure(self):
        with patch("app.core.db.async_engine") as mock_engine:
            mock_engine.begin.side_effect = Exception("Connection failed")

            result = await check_connection()
            assert result is False
