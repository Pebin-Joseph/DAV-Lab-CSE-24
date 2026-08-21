"""
Experiment 4D: Hypothesis Testing - ANOVA on Diabetes Datasets
"""

import os
import pandas as pd
from scipy.stats import f_oneway

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
UCI_DIABETES_PATH = os.path.join(BASE_DIR, "data", "raw", "uci_diabetes.csv")
PIMA_DIABETES_PATH = os.path.join(BASE_DIR, "data", "raw", "pima_diabetes.csv")


def run_experiment_4d():
    print("==================================================")
    print("EXPERIMENT 4D: ANOVA ON UCI AND PIMA DIABETES DATASETS")
    print("==================================================")

    if not (os.path.exists(UCI_DIABETES_PATH) and os.path.exists(PIMA_DIABETES_PATH)):
        from src.utils.dataset_loader import load_all_datasets

        load_all_datasets()

    uci_diabetes = pd.read_csv(UCI_DIABETES_PATH)
    pima_diabetes = pd.read_csv(PIMA_DIABETES_PATH)

    numerical_columns = ["Glucose", "BloodPressure", "BMI"]
    anova_results = {}

    for col in numerical_columns:
        f_stat, p_value = f_oneway(uci_diabetes[col], pima_diabetes[col])
        anova_results[col] = {"F-statistic": f_stat, "P-value": p_value}

    anova_df = pd.DataFrame(anova_results).T
    print("\nANOVA Results:")
    print(anova_df.to_string())


if __name__ == "__main__":
    run_experiment_4d()
