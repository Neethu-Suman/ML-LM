# Step-by-step procedure to build, test, and push this pipeline using VS Code.

## CI/CD python code for linear regression

Setting up a CI/CD pipeline for a Machine Learning model like Linear Regression adds a few unique requirements compared to standard software pipelines. In addition to testing if the code runs, the pipeline should 
also validate that the model performs adequately (e.g., checking that the $R^2$ score or Mean Squared Error meets a minimum threshold before deployment).Here is the complete step-by-step setup using VS Code, 
Python (Scikit-Learn), and GitHub Actions.

## Step 1: Create the Project Structure in VS Code

Open a new folder in VS Code and create the following directory structure:
Plaintext
📁 linear-regression-pipeline
├── 📁 .github
│   └── 📁 workflows
│       └── 📄 ml_ci_cd.yml
├── 📄 train.py
├── 📄 test_model.py
└── 📄 requirements.txt
Step 2: Write the Model Training Script (train.py)
This script generates synthetic data, trains a simple Linear Regression model, evaluates it, and saves both the model file (.pkl) and a text file tracking its performance metrics.
Step 3: Write the Automated Test (test_model.py)
This script acts as the CI gatekeeper. It runs the training script and asserts that the resulting model is valid and performs better than a baseline threshold (e.g., $R^2 > 0.80$).
Step 4: Define Dependencies (requirements.txt)
Add the libraries needed to compile data, train models, and execute tests:
Step 5: Create the GitHub Actions Workflow (.github/workflows/ml_ci_cd.yml)
This YAML configuration instructs GitHub to spin up a server, build the environment, run your ML validation test suite, and—if successful—save the resulting pipeline model as a production artifact.
Step 6: Push to GitHub via VS Code Terminal
Open your VS Code terminal (Ctrl + `) and execute the following commands to initialize Git and push your machine learning pipeline live:
git init 
git add . 
git commit -m "feat: complete linear regression ml ops pipeline" 
git branch -M main git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git git push -u origin main
