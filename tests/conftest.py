# tests/conftest.py

import pytest
import asyncio
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession
from app.main import app
from app.db.postgres import get_db, SessionLocal


# 🔄 Современное создание event loop
@pytest.fixture(scope="session")
def anyio_backend():
    return "asyncio"


# 🧪 Сессия базы данных
@pytest.fixture(scope="function")
async def async_session() -> AsyncSession:
    async with SessionLocal() as session:
        yield session


# 🧪 Асинхронный HTTP клиент
@pytest.fixture(scope="function")
async def async_client():
    async with AsyncClient(app=app, base_url="http://testserver") as client:
        yield client
