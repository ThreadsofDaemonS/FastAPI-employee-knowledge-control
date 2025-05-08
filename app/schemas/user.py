# app/schemas/user.py
from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime


# Base user data
class UserBase(BaseModel):
    email: EmailStr
    username: str
    full_name: Optional[str] = None


# Sign-up request schema
class SignUpRequest(UserBase):
    password: str


# Sign-in request schema
class SignInRequest(BaseModel):
    email: EmailStr
    password: str


# Update request schema
class UserUpdateRequest(BaseModel):
    full_name: Optional[str] = None


# Single user response schema
class UserDetailResponse(UserBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


# List of users response
class UsersListResponse(BaseModel):
    users: List[UserDetailResponse]
