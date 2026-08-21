"""
Experiment 4A: Data Visualization - Normal Curves on UCI Diabetes Dataset
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
UCI_DIABETES_PATH = os.path.join(BASE_DIR, "data", "raw", "uci_diabetes.csv")
PLOTS_DIR = os.path.join(BASE_DIR, "data", "processed", "plots")


def run_experiment_4a():
    print("==================================================")
    print("EXPERIMENT 4A: NORMAL CURVES ON UCI DIABETES DATASET")
    print("==================================================")

    if not os.path.exists(UCI_DIABETES_PATH):
        from src.utils.dataset_loader import load_all_datasets

        load_all_datasets()

    os.makedirs(PLOTS_DIR, exist_ok=True)

    uci_diabetes = pd.read_csv(UCI_DIABETES_PATH)

    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    sns.histplot(uci_diabetes["Glucose"], kde=True, stat="density", linewidth=0)
    x_values = np.linspace(uci_diabetes["Glucose"].min(), uci_diabetes["Glucose"].max(), 100)
    plt.plot(x_values, norm.pdf(x_values, uci_diabetes["Glucose"].mean(), uci_diabetes["Glucose"].std()), "r")
    plt.title("Normal Curve - Glucose")

    plt.subplot(1, 2, 2)
    sns.histplot(uci_diabetes["BMI"], kde=True, stat="density", linewidth=0)
    x_values = np.linspace(uci_diabetes["BMI"].min(), uci_diabetes["BMI"].max(), 100)
    plt.plot(x_values, norm.pdf(x_values, uci_diabetes["BMI"].mean(), uci_diabetes["BMI"].std()), "r")
    plt.title("Normal Curve - BMI")

    plt.tight_layout()
    output_plot = os.path.join(PLOTS_DIR, "exp4a_normal_curves.png")
    plt.savefig(output_plot)
    plt.close()

    print(f"Saved normal curve plot: {output_plot}")


if __name__ == "__main__":
    run_experiment_4a()
