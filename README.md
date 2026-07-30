# CS4503: Data Analytics and Visualization Lab Manual Solutions (Exp 1 to Exp 3-A)

This repository contains fully structured, modular Python scripts, executed Jupyter Notebooks, and datasets for **Experiments 1 through 3-A** as specified in the CS4503 Data Analytics and Visualization Lab Manual.

---

## 📁 Repository Architecture & Layering

The codebase is organized into modular layers to ensure maintainability, clear separation of concerns, and reproducible execution:

```text
DAV Assignment/
├── README.md                                  # Complete project documentation & Kaggle links
├── requirements.txt                            # Python package dependencies
├── data/
│   ├── raw/                                   # Downloaded/Generated raw datasets
│   │   ├── iris.csv                           # Iris Flower Dataset
│   │   ├── pima_diabetes.csv                  # Pima Indians Diabetes Dataset
│   │   ├── uci_diabetes.csv                   # UCI Diabetes Dataset
│   │   ├── Google_data.csv                    # Google Play Store Apps sample dataset
│   │   └── data_sample.xlsx                   # Sample Excel workbook (.xlsx)
│   └── processed/                             # Processed output files and plots
│       ├── filtered_data.csv                  # Subset export from Exp 2B
│       ├── processed_text.csv                 # Cleaned CSV export from Exp 2C
│       ├── processed_excel.xlsx               # Cleaned Excel export from Exp 2C
│       └── plots/                             # Saved visualizations from Exp 2D
│           ├── iris_histograms.png
│           ├── iris_sepal_length_boxplot.png
│           └── iris_pairplot.png
├── src/
│   ├── __init__.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── dataset_loader.py                  # Automated dataset downloader/generator
│   │   └── notebook_generator.py             # Jupyter notebook builder
│   └── experiments/
│       ├── __init__.py
│       ├── exp1_exploration.py               # Exp 1: Library Installation & Exploration
│       ├── exp2a_numpy.py                    # Exp 2A: NumPy Array Manipulations
│       ├── exp2b_pandas.py                   # Exp 2B: Pandas DataFrame Operations
│       ├── exp2c_reading_data.py             # Exp 2C: Multi-Source Data Ingestion
│       ├── exp2d_iris_descriptive.py         # Exp 2D: Iris Descriptive Analytics
│       └── exp3a_univariate_diabetes.py      # Exp 3A: Univariate Statistical Analysis
└── notebooks/
    ├── Exp1_Installation_and_Exploration.ipynb
    ├── Exp2A_NumPy_Arrays.ipynb
    ├── Exp2B_Pandas_DataFrames.ipynb
    ├── Exp2C_Reading_Data.ipynb
    ├── Exp2D_Iris_Descriptive_Analytics.ipynb
    └── Exp3A_Diabetes_Univariate_Analysis.ipynb
```

---

## 🔗 Dataset Information & Source Links

All datasets are automatically fetched or initialized via `src/utils/dataset_loader.py`. You can also manually access/download them from their original Kaggle / UCI repositories:

1. **Iris Dataset**:
   - **Kaggle Link**: [Iris Species Dataset on Kaggle](https://www.kaggle.com/datasets/uciml/iris)
   - **UCI ML Repository**: [UCI Iris Dataset](https://archive.ics.uci.edu/ml/datasets/iris)
2. **Pima Indians Diabetes Dataset**:
   - **Kaggle Link**: [Pima Indians Diabetes Database on Kaggle](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)
   - **UCI ML Repository**: [UCI Diabetes Dataset](https://archive.ics.uci.edu/ml/datasets/diabetes)
3. **UCI Diabetes Dataset**:
   - **Kaggle Link**: [Diabetes Dataset on Kaggle](https://www.kaggle.com/datasets/mathchi/diabetes-data-set)

---

## 🚀 How to Run the Experiments

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Download / Initialize Datasets
```bash
python -m src.utils.dataset_loader
```

### 3. Run Modular Python Experiments
Execute any experiment script directly:
```bash
python -m src.experiments.exp1_exploration
python -m src.experiments.exp2a_numpy
python -m src.experiments.exp2b_pandas
python -m src.experiments.exp2c_reading_data
python -m src.experiments.exp2d_iris_descriptive
python -m src.experiments.exp3a_univariate_diabetes
```

### 4. Open Interactive Jupyter Notebooks
Launch Jupyter Notebook to view pre-rendered interactive outputs:
```bash
jupyter notebook notebooks/
```

---

## 📊 Summary of Implemented Experiments & Outputs

### **Experiment 1: Installation and Exploration**
- **Objective**: Import and explore version information for core Data Science libraries: NumPy, SciPy, Jupyter/JupyterLab, Statsmodels, Pandas, Matplotlib, Seaborn, Plotly, Bokeh.
- **Script**: `src/experiments/exp1_exploration.py`
- **Notebook**: `notebooks/Exp1_Installation_and_Exploration.ipynb`

### **Experiment 2A: Working with NumPy Arrays**
- **Objective**: Implement 0D, 1D, 2D, and ones arrays; indexing, slicing, element-wise arithmetic, scalar operations, aggregations (sum, mean, std), boolean masking, fancy indexing, reshaping (1D to 2D), and structured arrays.
- **Script**: `src/experiments/exp2a_numpy.py`
- **Notebook**: `notebooks/Exp2A_NumPy_Arrays.ipynb`

### **Experiment 2B: Working with Pandas DataFrames**
- **Objective**: Perform data inspection (`head`, `tail`, `info`, `describe`), missing value imputation (`fillna`), column transformations, Series operations, multi-condition filtering, `groupby` aggregation, sorting, boolean masking, duplicate removal, and exporting subset files (`filtered_data.csv`).
- **Script**: `src/experiments/exp2b_pandas.py`
- **Notebook**: `notebooks/Exp2B_Pandas_DataFrames.ipynb`

### **Experiment 2C: Reading Data from Text Files, Excel, and Web**
- **Objective**: Read CSV files, Excel workbooks (`.xlsx`), and web datasets (raw GitHub URLs). Handle missing values with forward-fill (`ffill`), backward-fill (`bfill`), and `dropna`. Save processed files to `processed_text.csv` and `processed_excel.xlsx`.
- **Script**: `src/experiments/exp2c_reading_data.py`
- **Notebook**: `notebooks/Exp2C_Reading_Data.ipynb`

### **Experiment 2D: Exploring Descriptive Analytics Using Iris Dataset**
- **Objective**: Conduct descriptive analytics on the Iris dataset. Compute summary statistics and species value counts. Render feature distribution histograms, Sepal Length boxplots by species, and pairplots. Save plot images under `data/processed/plots/`.
- **Script**: `src/experiments/exp2d_iris_descriptive.py`
- **Notebook**: `notebooks/Exp2D_Iris_Descriptive_Analytics.ipynb`

### **Experiment 3-A: Statistical Analysis Using Diabetes Datasets - Univariate Analysis**
- **Objective**: Perform univariate statistical analysis on UCI Diabetes and Pima Indians Diabetes datasets across numerical features (`Glucose`, `BloodPressure`, `SkinThickness`, `Insulin`, `BMI`, `DiabetesPedigreeFunction`, `Age`). Compute **Mean**, **Median**, **Mode**, **Variance**, **Standard Deviation**, **Skewness**, and **Kurtosis**.
- **Script**: `src/experiments/exp3a_univariate_diabetes.py`
- **Notebook**: `notebooks/Exp3A_Diabetes_Univariate_Analysis.ipynb`
