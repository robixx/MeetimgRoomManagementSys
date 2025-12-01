
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class addRoomManageDto(BaseModel):
   
    room_name: Optional[str] = None
    number_seats: int
    location: Optional[str] = None
    create_by: Optional[int]| None = None   
    is_status: int   