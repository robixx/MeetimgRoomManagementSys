
from pydantic import BaseModel, Field, field_validator
from datetime import datetime, time
from typing import Optional

class RoomManageDto(BaseModel):
    room_id: int
    room_name: Optional[str] = None
    number_seats: int
    location: Optional[str] = None
    create_by: Optional[int]| None = None
    create_date: Optional[datetime] = Field(default_factory=datetime.now)  
    is_status: int
    
    
    @field_validator("create_date", mode="before")
    def parse_create_date(cls, v):
        if v is None:
            return datetime.now()
        if isinstance(v, str):
            try:
                return datetime.strptime(v, "%d-%m-%Y")
            except ValueError:
                return datetime.fromisoformat(v)
        if isinstance(v, time):  # ✅ import time from datetime
            today = datetime.today()
            return datetime.combine(today, v)
        return v  # already datetime
