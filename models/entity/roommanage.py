from sqlalchemy import Column, BigInteger, Integer, String, DateTime
from db.base import Base
from datetime import datetime

class RoomManage(Base):
    __tablename__ = "Room_Manage"

    room_id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    room_name = Column(String)
    number_seats = Column(Integer, default=0)
    location = Column(String)
    create_by = Column(Integer)
    create_date = Column(DateTime,default=datetime.now)
    is_status = Column(Integer, default=1)

