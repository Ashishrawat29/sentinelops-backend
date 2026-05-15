import joblib
import numpy as np
import os

# CURRENT FILE DIRECTORY
BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

# MODEL PATH
model_path = os.path.join(
    BASE_DIR,
    "../../../trained_models/failure_model.pkl"
)

# LOAD MODEL
model = joblib.load(model_path)

def predict_failure(data):

    features = np.array([
        [
            data.temperature,
            data.vibration,
            data.voltage,
            data.pressure,
            data.runtime_hours
        ]
    ])

    prediction = model.predict(features)[0]

    probability = model.predict_proba(
        features
    )[0][1]

    return {
        "prediction": int(prediction),
        "failure_probability": float(probability)
    }