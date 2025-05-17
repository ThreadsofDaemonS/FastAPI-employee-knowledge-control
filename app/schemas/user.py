# app/schemas/user.py

from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional, List
from datetime import datetime


# 🔹 Общая базовая схема
class UserBase(BaseModel):
    email: EmailStr
    username: str
    full_name: Optional[str] = None


# 🔐 Схема создания пользователя
class SignUpRequest(UserBase):
    password: str


# 🔑 Схема для входа (если будет логин)
class SignInRequest(BaseModel):
    email: EmailStr
    password: str


# ✏️ Обновление пользователя
class UserUpdateRequest(BaseModel):
    full_name: Optional[str] = None
    password: Optional[str] = None


# 📄 Ответ: один пользователь
class UserDetailResponse(UserBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)  # ✅ Актуальный формат


# 📋 Ответ: список пользователей
class UsersListResponse(BaseModel):
    users: List[UserDetailResponse]
