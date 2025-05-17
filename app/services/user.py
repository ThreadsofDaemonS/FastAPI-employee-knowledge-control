# app/services/user.py

from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.db.models import User
from app.schemas.user import SignUpRequest, UserUpdateRequest
from app.utils.security import hash_password
from app.core.logger import logger


class UserService:
    @staticmethod
    async def get_all(session: AsyncSession, limit: int = 10, offset: int = 0) -> list[User]:
        """Return a list of users with pagination."""
        result = await session.execute(select(User).offset(offset).limit(limit))
        users = result.scalars().all()
        return users

    @staticmethod
    async def get_by_id(session: AsyncSession, user_id: int) -> User:
        """Get user by ID or raise 404."""
        result = await session.execute(select(User).where(User.id == user_id))
        user = result.scalar_one_or_none()
        if user is None:
            logger.warning(f"User with ID {user_id} not found")
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        return user

    @staticmethod
    async def create(session: AsyncSession, user_data: SignUpRequest) -> User:
        """Create user with hashed password."""
        hashed_pw = hash_password(user_data.password)
        new_user = User(
            email=user_data.email,
            username=user_data.username,
            full_name=user_data.full_name,
            hashed_password=hashed_pw
        )
        session.add(new_user)
        await session.commit()
        await session.refresh(new_user)
        logger.info(f"User created: {new_user.email}")
        return new_user

    @staticmethod
    async def update(session: AsyncSession, user_id: int, update_data: UserUpdateRequest) -> User:
        """Update full name and/or password."""
        user = await UserService.get_by_id(session, user_id)

        if update_data.full_name:
            user.full_name = update_data.full_name

        if update_data.password:
            user.hashed_password = hash_password(update_data.password)

        await session.commit()
        await session.refresh(user)
        logger.info(f"User updated: ID {user_id}")
        return user

    @staticmethod
    async def delete(session: AsyncSession, user_id: int) -> None:
        """Delete user by ID."""
        user = await UserService.get_by_id(session, user_id)
        await session.delete(user)
        await session.commit()
        logger.info(f"User deleted: ID {user_id}")
