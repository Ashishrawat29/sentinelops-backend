from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal

from app.models.sensor_data import SensorData

from app.schemas.sensor_schema import (
    SensorDataCreate
)

router = APIRouter()

def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()

# ADD SENSOR DATA
@router.post("/")
def add_sensor_data(
    sensor: SensorDataCreate,
    db: Session = Depends(get_db)
):
    new_sensor_data = SensorData(
        equipment_id=sensor.equipment_id,
        temperature=sensor.temperature,
        vibration=sensor.vibration,
        voltage=sensor.voltage,
        pressure=sensor.pressure,
        runtime_hours=sensor.runtime_hours
    )

    db.add(new_sensor_data)

    db.commit()

    db.refresh(new_sensor_data)

    return {
        "message": "Sensor data added successfully"
    }

# GET ALL SENSOR DATA
@router.get("/")
def get_sensor_data(
    db: Session = Depends(get_db)
):
    data = db.query(SensorData).all()

    return data

# GET SENSOR DATA FOR EQUIPMENT
@router.get("/{equipment_id}")
def get_equipment_sensor_data(
    equipment_id: int,
    db: Session = Depends(get_db)
):
    data = db.query(SensorData).filter(
        SensorData.equipment_id == equipment_id
    ).all()

    return data