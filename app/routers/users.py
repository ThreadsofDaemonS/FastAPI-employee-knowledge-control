# app/routers/users.py

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.services.user import UserService
from app.schemas.user import (
    SignUpRequest,
    UserDetailResponse,
    UsersListResponse,
    UserUpdateRequest,
)
from app.db.postgres import get_db

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/", response_model=UsersListResponse)
async def get_users(limit: int = 10, offset: int = 0, session: AsyncSession = Depends(get_db)):
    users = await UserService.get_all(session, limit, offset)
    return {"users": users}

@router.get("/{user_id}", response_model=UserDetailResponse)
async def get_user_by_id(user_id: int, session: AsyncSession = Depends(get_db)):
    return await UserService.get_by_id(session, user_id)

@router.post("/", response_model=UserDetailResponse, status_code=status.HTTP_201_CREATED)
async def create_user(user_data: SignUpRequest, session: AsyncSession = Depends(get_db)):
    return await UserService.create(session, user_data)

@router.put("/{user_id}", response_model=UserDetailResponse)
async def update_user(user_id: int, update_data: UserUpdateRequest, session: AsyncSession = Depends(get_db)):
    return await UserService.update(session, user_id, update_data)

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int, session: AsyncSession = Depends(get_db)):
    await UserService.delete(session, user_id)
    return None
