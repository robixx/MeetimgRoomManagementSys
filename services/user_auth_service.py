import os
import jwt
from interface.user_auth_interface import IUserAuth
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime,timedelta
from dotenv import load_dotenv
from models.viewmodel.loginRequest import LoginRequest


load_dotenv(dotenv_path=".env")

secret_key= os.getenv("SECRET_KEY")



class UserAuthoService(IUserAuth):
    async def login_user(self, data:LoginRequest, db: AsyncSession):
        if data.username == "admin" and data.password == "123":
            payload = {
                "username": data.username,
                "exp": datetime.now() + timedelta(hours=2)
            }
            token = jwt.encode(payload, secret_key, algorithm="HS256")
            return token
    
        return {"error": "Invalid credentials"}