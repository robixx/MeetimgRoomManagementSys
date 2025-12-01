
from abc import ABC, abstractmethod
from sqlalchemy.ext.asyncio import AsyncSession



class IUserAuth(ABC):

    @abstractmethod
    async def login_user(self, username:str, password:str, db: AsyncSession):
         pass