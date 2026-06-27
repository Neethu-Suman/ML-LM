# test_model.py
import os
import joblib
import numpy as np

def test_ml_pipeline():
    # 1. Run the training pipeline to generate artifacts
    os.system("python train.py")

    # 2. Assert that files were successfully created
    assert os.path.exists("linear_model.pkl"), "Model file was not generated."
    assert os.path.exists("metrics.txt"), "Metrics log file was not generated."

    # 3. Load model and verify performance threshold
    with open("metrics.txt", "r") as f:
        lines = f.readlines()
        r2_score = float(lines[0].split(": ")[1].strip())

    # Ensure the model accuracy meets the production threshold
    assert r2_score >= 0.80, f"Model performance dropped! R² is only {r2_score}"

    # 4. Functional Sanity Check: Ensure model predicts logical values
    model = joblib.load("linear_model.pkl")
    test_input = np.array([[5.0]])
    prediction = model.predict(test_input)[0][0]
    
    # Given y = 2x + 1, x=5 should yield a result close to 11
    assert 9.0 <= prediction <= 13.0, f"Unreasonable model prediction: {prediction}"