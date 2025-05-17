# tests/test_users.py
import pytest
from httpx import AsyncClient

BASE_URL = "http://app:8000"


@pytest.mark.asyncio
class TestUsers:
    user_id = None

    @pytest.mark.order(1)
    async def test_create_user(self):
        async with AsyncClient(base_url=BASE_URL) as ac:
            payload = {
                "email": "test@example.com",
                "username": "testuser",
                "password": "testpass123",
                "full_name": "Test User"
            }
            response = await ac.post("/users/", json=payload)
            assert response.status_code == 201
            data = response.json()
            assert data["email"] == payload["email"]
            assert data["username"] == payload["username"]
            TestUsers.user_id = data["id"]

    @pytest.mark.order(2)
    async def test_get_user_by_id(self):
        async with AsyncClient(base_url=BASE_URL) as ac:
            response = await ac.get(f"/users/{self.user_id}")
            assert response.status_code == 200
            assert response.json()["id"] == self.user_id

    @pytest.mark.order(3)
    async def test_get_all_users(self):
        async with AsyncClient(base_url=BASE_URL) as ac:
            response = await ac.get("/users/")
            assert response.status_code == 200
            assert isinstance(response.json()["users"], list)

    @pytest.mark.order(4)
    async def test_update_user(self):
        async with AsyncClient(base_url=BASE_URL) as ac:
            payload = {"full_name": "Updated Name"}
            response = await ac.put(f"/users/{self.user_id}", json=payload)
            assert response.status_code == 200
            assert response.json()["full_name"] == "Updated Name"

    @pytest.mark.order(5)
    async def test_delete_user(self):
        async with AsyncClient(base_url=BASE_URL) as ac:
            response = await ac.delete(f"/users/{self.user_id}")
            assert response.status_code == 204
