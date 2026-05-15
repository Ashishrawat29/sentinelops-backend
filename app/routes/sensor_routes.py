from fastapi import APIRouter

from app.schemas.sensor_schema import (
    SensorDataCreate,
)

router = APIRouter()


# ADD SENSOR DATA

@router.post("/")
def add_sensor_data(
    sensor: SensorDataCreate,
):

    return {

        "message":
            "Sensor data received successfully",

        "data":
            sensor.dict(),
    }


# GET ALL SENSOR DATA

@router.get("/")
def get_sensor_data():

    return {

        "message":
            "Sensor data endpoint working",
    }


# GET SENSOR DATA FOR EQUIPMENT

@router.get("/{equipment_id}")
def get_equipment_sensor_data(
    equipment_id: int,
):

    return {

        "equipment_id":
            equipment_id,

        "message":
            "Equipment sensor endpoint working",
    }