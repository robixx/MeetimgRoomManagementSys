
from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from interface.room_manage_interface import IRoomManageService
from models.entity.roommanage import RoomManage
from models.viewmodel.roommanageDto import RoomManageDto
from sqlalchemy import cast, BigInteger, select

class RoomManageService(IRoomManageService):

    async def get_all_rooms(self, db: AsyncSession) -> List[RoomManageDto]:
        result = await db.execute(select(RoomManage))
        rooms = result.scalars().all()

        return [
            RoomManageDto(
                room_id=room.room_id,
                room_name=room.room_name,
                location=room.location,
                number_seats=room.number_seats,
                create_by=room.create_by,
                create_date=room.create_date,
                is_status=room.is_status
            ) for room in rooms
        ]

    async def add_room(self, db: AsyncSession, room: RoomManageDto) -> RoomManageDto:
    # Update existing room
     if room.room_id and room.room_id > 0:
        query = select(RoomManage).where(RoomManage.room_id == room.room_id)
        result = await db.execute(query)
        existing_room = result.scalar_one_or_none()

        if not existing_room:
            raise Exception("Room not found for update")

        # Update fields
        existing_room.room_name = room.room_name
        existing_room.number_seats = room.number_seats
        existing_room.location = room.location
        existing_room.create_by = room.create_by        
        existing_room.is_status = room.is_status or 1

        db.add(existing_room)
        await db.commit()
        await db.refresh(existing_room)

        return RoomManageDto(
            room_id=existing_room.room_id,
            room_name=existing_room.room_name,
            number_seats=existing_room.number_seats,
            location=existing_room.location,
            create_by=existing_room.create_by,
            create_date=existing_room.create_date,
            is_status=existing_room.is_status
        )

    # Insert new room
     new_room = RoomManage(
        room_name=room.room_name,
        number_seats=room.number_seats,
        location=room.location,
        create_by=room.create_by,
        create_date=room.create_date,
        is_status=room.is_status or 1
    )
     db.add(new_room)
     await db.commit()
     await db.refresh(new_room)

     return RoomManageDto(
        room_id=new_room.room_id,
        room_name=new_room.room_name,
        number_seats=new_room.number_seats,
        location=new_room.location,
        create_by=new_room.create_by,
        create_date=new_room.create_date,
        is_status=new_room.is_status
    )

    async def get_room_id(self, db: AsyncSession, roomid: int) -> Optional[RoomManageDto]:
        query = select(RoomManage).where(RoomManage.room_id == roomid)
        result = await db.execute(query)
        room = result.scalars().first()  # use scalars() to get ORM objects

        if not room:
            return None  # or raise HTTPException in controller

        return RoomManageDto(
            room_id=room.room_id,
            room_name=room.room_name,
            number_seats=room.number_seats,
            location=room.location,
            create_by=room.create_by,
            create_date=room.create_date,
            is_status=room.is_status
        )