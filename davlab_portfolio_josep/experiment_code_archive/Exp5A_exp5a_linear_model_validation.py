"""
Experiment 5A: Building and Validating Linear Models
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
UCI_DIABETES_PATH = os.path.join(BASE_DIR, "data", "raw", "uci_diabetes.csv")
PIMA_DIABETES_PATH = os.path.join(BASE_DIR, "data", "raw", "pima_diabetes.csv")
PLOTS_DIR = os.path.join(BASE_DIR, "data", "processed", "plots")


def evaluate_linear_model(df, features, target):
    x_data = df[features]
    y_data = df[target]

    x_train, x_test, y_train, y_test = train_test_split(
        x_data, y_data, test_size=0.2, random_state=42
    )

    model = LinearRegression()
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)

    return {
        "r2": r2_score(y_test, y_pred),
        "mse": mean_squared_error(y_test, y_pred),
        "mae": mean_absolute_error(y_test, y_pred),
        "y_test": y_test,
        "y_pred": y_pred,
    }


def save_actual_vs_pred_plot(y_test, y_pred, title, path):
    plt.figure(figsize=(7, 5))
    plt.scatter(y_test, y_pred, color="green", alpha=0.7)
    min_val = min(y_test.min(), y_pred.min())
    max_val = max(y_test.max(), y_pred.max())
    plt.plot([min_val, max_val], [min_val, max_val], "r--", linewidth=2)
    plt.xlabel("Actual")
    plt.ylabel("Predicted")
    plt.title(title)
    plt.tight_layout()
    plt.savefig(path)
    plt.close()


def run_experiment_5a():
    print("==================================================")
    print("EXPERIMENT 5A: BUILDING AND VALIDATING LINEAR MODELS")
    print("==================================================")

    if not (os.path.exists(UCI_DIABETES_PATH) and os.path.exists(PIMA_DIABETES_PATH)):
        from src.utils.dataset_loader import load_all_datasets

        load_all_datasets()

    os.makedirs(PLOTS_DIR, exist_ok=True)

    uci_diabetes = pd.read_csv(UCI_DIABETES_PATH)
    pima_diabetes = pd.read_csv(PIMA_DIABETES_PATH)

    features = ["Glucose", "BloodPressure", "BMI"]
    target = "Age"

    uci_metrics = evaluate_linear_model(uci_diabetes, features, target)
    pima_metrics = evaluate_linear_model(pima_diabetes, features, target)

    uci_plot = os.path.join(PLOTS_DIR, "exp5a_uci_actual_vs_pred.png")
    pima_plot = os.path.join(PLOTS_DIR, "exp5a_pima_actual_vs_pred.png")
    save_actual_vs_pred_plot(
        uci_metrics["y_test"], uci_metrics["y_pred"], "UCI Linear Model: Actual vs Predicted", uci_plot
    )
    save_actual_vs_pred_plot(
        pima_metrics["y_test"], pima_metrics["y_pred"], "Pima Linear Model: Actual vs Predicted", pima_plot
    )

    print("UCI Linear Regression Results:")
    print(
        f"R2: {uci_metrics['r2']:.4f}, MSE: {uci_metrics['mse']:.4f}, MAE: {uci_metrics['mae']:.4f}"
    )

    print("\nPima Linear Regression Results:")
    print(
        f"R2: {pima_metrics['r2']:.4f}, MSE: {pima_metrics['mse']:.4f}, MAE: {pima_metrics['mae']:.4f}"
    )

    print(f"\nSaved plots: {uci_plot}")
    print(f"Saved plots: {pima_plot}")


if __name__ == "__main__":
    run_experiment_5a()
