from sqlalchemy import (
    Column,
    Integer,
    Float,
    DateTime,
    ForeignKey
)

from datetime import datetime

from app.database import Base

class SensorData(Base):
    __tablename__ = "sensor_data"

    id = Column(Integer, primary_key=True, index=True)

    equipment_id = Column(
        Integer,
        ForeignKey("equipment.id")
    )

    temperature = Column(Float)

    vibration = Column(Float)

    voltage = Column(Float)

    pressure = Column(Float)

    runtime_hours = Column(Float)

    timestamp = Column(
        DateTime,
        default=datetime.utcnow
    )