"""
Experiment 4C: Hypothesis Testing - T-Test on Diabetes Datasets
"""

import os
import pandas as pd
from scipy.stats import ttest_ind

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
UCI_DIABETES_PATH = os.path.join(BASE_DIR, "data", "raw", "uci_diabetes.csv")
PIMA_DIABETES_PATH = os.path.join(BASE_DIR, "data", "raw", "pima_diabetes.csv")


def run_experiment_4c():
    print("==================================================")
    print("EXPERIMENT 4C: T-TEST ON UCI AND PIMA DIABETES DATASETS")
    print("==================================================")

    if not (os.path.exists(UCI_DIABETES_PATH) and os.path.exists(PIMA_DIABETES_PATH)):
        from src.utils.dataset_loader import load_all_datasets

        load_all_datasets()

    uci_diabetes = pd.read_csv(UCI_DIABETES_PATH)
    pima_diabetes = pd.read_csv(PIMA_DIABETES_PATH)

    numerical_columns = ["Glucose", "BloodPressure", "BMI"]
    t_test_results = {}

    for col in numerical_columns:
        t_stat, p_value = ttest_ind(
            uci_diabetes[col], pima_diabetes[col], equal_var=False
        )
        t_test_results[col] = {"T-statistic": t_stat, "P-value": p_value}

    t_test_df = pd.DataFrame(t_test_results).T
    print("\nT-test Results:")
    print(t_test_df.to_string())


if __name__ == "__main__":
    run_experiment_4c()
