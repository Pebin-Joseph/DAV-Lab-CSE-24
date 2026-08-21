"""
Experiment 3B: Bivariate Analysis - Linear and Logistic Regression Modeling
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import r2_score, accuracy_score

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
UCI_DIABETES_PATH = os.path.join(BASE_DIR, "data", "raw", "uci_diabetes.csv")
PIMA_DIABETES_PATH = os.path.join(BASE_DIR, "data", "raw", "pima_diabetes.csv")
PLOTS_DIR = os.path.join(BASE_DIR, "data", "processed", "plots")


def linear_regression_analysis(df, x_column, y_column, title, output_plot):
    x_data = df[[x_column]]
    y_data = df[y_column]
    model = LinearRegression()
    model.fit(x_data, y_data)
    y_pred = model.predict(x_data)
    r2 = r2_score(y_data, y_pred)

    plt.figure(figsize=(7, 5))
    plt.scatter(x_data, y_data, color="blue", alpha=0.7, label="Actual Data")
    plt.plot(x_data, y_pred, color="red", linewidth=2, label="Regression Line")
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.title(title)
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_plot)
    plt.close()

    return r2


def logistic_regression_analysis(df, features, target):
    x_data = df[features]
    y_data = df[target]

    x_train, x_test, y_train, y_test = train_test_split(
        x_data, y_data, test_size=0.2, random_state=42
    )
    model = LogisticRegression(max_iter=1000)
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    return accuracy_score(y_test, y_pred)


def run_experiment_3b():
    print("==================================================")
    print("EXPERIMENT 3B: BIVARIATE REGRESSION ANALYSIS")
    print("==================================================")

    if not (os.path.exists(UCI_DIABETES_PATH) and os.path.exists(PIMA_DIABETES_PATH)):
        from src.utils.dataset_loader import load_all_datasets

        load_all_datasets()

    os.makedirs(PLOTS_DIR, exist_ok=True)

    uci_diabetes = pd.read_csv(UCI_DIABETES_PATH)
    pima_diabetes = pd.read_csv(PIMA_DIABETES_PATH)

    print("\nUCI Diabetes Dataset Sample:")
    print(uci_diabetes.head())

    print("\nPima Indians Diabetes Dataset Sample:")
    print(pima_diabetes.head())

    uci_plot = os.path.join(PLOTS_DIR, "exp3b_uci_linear_regression.png")
    pima_plot = os.path.join(PLOTS_DIR, "exp3b_pima_linear_regression.png")

    uci_r2 = linear_regression_analysis(
        uci_diabetes,
        "Glucose",
        "BMI",
        "UCI: Linear Regression (Glucose vs BMI)",
        uci_plot,
    )
    pima_r2 = linear_regression_analysis(
        pima_diabetes,
        "Glucose",
        "BMI",
        "Pima: Linear Regression (Glucose vs BMI)",
        pima_plot,
    )

    features = ["Glucose", "BloodPressure", "BMI", "Age"]
    target = "Outcome"

    uci_accuracy = logistic_regression_analysis(uci_diabetes, features, target)
    pima_accuracy = logistic_regression_analysis(pima_diabetes, features, target)

    print("\nLinear Regression (Glucose -> BMI)")
    print(f"UCI R2 Score: {uci_r2:.4f}")
    print(f"Pima R2 Score: {pima_r2:.4f}")

    print("\nLogistic Regression (Outcome Classification)")
    print(f"UCI Accuracy: {uci_accuracy:.4f}")
    print(f"Pima Accuracy: {pima_accuracy:.4f}")

    print(f"\nSaved plots: {uci_plot}")
    print(f"Saved plots: {pima_plot}")


if __name__ == "__main__":
    run_experiment_3b()
