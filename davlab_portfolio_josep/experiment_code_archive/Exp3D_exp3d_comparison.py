"""
Experiment 3D: Comparison of Analysis Results Between UCI and Pima Diabetes Datasets
"""

import os
import pandas as pd
from scipy.stats import skew, kurtosis
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import r2_score, accuracy_score

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
UCI_DIABETES_PATH = os.path.join(BASE_DIR, "data", "raw", "uci_diabetes.csv")
PIMA_DIABETES_PATH = os.path.join(BASE_DIR, "data", "raw", "pima_diabetes.csv")


def summary_stats(df, columns):
    stats = {}
    for col in columns:
        stats[col] = {
            "Mean": df[col].mean(),
            "Median": df[col].median(),
            "Variance": df[col].var(ddof=1),
            "Skewness": skew(df[col]),
            "Kurtosis": kurtosis(df[col]),
        }
    return pd.DataFrame(stats).T


def regression_scores(df):
    x_lin = df[["Glucose"]]
    y_lin = df["BMI"]
    lin_model = LinearRegression()
    lin_model.fit(x_lin, y_lin)
    lin_r2 = r2_score(y_lin, lin_model.predict(x_lin))

    features = ["Glucose", "BloodPressure", "BMI", "Age"]
    target = "Outcome"
    x_data = df[features]
    y_data = df[target]
    x_train, x_test, y_train, y_test = train_test_split(
        x_data, y_data, test_size=0.2, random_state=42
    )
    log_model = LogisticRegression(max_iter=1000)
    log_model.fit(x_train, y_train)
    log_acc = accuracy_score(y_test, log_model.predict(x_test))

    return lin_r2, log_acc


def run_experiment_3d():
    print("==================================================")
    print("EXPERIMENT 3D: COMPARATIVE ANALYSIS (UCI vs PIMA)")
    print("==================================================")

    if not (os.path.exists(UCI_DIABETES_PATH) and os.path.exists(PIMA_DIABETES_PATH)):
        from src.utils.dataset_loader import load_all_datasets

        load_all_datasets()

    uci_diabetes = pd.read_csv(UCI_DIABETES_PATH)
    pima_diabetes = pd.read_csv(PIMA_DIABETES_PATH)

    cols = [
        "Glucose",
        "BloodPressure",
        "SkinThickness",
        "Insulin",
        "BMI",
        "DiabetesPedigreeFunction",
        "Age",
    ]

    uci_summary = summary_stats(uci_diabetes, cols)
    pima_summary = summary_stats(pima_diabetes, cols)

    print("\nUCI Summary Statistics:")
    print(uci_summary.to_string())

    print("\nPima Summary Statistics:")
    print(pima_summary.to_string())

    uci_r2, uci_acc = regression_scores(uci_diabetes)
    pima_r2, pima_acc = regression_scores(pima_diabetes)

    print("\nRegression Performance Comparison:")
    print(f"Linear Regression R2 - UCI: {uci_r2:.4f}, Pima: {pima_r2:.4f}")
    print(f"Logistic Regression Accuracy - UCI: {uci_acc:.4f}, Pima: {pima_acc:.4f}")


if __name__ == "__main__":
    run_experiment_3d()
