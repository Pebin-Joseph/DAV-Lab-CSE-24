# DAV Lab CSE 24

This repository contains a complete data analytics and visualization lab portfolio built around Python-based experiments, datasets, and saved outputs.

The project includes all major experiments from the lab manual, organized into a cleaner structure for submission and portfolio use.

---

## Project Overview

This repository demonstrates work in:
- data loading and preprocessing
- NumPy and Pandas operations
- descriptive statistics
- regression and comparison analysis
- hypothesis testing
- ANOVA
- logistic and linear model validation
- time series analysis

The code is organized for clarity and reuse, and the final outputs are saved separately in archive folders.

---

## Repository Structure

```text
DAV-Lab-CSE-24-main/
├── README.md
├── requirements.txt
├── .gitignore
├── data/
│   ├── raw/
│   │   ├── Google_data.csv
│   │   ├── iris.csv
│   │   ├── pima_diabetes.csv
│   │   ├── uci_diabetes.csv
│   │   └── data_sample.xlsx
│   └── processed/
│       ├── processed_text.csv
│       ├── processed_excel.xlsx
│       ├── subset_data.csv
│       └── plots/
├── src/
│   ├── __init__.py
│   ├── experiments/
│   │   ├── exp1_exploration.py
│   │   ├── exp2a_numpy.py
│   │   ├── exp2b_pandas.py
│   │   ├── exp2c_reading_data.py
│   │   ├── exp2d_iris_descriptive.py
│   │   ├── exp3a_univariate_diabetes.py
│   │   ├── exp3b_bivariate_regression.py
│   │   ├── exp3c_multiple_regression.py
│   │   ├── exp3d_comparison.py
│   │   ├── exp4a_normal_curves.py
│   │   ├── exp4b_ztest.py
│   │   ├── exp4c_ttest.py
│   │   ├── exp4d_anova.py
│   │   ├── exp5a_linear_model_validation.py
│   │   ├── exp5b_logistic_model_validation.py
│   │   ├── exp5c_time_series_analysis.py
│   │   └── generate_lab_submission.py
│   └── utils/
│       ├── dataset_loader.py
│       ├── notebook_generator.py
│       └── __init__.py
└── davlab_portfolio_josep/
    ├── experiment_code_archive/
    │   ├── Exp1_exp1_exploration.py
    │   ├── Exp2A_exp2a_numpy.py
    │   └── ...
    └── experiment_output_archive/
        ├── Exp1/
        ├── Exp2A/
        ├── Exp2B/
        └── ...
```

---

## Main Folders

### src/
Contains the working Python experiment scripts used for analysis and execution.

### data/
Stores all raw and processed datasets including CSV, Excel, and generated plots.

### davlab_portfolio_josep/experiment_code_archive/
Contains a clean copy of each experiment file saved as a submission-ready archive.

### davlab_portfolio_josep/experiment_output_archive/
Contains output text files for each experiment, kept separate from the code archive.

---

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run a specific experiment:

```bash
python src/experiments/exp2a_numpy.py
python src/experiments/exp2b_pandas.py
python src/experiments/exp3a_univariate_diabetes.py
```

Or run the archive generator:

```bash
python src/experiments/generate_lab_submission.py
```

---

## Experiments Included

- Exp1: Exploration and environment setup
- Exp2A: NumPy operations
- Exp2B: Pandas DataFrames
- Exp2C: Reading data from multiple sources
- Exp2D: Iris descriptive analysis
- Exp3A: Univariate diabetes analysis
- Exp3B: Bivariate regression
- Exp3C: Multiple regression
- Exp3D: Comparison analysis
- Exp4A: Normal curves
- Exp4B: Z-test
- Exp4C: T-test
- Exp4D: ANOVA
- Exp5A: Linear model validation
- Exp5B: Logistic model validation
- Exp5C: Time series analysis

---

## Notes

This repository was structured to keep code and outputs separated for a cleaner portfolio and assignment submission.

The project is ready for GitHub publishing and version control.
