# Linear Regression CI/CD MLOps Pipeline

An end-to-end MLOps (Machine Learning Operations) pipeline demonstrating Continuous Integration (CI) and Continuous Deployment (CD) for a Linear Regression model.

The system automatically trains a model, validates that its accuracy meets production standards via automated tests, and packages the verified model as a deployment-ready artifact using GitHub Actions.

## 🏗️ Architecture & Pipeline Workflow

This project implements a standard automated MLOps loop:

Plaintext

    [ Code Push ] ➡️ [ GitHub Actions Runner ] ➡️ [ Install ML Dependencies ] ➡️ [ Evaluate Model Performance (R² > 0.80) ] ➡️ [ Deploy Trained Model Artifact ]

1. Continuous Integration (CI): Every code commit triggers automated tests via pytest. The pipeline checks if the model script executes successfully and ensures the trained model's R^2
  performance score meets our minimum quality threshold.

2. Continuous Deployment (CD): If and only if the evaluation checks pass, the pipeline packages the serialized model (linear_model.pkl) and its associated metadata (metrics.txt) as downloadable build artifacts.

## 📂 Project Structure

Plaintext

    📁 linear-regression-pipeline
    
    ├── 📁 .github/
    
    │   └── 📁 workflows/
    
    │       └── 📄 ml_ci_cd.yml    # GitHub Actions workflow configuration
    
    ├── 📄 train.py               # Linear regression training script
    
    ├── 📄 test_model.py          # Pytest suite validating model accuracy and sanity
    
    └── 📄 requirements.txt       # Python environment dependencies

## 🚀 Getting Started (Local Setup)

Prerequisites

Make sure you have Python 3.10+ installed on your system.

1. Clone and Install
Open your terminal (or VS Code terminal) and run:

Bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd linear-regression-pipeline

# Install the required ML packages
pip install -r requirements.txt
2. Run Training Locally
To execute the pipeline manually and train the linear regression model:

Bash
python train.py
This will generate two files in your workspace:

linear_model.pkl: The trained, serialized Scikit-Learn model.

metrics.txt: A text file capturing the model's R 
2
  score, calculated slope, and intercept.

3. Run Validation Tests
To run the automated test suite locally exactly how the GitHub Actions runner executes it:

Bash
pytest test_model.py
🛠️ CI/CD Gatekeeping Thresholds
To prevent broken or underperforming models from reaching production, test_model.py enforces the following constraints:

Artifact Integrity: The training script must generate both the .pkl and metrics.txt files without errors.

Performance Quality: The model's R 
2
  validation score must be ≥0.80.

Sanity Baseline Check: Given a test feature input of 5.0 on the linear equation (y=2x+1+noise), the model's prediction must fall logically within a realistic boundary (9.0≤prediction≤13.0).

📄 License
Distributed under the MIT License. See LICENSE for more information.
