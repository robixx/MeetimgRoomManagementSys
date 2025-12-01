


from fastapi import APIRouter, Depends, HTTPException,Query
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from db.config import get_db

from interface.user_auth_interface import IUserAuth
from services.user_auth_service import UserAuthoService
from models.viewmodel.responseModel import ResponseModel
from models.viewmodel.loginRequest import LoginRequest

router = APIRouter()

# Dependency injection
async def get_auth_service() -> IUserAuth:
    return UserAuthoService()





@router.post("/login")
async def login_user(data:LoginRequest, db: AsyncSession = Depends(get_db),
    service: IUserAuth = Depends(get_auth_service)):
    token=await service.login_user(data, db)
    return {
         "status": 200,
        "message": "Login successful",
        "data": token  # {"token": "...jwt..."}
    }
    