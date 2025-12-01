from abc import ABC, abstractmethod
from typing import List, Optional
from models.viewmodel.roommanageDto import RoomManageDto
from models.viewmodel.addroommanage import addRoomManageDto
from sqlalchemy.ext.asyncio import AsyncSession

class IRoomManageService(ABC):

    @abstractmethod
    async def get_all_rooms(self, db: AsyncSession) -> List[RoomManageDto]:
        pass
    
    @abstractmethod
    async def add_room(self, db: AsyncSession, room: RoomManageDto) -> RoomManageDto:
        pass
    
    @abstractmethod
    async def get_room_id(self, db: AsyncSession, roomid: int) -> Optional[RoomManageDto]:
        pass