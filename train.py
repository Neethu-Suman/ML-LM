# train.py
import numpy as np
import joblib
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

def train_and_save_model():
    # 1. Generate some dummy linear data (y = 2x + 1 + noise)
    np.random.seed(42)
    X = np.random.rand(100, 1) * 10
    y = 2 * X + 1 + np.random.randn(100, 1)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 2. Train the Linear Regression Model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # 3. Evaluate the model
    predictions = model.predict(X_test)
    r2 = r2_score(y_test, predictions)
    print(f"Model Trained. R² Score: {r2:.4f}")

    # 4. Save the trained model artifact
    joblib.dump(model, "linear_model.pkl")

    # 5. Save metrics to a file for tracking
    with open("metrics.txt", "w") as f:
        f.write(f"R2_Score: {r2:.4f}\n")
        f.write(f"Slope: {model.coef_[0][0]:.4f}\n")
        f.write(f"Intercept: {model.intercept_[0]:.4f}\n")

if __name__ == "__main__":
    train_and_save_model()