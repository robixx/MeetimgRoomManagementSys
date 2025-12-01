from fastapi import FastAPI
from controller import roommanage_controller, auth_controller
from db.base import Base
from db.config import async_engine


from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Runs before app starts
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    # Runs on shutdown (optional cleanup)
    await async_engine.dispose()

app = FastAPI(title="Room booking System",lifespan=lifespan)

# Include router with prefix and tags
app.include_router(
    roommanage_controller.router,
    prefix="/rooms",
    tags=["Room Management"]
)

app.include_router(
    auth_controller.router,
    prefix="/auth",
    tags=["User Login"]
)
