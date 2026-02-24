import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib
import os

# Generate synthetic dataset
np.random.seed(42)

data = pd.DataFrame({
    "study_hours": np.random.randint(1, 10, 500),
    "sleep_hours": np.random.randint(4, 10, 500),
    "screen_time": np.random.randint(1, 8, 500),
    "attendance": np.random.randint(50, 100, 500),
    "practice_tests": np.random.randint(0, 10, 500)
})

data["final_score"] = (
    data["study_hours"] * 5 +
    data["sleep_hours"] * 2 -
    data["screen_time"] * 1.5 +
    data["attendance"] * 0.3 +
    data["practice_tests"] * 4 +
    np.random.normal(0, 5, 500)
)

X = data.drop("final_score", axis=1)
y = data["final_score"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestRegressor()
model.fit(X_train, y_train)

os.makedirs("model", exist_ok=True)
joblib.dump(model, "model/model.pkl")

print("Model trained and saved successfully!")