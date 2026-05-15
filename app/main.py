from fastapi import FastAPI

from app.database import Base, engine
from fastapi.middleware.cors import CORSMiddleware
from app.models.user import User
from app.models.equipment import Equipment
from app.models.sensor_data import SensorData
from app.routes.prediction_routes import (
    router as prediction_router
)

from app.routes.sensor_routes import (
    router as sensor_router
)

from app.routes.websocket_routes import (
    router as websocket_router
)

from app.routes.auth_routes import router
from app.routes.equipment_routes import (
    router as equipment_router
)

app = FastAPI()

app.include_router(
    router,
    prefix="/auth",
    tags=["Authentication"]
)

app.include_router(
    equipment_router,
    prefix="/equipment",
    tags=["Equipment"]
)

app.include_router(
    sensor_router,
    prefix="/sensor",
    tags=["Sensor Data"]
)

app.include_router(
    prediction_router,
    prefix="/predict",
    tags=["Prediction"]
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(websocket_router)

@app.get("/")
def home():
    return {
        "message": "API Running Successfully"
    }