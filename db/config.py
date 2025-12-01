import os
from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from dotenv import load_dotenv


load_dotenv(dotenv_path=".env")

base_Url= os.getenv("DATABASE_URL")

async_engine = create_async_engine(base_Url, echo=True)

# Async session factory
async_session = async_sessionmaker(bind=async_engine, expire_on_commit=False)

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session