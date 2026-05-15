from pydantic import BaseModel
from datetime import datetime

class SensorDataCreate(BaseModel):
    equipment_id: int
    temperature: float
    vibration: float
    voltage: float
    pressure: float
    runtime_hours: float

class SensorResponse(SensorDataCreate):
    id: int
    timestamp: datetime

    class Config:
        orm_mode = True