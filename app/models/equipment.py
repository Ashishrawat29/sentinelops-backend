from sqlalchemy import Column, Integer, String, Float, Date
from app.database import Base

class Equipment(Base):
    __tablename__ = "equipment"

    id = Column(Integer, primary_key=True, index=True)

    equipment_name = Column(String(100))
    category = Column(String(100))

    status = Column(String(50))

    health_score = Column(Float)

    deployment_location = Column(String(100))

    last_maintenance = Column(Date)