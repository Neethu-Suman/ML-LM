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

    # Real-world single feature baseline threshold for California Housing
    assert r2_score >= 0.40, f"Model performance dropped below baseline! R² is {r2_score}"

    # 4. Functional Sanity Check: Ensure model predicts logical values
    model = joblib.load("linear_model.pkl")
    
    # Test input: An income of 5.0 ($50,000)
    test_input = np.array([[5.0]])
    prediction = model.predict(test_input)[0]
    
    # California house values are expressed in hundreds of thousands ($100,000s)
    # An income of 5.0 should reasonably predict a house between $150k and $300k (1.5 to 3.0)
    assert 1.5 <= prediction <= 3.0, f"Unreasonable house price prediction: {prediction}"