# tests/test_migration.py

import pytest
from sqlalchemy import text
from app.db.postgres import get_db


@pytest.mark.asyncio
async def test_users_table_exists():
    """
    Check that the 'users' table exists in the database after migration.
    """
    async for session in get_db():
        result = await session.execute(text("SELECT to_regclass('public.users');"))
        table = result.scalar()
        assert table == 'users', "Table 'users' does not exist in the database"
