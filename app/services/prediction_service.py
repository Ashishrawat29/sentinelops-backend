from app.schemas.prediction_schema import (
    PredictionRequest,
)


def predict_failure(
    data: PredictionRequest,
):

    risk_score = 0

    recommendations = []

    # TEMPERATURE ANALYSIS

    if data.temperature >= 95:

        risk_score += 40

        recommendations.append(
            "Critical temperature detected."
        )

    elif data.temperature >= 80:

        risk_score += 25

        recommendations.append(
            "High temperature trend detected."
        )

    elif data.temperature >= 65:

        risk_score += 10

        recommendations.append(
            "Moderate temperature fluctuation."
        )

    # VIBRATION ANALYSIS

    if data.vibration >= 9:

        risk_score += 35

        recommendations.append(
            "Extreme vibration detected."
        )

    elif data.vibration >= 7:

        risk_score += 20

        recommendations.append(
            "High vibration detected."
        )

    elif data.vibration >= 5:

        risk_score += 10

        recommendations.append(
            "Moderate vibration detected."
        )

    # PRESSURE ANALYSIS

    if data.pressure >= 140:

        risk_score += 25

        recommendations.append(
            "Critical pressure anomaly detected."
        )

    elif data.pressure >= 120:

        risk_score += 15

        recommendations.append(
            "Pressure imbalance observed."
        )

    elif data.pressure >= 100:

        risk_score += 8

        recommendations.append(
            "Pressure slightly above optimal."
        )

    # RISK LEVEL

    if risk_score >= 80:

        risk_level = "Critical"

    elif risk_score >= 55:

        risk_level = "High"

    elif risk_score >= 30:

        risk_level = "Medium"

    else:

        risk_level = "Low"

    health_score = max(
        0,
        100 - risk_score,
    )

    failure_probability = min(
        risk_score,
        100,
    )

    return {

        "prediction":
            risk_level,

        "failure_probability":
            failure_probability,

        "health_score":
            health_score,

        "recommendations":
            recommendations,
    }