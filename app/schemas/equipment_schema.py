from pydantic import BaseModel
from datetime import date

class EquipmentCreate(BaseModel):
    equipment_name: str
    category: str
    status: str
    health_score: float
    deployment_location: str
    last_maintenance: date

class EquipmentResponse(EquipmentCreate):
    id: int

    class Config:
        orm_mode = True