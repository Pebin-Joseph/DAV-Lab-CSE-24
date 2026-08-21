"""
Experiment 5B: Building and Validating Logistic Models
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
UCI_DIABETES_PATH = os.path.join(BASE_DIR, "data", "raw", "uci_diabetes.csv")
PIMA_DIABETES_PATH = os.path.join(BASE_DIR, "data", "raw", "pima_diabetes.csv")
PLOTS_DIR = os.path.join(BASE_DIR, "data", "processed", "plots")


def evaluate_logistic_model(df, features, target):
    x_data = df[features]
    y_data = df[target]

    x_train, x_test, y_train, y_test = train_test_split(
        x_data, y_data, test_size=0.2, random_state=42
    )

    model = LogisticRegression(max_iter=1000)
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)

    return {
        "accuracy": accuracy_score(y_test, y_pred),
        "precision": precision_score(y_test, y_pred, zero_division=0),
        "recall": recall_score(y_test, y_pred, zero_division=0),
        "f1": f1_score(y_test, y_pred, zero_division=0),
        "cm": confusion_matrix(y_test, y_pred),
    }


def save_confusion_matrix(cm, title, path):
    plt.figure(figsize=(5, 4))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
    plt.title(title)
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.tight_layout()
    plt.savefig(path)
    plt.close()


def run_experiment_5b():
    print("==================================================")
    print("EXPERIMENT 5B: BUILDING AND VALIDATING LOGISTIC MODELS")
    print("==================================================")

    if not (os.path.exists(UCI_DIABETES_PATH) and os.path.exists(PIMA_DIABETES_PATH)):
        from src.utils.dataset_loader import load_all_datasets

        load_all_datasets()

    os.makedirs(PLOTS_DIR, exist_ok=True)

    uci_diabetes = pd.read_csv(UCI_DIABETES_PATH)
    pima_diabetes = pd.read_csv(PIMA_DIABETES_PATH)

    features = ["Glucose", "BloodPressure", "BMI"]
    target = "Outcome"

    uci_metrics = evaluate_logistic_model(uci_diabetes, features, target)
    pima_metrics = evaluate_logistic_model(pima_diabetes, features, target)

    uci_plot = os.path.join(PLOTS_DIR, "exp5b_uci_confusion_matrix.png")
    pima_plot = os.path.join(PLOTS_DIR, "exp5b_pima_confusion_matrix.png")

    save_confusion_matrix(uci_metrics["cm"], "UCI - Confusion Matrix", uci_plot)
    save_confusion_matrix(pima_metrics["cm"], "Pima - Confusion Matrix", pima_plot)

    print("UCI Logistic Regression Results:")
    print(
        f"Accuracy: {uci_metrics['accuracy']:.4f}, Precision: {uci_metrics['precision']:.4f}, Recall: {uci_metrics['recall']:.4f}, F1: {uci_metrics['f1']:.4f}"
    )

    print("\nPima Logistic Regression Results:")
    print(
        f"Accuracy: {pima_metrics['accuracy']:.4f}, Precision: {pima_metrics['precision']:.4f}, Recall: {pima_metrics['recall']:.4f}, F1: {pima_metrics['f1']:.4f}"
    )

    print(f"\nSaved plots: {uci_plot}")
    print(f"Saved plots: {pima_plot}")


if __name__ == "__main__":
    run_experiment_5b()
