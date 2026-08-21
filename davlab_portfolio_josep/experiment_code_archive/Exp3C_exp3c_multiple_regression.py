"""
Experiment 3C: Statistical Analysis Using Diabetes Datasets - Multiple Regression Analysis
"""

import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
UCI_DIABETES_PATH = os.path.join(BASE_DIR, "data", "raw", "uci_diabetes.csv")
PIMA_DIABETES_PATH = os.path.join(BASE_DIR, "data", "raw", "pima_diabetes.csv")


def multiple_regression_analysis(df, features, target):
    x_data = df[features]
    y_data = df[target]

    x_train, x_test, y_train, y_test = train_test_split(
        x_data, y_data, test_size=0.2, random_state=42
    )

    model = LinearRegression()
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)

    return r2_score(y_test, y_pred)


def run_experiment_3c():
    print("==================================================")
    print("EXPERIMENT 3C: MULTIPLE REGRESSION ANALYSIS")
    print("==================================================")

    if not (os.path.exists(UCI_DIABETES_PATH) and os.path.exists(PIMA_DIABETES_PATH)):
        from src.utils.dataset_loader import load_all_datasets

        load_all_datasets()

    uci_diabetes = pd.read_csv(UCI_DIABETES_PATH)
    pima_diabetes = pd.read_csv(PIMA_DIABETES_PATH)

    features = ["Glucose", "BloodPressure", "Age"]
    target = "BMI"

    uci_r2 = multiple_regression_analysis(uci_diabetes, features, target)
    pima_r2 = multiple_regression_analysis(pima_diabetes, features, target)

    print(f"UCI Diabetes Dataset - Multiple Regression R2 Score: {uci_r2:.4f}")
    print(f"Pima Indians Diabetes Dataset - Multiple Regression R2 Score: {pima_r2:.4f}")


if __name__ == "__main__":
    run_experiment_3c()
