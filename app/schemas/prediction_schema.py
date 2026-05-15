from pydantic import BaseModel

class PredictionInput(BaseModel):
    temperature: float
    vibration: float
    voltage: float
    pressure: float
    runtime_hours: float