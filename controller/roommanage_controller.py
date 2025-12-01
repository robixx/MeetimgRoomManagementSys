
from fastapi import APIRouter, Depends, HTTPException,Query
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from db.config import get_db
from models.viewmodel.roommanageDto import RoomManageDto
from models.viewmodel.addroommanage import addRoomManageDto
from interface.room_manage_interface import IRoomManageService
from services.room_manage_service import RoomManageService
from models.viewmodel.responseModel import ResponseModel


router = APIRouter()

# Dependency injection
async def get_room_service() -> IRoomManageService:
    return RoomManageService()

@router.get("/room_list", response_model=ResponseModel[RoomManageDto])
async def get_rooms(
    db: AsyncSession = Depends(get_db),
    service: IRoomManageService = Depends(get_room_service)
):
   
    roomlist=await service.get_all_rooms(db)
    return ResponseModel(
        status=200,
        message="Data retrieved successfully",
        data=roomlist
    )
    
@router.post("/add_rooms", response_model=ResponseModel[RoomManageDto])
async def save_room(
    room: RoomManageDto,  # request body
    db: AsyncSession = Depends(get_db),
    service: IRoomManageService = Depends(get_room_service)
):
    try:
        saved_room =await service.add_room(db, room)  # call service to save
        return ResponseModel(
            status=200,
            message="Room added successfully",
            data=[saved_room]  # wrap in list to match ResponseModel[RoomManageDto]
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/edit-room", response_model=ResponseModel[RoomManageDto])
async def find_room(
    roomid: int = Query(..., description="Room ID"),  # ✅ correct type hint
    db: AsyncSession = Depends(get_db),
    service: IRoomManageService = Depends(get_room_service)
):
    try:
        found = await service.get_room_id(db, roomid)

        if not found:
            raise HTTPException(status_code=404, detail="Room not found")
        
        return ResponseModel(
            status=200,
            message="Data retrieved successfully",
            data=[found]  # wrap in a list to match ResponseModel[List[RoomManageDto]]
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))