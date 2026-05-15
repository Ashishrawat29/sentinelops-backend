from fastapi import APIRouter

from app.schemas.prediction_schema import (
    PredictionInput
)

from app.services.prediction_service import (
    predict_failure
)

from app.services.recommendation_service import (
    generate_recommendation
)

router = APIRouter()

@router.post("/")
def predict(data: PredictionInput):

    result = predict_failure(data)

    if result["prediction"] == 1:
        risk = "Critical"

    else:
        risk = "Healthy"

    recommendations = generate_recommendation(

        data.temperature,
        data.vibration,
        data.voltage,
        data.pressure,
        data.runtime_hours,
    )

    return {

        "prediction":
            result["prediction"],

        "risk_level":
            risk,

        "failure_probability":
            result["failure_probability"],

        "recommendations":
            recommendations,
    }
    
