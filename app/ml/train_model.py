import pandas as pd
import os

from sklearn.model_selection import (
    train_test_split
)

from sklearn.ensemble import (
    RandomForestClassifier
)

from sklearn.metrics import accuracy_score

import joblib


# CURRENT FILE DIRECTORY
BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

# DATASET PATH
dataset_path = os.path.join(
    BASE_DIR,
    "../../../dataset/equipment_sensor_data.csv"
)

# MODEL SAVE PATH
model_path = os.path.join(
    BASE_DIR,
    "../../../trained_models/failure_model.pkl"
)

# LOAD DATASET
data = pd.read_csv(dataset_path)

# FEATURES
X = data[
    [
        "temperature",
        "vibration",
        "voltage",
        "pressure",
        "runtime_hours"
    ]
]

# TARGET
y = data["failure"]

# SPLIT DATA
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# MODEL
model = RandomForestClassifier()

# TRAIN MODEL
model.fit(X_train, y_train)

# PREDICTIONS
predictions = model.predict(X_test)

# ACCURACY
accuracy = accuracy_score(
    y_test,
    predictions
)

print(f"Model Accuracy: {accuracy}")

# SAVE MODEL
joblib.dump(model, model_path)

print("Model saved successfully")