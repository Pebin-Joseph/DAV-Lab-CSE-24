"""
Experiment 4B: Hypothesis Testing - Z-Test on UCI Diabetes Dataset
"""

import os
import pandas as pd
from statsmodels.stats.weightstats import ztest

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
UCI_DIABETES_PATH = os.path.join(BASE_DIR, "data", "raw", "uci_diabetes.csv")


def run_experiment_4b():
    print("==================================================")
    print("EXPERIMENT 4B: Z-TEST ON UCI DIABETES DATASET")
    print("==================================================")

    if not os.path.exists(UCI_DIABETES_PATH):
        from src.utils.dataset_loader import load_all_datasets

        load_all_datasets()

    uci_diabetes = pd.read_csv(UCI_DIABETES_PATH)
    z_stat, p_value = ztest(uci_diabetes["Glucose"], value=100)

    print(f"Z-Statistic: {z_stat:.4f}")
    print(f"P-Value: {p_value:.4f}")

    alpha = 0.05
    if p_value < alpha:
        print("Reject the null hypothesis: Mean Glucose differs significantly from 100.")
    else:
        print("Fail to reject the null hypothesis: No significant difference from 100.")


if __name__ == "__main__":
    run_experiment_4b()
