# DAV Lab Experiments – Data Analysis and Visualization

## Overview

This repository contains **16 Python experiments** covering the full spectrum of Data Analysis and Visualization (DAV) techniques. The experiments are organized into five groups (Experiments 1 through 5), progressing from environment setup and basic NumPy/Pandas operations all the way to regression modeling, statistical hypothesis testing, and time series forecasting. All programs use real-world and synthetic datasets with libraries such as **NumPy**, **Pandas**, **Matplotlib**, **Seaborn**, **SciPy**, **Statsmodels**, and **Scikit-learn**.

---

## Repository Structure

```
DAV_Lab_Experiments/
├── Experiment_1/          # Environment setup & library installation
├── Experiment_2a/         # NumPy arrays and operations
├── Experiment_2b/         # Pandas DataFrame operations
├── Experiment_2c/         # Data preprocessing with text/mixed datasets
├── Experiment_2d/         # EDA on Iris dataset using Seaborn
├── Experiment_3a/         # Univariate analysis on Iris dataset
├── Experiment_3b/         # Bivariate analysis – Linear & Logistic Regression
├── Experiment_3c/         # Multiple Regression Analysis
├── Experiment_3d/         # Comparison of analysis results
├── Experiment_4a/         # Data Visualization – Normal Curves
├── Experiment_4b/         # Hypothesis Testing – Z-Test
├── Experiment_4c/         # Hypothesis Testing – T-Test
├── Experiment_4d/         # Hypothesis Testing – ANOVA
├── Experiment_5a/         # Model Building – Linear Regression Validation
├── Experiment_5b/         # Model Building – Logistic Regression Validation
└── Experiment_5c/         # Time Series Analysis & ARIMA Forecasting
```

---

## Experiment 1: Environment Setup and Library Installation

### Objective

Install and verify all required Python libraries for the Data Analysis and Visualization lab.

### Libraries Installed & Verified

| Library       | Purpose                            |
| ------------- | ---------------------------------- |
| NumPy         | Numerical computations             |
| Pandas        | Data manipulation and analysis     |
| Matplotlib    | Basic plotting                     |
| Seaborn       | Advanced statistical visualization |
| SciPy         | Statistical calculations           |
| Statsmodels   | Statistical models and tests       |
| Plotly        | Interactive visualizations         |
| Bokeh         | Interactive web-based plots        |
| Jupyter       | Interactive notebook environment   |

### Operations Performed

* Install all required libraries using `pip`
* Import each library and print its version number to confirm successful installation

### Learning Outcome

Students set up the complete Python data science environment and confirm that all libraries are available for subsequent experiments.

---

## Experiment 2A: NumPy Arrays and Operations

### Objective

Understand the NumPy library by creating different types of arrays and performing element-wise operations, indexing, and slicing.

### Libraries Used

* NumPy

### Operations Performed

* Create 0-D, 1-D, and 2-D arrays
* Array indexing and slicing
* Element-wise arithmetic operations (addition, subtraction, multiplication, division)
* Special array creation: `ones`, `zeros`, `arange`
* Print NumPy version

### Key Concepts

* **ndarray**: NumPy's core N-dimensional array object
* **Broadcasting**: Automatic element-wise operations between arrays of different shapes
* **Vectorization**: Performing operations on entire arrays without explicit loops

### Learning Outcome

Students understand NumPy array creation, manipulation, and the concept of vectorized computation.

---

## Experiment 2B: Pandas DataFrame Operations

### Objective

Explore the Pandas library by creating synthetic DataFrames and performing essential data manipulation operations.

### Libraries Used

* Pandas
* NumPy

### Dataset

Synthetic dataset (100 rows) generated using `numpy.random` with numeric and categorical columns.

### Operations Performed

* Create a DataFrame from a dictionary of NumPy arrays
* Display shape, data types, and basic info
* Add and modify columns
* Filter rows using boolean conditions
* Group by a categorical column and aggregate
* Apply string operations to text columns
* Handle missing values (fill and drop)
* Export the DataFrame to CSV

### Learning Outcome

Students master the core Pandas DataFrame API for creating, exploring, transforming, and exporting tabular data.

---

## Experiment 2C: Data Preprocessing with Mixed Datasets

### Objective

Perform data preprocessing on mixed (numeric and text) synthetic datasets, mimicking real-world data ingestion scenarios.

### Libraries Used

* Pandas
* NumPy

### Dataset

Synthetic dataset (50 rows) with text columns and numerical columns; intentional `NaN` values are introduced.

### Operations Performed

* Generate and load a synthetic text/mixed dataset
* Detect and count missing values
* Apply Forward Fill (`ffill`) and Backward Fill (`bfill`) strategies
* Drop rows/columns with missing values
* Perform string extraction and transformation on text columns
* Merge or join multiple DataFrames

### Learning Outcome

Students learn robust data cleaning techniques for mixed-type datasets, including filling strategies and string manipulation.

---

## Experiment 2D: Exploratory Data Analysis on the Iris Dataset

### Objective

Perform Exploratory Data Analysis (EDA) on the classic Iris dataset using Seaborn and Matplotlib to understand feature distributions and species relationships.

### Libraries Used

* Pandas
* Seaborn
* Matplotlib
* Scikit-learn (`load_iris`)

### Dataset

**Iris Dataset** — 150 samples, 4 numerical features (sepal length, sepal width, petal length, petal width), 3 species classes.

### Operations Performed

* Load the Iris dataset from `sklearn.datasets`
* Display basic information and summary statistics
* Count species distribution
* Generate feature histograms
* Boxplot: Sepal Length by species
* Pairplot to visualize all pairwise feature relationships colored by species

### Visualizations

| Plot         | Purpose                                      |
| ------------ | -------------------------------------------- |
| Histograms   | Feature distribution per attribute           |
| Boxplot      | Sepal Length distribution across species     |
| Pairplot     | All pairwise feature relationships by class  |

### Learning Outcome

Students gain hands-on experience with EDA on a classic multi-class dataset and learn to extract visual insights from feature distributions.

---

## Experiment 3A: Univariate Analysis on the Iris Dataset

### Objective

Perform Univariate Statistical Analysis on the Iris dataset, examining each feature independently through descriptive statistics and visualizations.

### Libraries Used

* Pandas
* Seaborn
* Matplotlib
* Scikit-learn (`load_iris`)

### Dataset

Iris Dataset (via `sklearn.datasets.load_iris`)

### Statistical Analysis Performed

* Species count (value counts)
* Descriptive statistics (`describe()`)
* Distribution of each numerical feature

### Visualizations

* Feature distribution histograms (all 4 features)
* Boxplot for Sepal Length comparison across species
* Pairplot for multi-feature overview

### Learning Outcome

Students understand univariate analysis techniques and how individual feature statistics vary across classes.

---

## Experiment 3B: Bivariate Analysis – Linear & Logistic Regression

### Objective

Perform Bivariate Analysis on the UCI Diabetes and Pima Indians Diabetes datasets using both Linear Regression and Logistic Regression.

### Libraries Used

* Pandas, NumPy, Seaborn, Matplotlib
* Scikit-learn (`LinearRegression`, `LogisticRegression`, `train_test_split`, `r2_score`, `accuracy_score`)

### Datasets

* UCI Diabetes Dataset (`uci_diabetes.csv`)
* Pima Indians Diabetes Dataset (`pima_diabetes.csv`)

### Analysis Performed

#### Linear Regression (Glucose → BMI)

* Fits a simple linear regression model
* Computes **R² Score**
* Scatter plot overlaid with regression line

#### Logistic Regression (Predicting Diabetes Outcome)

* Features: Glucose, BloodPressure, BMI, Age
* Target: Outcome (0 = No Diabetes, 1 = Diabetes)
* 80/20 train-test split
* Computes **Accuracy Score**

### Functions Used

| Function               | Description                               |
| ---------------------- | ----------------------------------------- |
| `LinearRegression()`   | Fits a linear model to the data           |
| `LogisticRegression()` | Fits a logistic model for classification  |
| `train_test_split()`   | Splits data into training/testing sets    |
| `r2_score()`           | Evaluates regression model quality        |
| `accuracy_score()`     | Evaluates classification accuracy         |

### Learning Outcome

Students understand the distinction between regression and classification, apply both models to real datasets, and evaluate their performance.

---

## Experiment 3C: Multiple Regression Analysis

### Objective

Perform Multiple Linear Regression on both diabetes datasets to predict BMI using multiple independent variables.

### Libraries Used

* Pandas, NumPy, Matplotlib
* Scikit-learn (`LinearRegression`, `train_test_split`, `r2_score`)

### Datasets

* UCI Diabetes Dataset
* Pima Indians Diabetes Dataset

### Model Details

* **Features (X):** Glucose, BloodPressure, Age
* **Target (y):** BMI
* **Split:** 80% training / 20% testing
* **Metric:** R² Score

### Operations Performed

* Load both datasets
* Select features and target variable
* Split into training and test sets
* Train `LinearRegression` model on each dataset
* Predict on test set and compute R² Score

### Learning Outcome

Students understand how multiple predictors are used simultaneously in a regression model and compare model performance across two related datasets.

---

## Experiment 3D: Comparison of Analysis Results

### Objective

Compare the statistical analysis results (Univariate, Bivariate, and Multiple Regression) between the UCI Diabetes Dataset and the Pima Indians Diabetes Dataset.

### Libraries Used

* Pandas, NumPy

### Datasets

* UCI Diabetes Dataset
* Pima Indians Diabetes Dataset

### Comparisons Made

* **Univariate statistics**: Summary statistics from both datasets side by side
* **Linear Regression R² Scores**: UCI vs. Pima performance
* **Logistic Regression Accuracy**: UCI vs. Pima classification performance

### Key Results (Example Values)

| Metric                   | UCI Dataset | Pima Dataset |
| ------------------------ | ----------- | ------------ |
| Linear Regression R²     | 0.78        | 0.72         |
| Logistic Regression Acc. | 82.4%       | 79.1%        |

### Learning Outcome

Students develop the ability to critically compare analytical results across datasets and interpret model performance differences.

---

## Experiment 4A: Data Visualization – Normal Curves

### Objective

Visualize the distribution of key numerical attributes in the UCI Diabetes dataset by overlaying normal distribution curves on histograms.

### Libraries Used

* Pandas, NumPy, Matplotlib, Seaborn
* SciPy (`scipy.stats.norm`)

### Dataset

UCI Diabetes Dataset

### Visualizations Generated

| Plot                     | Description                                    |
| ------------------------ | ---------------------------------------------- |
| Histogram + KDE + Normal | Glucose distribution with normal curve overlay |
| Histogram + KDE + Normal | BMI distribution with normal curve overlay     |

### Operations Performed

* Plot histograms with KDE for Glucose and BMI
* Compute theoretical normal PDF using `scipy.stats.norm.pdf`
* Overlay the normal curve on each histogram for comparison

### Learning Outcome

Students understand how to assess normality of data distributions visually and compare empirical distributions to theoretical normal curves.

---

## Experiment 4B: Hypothesis Testing – Z-Test

### Objective

Perform a Z-Test on the UCI Diabetes dataset to determine whether the mean Glucose level significantly differs from a specified population mean.

### Libraries Used

* Pandas, NumPy
* Statsmodels (`statsmodels.stats.weightstats.ztest`)

### Dataset

UCI Diabetes Dataset

### Hypothesis

* **H₀ (Null Hypothesis):** Mean Glucose = 100
* **H₁ (Alternative Hypothesis):** Mean Glucose ≠ 100
* **Significance Level (α):** 0.05

### Operations Performed

* Perform one-sample Z-Test on the Glucose column
* Compute Z-Statistic and P-Value
* Interpret the result against the significance level

### Interpretation

* If `p_value < 0.05` → Reject H₀ (Glucose mean is significantly different from 100)
* If `p_value ≥ 0.05` → Fail to reject H₀

### Learning Outcome

Students understand the Z-Test procedure, the concept of hypothesis testing, significance levels, and how to interpret p-values in a medical data context.

---

## Experiment 4C: Hypothesis Testing – T-Test

### Objective

Perform an Independent Samples T-Test to compare the means of numerical variables between the UCI Diabetes and Pima Indians Diabetes datasets and determine statistical significance.

### Libraries Used

* Pandas, NumPy
* SciPy (`scipy.stats.ttest_ind`)

### Datasets

* UCI Diabetes Dataset
* Pima Indians Diabetes Dataset

### Variables Tested

* Glucose
* BloodPressure
* BMI

### Operations Performed

* Apply Welch's T-Test (unequal variance) for each numerical column
* Compute T-Statistic and P-Value for each variable
* Display results as a formatted DataFrame

### Interpretation

* If `p_value < 0.05` → Significant difference between the two datasets for that variable
* If `p_value ≥ 0.05` → No significant difference

### Learning Outcome

Students learn to apply independent samples T-Tests to compare two population means and interpret whether differences are statistically significant.

---

## Experiment 4D: Hypothesis Testing – ANOVA

### Objective

Perform One-Way ANOVA (Analysis of Variance) on the UCI and Pima Indians Diabetes datasets to test for statistically significant differences in group means across multiple numerical attributes.

### Libraries Used

* Pandas, NumPy
* SciPy (`scipy.stats.f_oneway`)

### Datasets

* UCI Diabetes Dataset
* Pima Indians Diabetes Dataset

### Variables Tested

* Glucose
* BloodPressure
* BMI

### Operations Performed

* Apply One-Way ANOVA for each numerical column comparing UCI vs. Pima groups
* Compute F-Statistic and P-Value for each variable
* Display results as a formatted DataFrame

### Interpretation

* If `p_value < 0.05` → Significant difference between group means (reject H₀)
* If `p_value ≥ 0.05` → No significant difference between group means

### Learning Outcome

Students understand ANOVA as a generalization of the T-Test for comparing more than two groups, and can identify which variables differ significantly between datasets.

---

## Experiment 5A: Model Building – Linear Regression Validation

### Objective

Build and validate Linear Regression Models on both diabetes datasets, evaluating their predictive accuracy using multiple performance metrics.

### Libraries Used

* Pandas, NumPy, Matplotlib, Seaborn
* Scikit-learn (`LinearRegression`, `train_test_split`, `r2_score`, `mean_squared_error`, `mean_absolute_error`)

### Datasets

* UCI Diabetes Dataset
* Pima Indians Diabetes Dataset

### Model Details

* **Features (X):** Glucose, BloodPressure, BMI
* **Target (y):** Age
* **Split:** 80% training / 20% testing (`random_state=42`)

### Performance Metrics

| Metric                    | Description                                         |
| ------------------------- | --------------------------------------------------- |
| R² Score                  | Proportion of variance explained by the model       |
| Mean Squared Error (MSE)  | Average squared difference between actual/predicted |
| Mean Absolute Error (MAE) | Average absolute difference between actual/predicted|

### Operations Performed

* Prepare features and target for both datasets
* Split data into training and testing sets
* Train separate `LinearRegression` models for UCI and Pima datasets
* Predict on test set and compute R², MSE, and MAE
* Print a comprehensive results summary

### Learning Outcome

Students learn to validate regression models using multiple performance metrics and understand the trade-offs between different evaluation criteria.

---

## Experiment 5B: Model Building – Logistic Regression Validation

### Objective

Build and validate Logistic Regression Models to predict diabetes presence (Outcome), evaluating classification performance with multiple metrics and confusion matrices.

### Libraries Used

* Pandas, NumPy, Matplotlib, Seaborn
* Scikit-learn (`LogisticRegression`, `train_test_split`, `accuracy_score`, `precision_score`, `recall_score`, `f1_score`, `confusion_matrix`)

### Datasets

* UCI Diabetes Dataset
* Pima Indians Diabetes Dataset

### Model Details

* **Features (X):** Glucose, BloodPressure, BMI
* **Target (y):** Outcome (binary: 0 = No Diabetes, 1 = Diabetes)
* **Split:** 80% training / 20% testing

### Performance Metrics

| Metric    | Description                                         |
| --------- | --------------------------------------------------- |
| Accuracy  | Fraction of correct predictions                     |
| Precision | True positives / (True positives + False positives) |
| Recall    | True positives / (True positives + False negatives) |
| F1 Score  | Harmonic mean of Precision and Recall               |

### Visualizations

* **Confusion Matrix Heatmaps** for both UCI and Pima datasets (side-by-side)

### Learning Outcome

Students learn comprehensive classification model evaluation using accuracy, precision, recall, F1 score, and confusion matrix visualization.

---

## Experiment 5C: Time Series Analysis & ARIMA Forecasting

### Objective

Perform Time Series Analysis on glucose-level data, identifying trends, seasonality, and residuals, followed by ARIMA-based forecasting.

### Libraries Used

* Pandas, NumPy, Matplotlib, Seaborn
* Statsmodels (`seasonal_decompose`, `ARIMA`)

### Dataset

`diabetes9.csv` — A time-series dataset with a `Glucose` column representing glucose levels over time.

### Operations Performed

1. **Load and Preview** — Read the dataset and display the first few rows
2. **Plot Time Series** — Visualize raw Glucose levels over index
3. **Seasonal Decomposition** — Decompose into Trend, Seasonal, and Residual components using `seasonal_decompose` (additive model, period=30)
4. **Moving Average Smoothing** — Apply a 7-day rolling mean to smooth the series
5. **ARIMA Modeling** — Fit an ARIMA(5,1,0) model on the training set (80% of data)
6. **Forecasting** — Forecast Glucose levels for the remaining 20% and compare against actuals

### Visualizations Generated

| Plot                       | Description                                |
| -------------------------- | ------------------------------------------ |
| Raw Time Series            | Original Glucose level over time           |
| Decomposition (3 subplots) | Trend, Seasonal, and Residual components   |
| Moving Average             | Original vs. 7-day smoothed Glucose levels |
| Forecast vs. Actual        | ARIMA predictions vs. true test values     |

### Learning Outcome

Students gain practical skills in time series decomposition, smoothing techniques, and ARIMA-based forecasting for sequential biomedical data.

---

## Libraries Summary

| Library      | Purpose                                        |
| ------------ | ---------------------------------------------- |
| NumPy        | Numerical arrays and mathematical operations   |
| Pandas       | Data loading, manipulation, and analysis       |
| Matplotlib   | Basic and custom static plotting               |
| Seaborn      | Statistical visualizations and heatmaps        |
| SciPy        | Statistical tests (Z, T, ANOVA, normal PDF)    |
| Statsmodels  | Z-Test, Time Series (ARIMA, decomposition)     |
| Scikit-learn | Machine learning models and metrics            |
| Plotly       | Interactive charts                             |
| Bokeh        | Interactive web-based visualizations           |

---

## Visualization Techniques Used Across All Experiments

| Visualization            | Experiment(s) | Purpose                                   |
| ------------------------ | ------------- | ----------------------------------------- |
| Histogram                | 2D, 3A, 4A   | Feature distribution                      |
| Boxplot                  | 2D, 3A       | Spread and outlier detection              |
| Pairplot                 | 2D, 3A       | Pairwise feature relationships            |
| Scatter + Regression     | 3B           | Linear relationship visualization         |
| Confusion Matrix Heatmap | 5B           | Classification performance                |
| Normal Curve Overlay     | 4A           | Distribution normality assessment         |
| Time Series Plot         | 5C           | Glucose trends over time                  |
| Decomposition Plot       | 5C           | Trend, seasonal, and residual components  |
| Moving Average Plot      | 5C           | Smoothed signal visualization             |
| ARIMA Forecast Plot      | 5C           | Predicted vs. actual glucose levels       |

---

## Overall Learning Outcomes

By completing all 16 experiments, students will be able to:

* Set up a complete Python data science environment with all essential libraries.
* Create and manipulate NumPy arrays with vectorized operations.
* Load, clean, filter, sort, group, and export data using Pandas.
* Perform Exploratory Data Analysis (EDA) on real-world datasets (Iris, Diabetes).
* Conduct Univariate and Bivariate statistical analysis.
* Build and evaluate Linear and Logistic Regression models.
* Perform Multiple Regression and compare model performance across datasets.
* Apply formal hypothesis testing techniques: Z-Test, T-Test, and ANOVA.
* Visualize normal distributions and assess data normality.
* Decompose time series data into trend, seasonal, and residual components.
* Build ARIMA forecasting models and evaluate forecast accuracy.
* Interpret all statistical metrics: R², MSE, MAE, Accuracy, Precision, Recall, F1, p-value.

---

# Program 1: Pandas Data Manipulation and Basic Visualization

## Objective

The objective of this program is to understand the basic operations of the Pandas library, including reading datasets, handling missing values, filtering data, sorting, grouping, creating new columns, exporting processed data, and generating simple visualizations.

### Libraries Used

* Pandas
* NumPy
* Matplotlib

### Operations Performed

* Read CSV file
* Display first and last records
* Display dataset information
* Generate descriptive statistics
* Handle missing values
* Create a new column
* Perform Series operations
* Filter rows using conditions
* Group data and calculate mean values
* Sort records
* Apply Boolean masking
* Remove duplicate rows
* Remove missing values
* Create a subset of selected columns
* Export processed data into a CSV file
* Calculate Sum, Mean and Standard Deviation

### Visualizations

* Bar Chart
* Line Chart

### Functions Used

| Function          | Description                   |
| ----------------- | ----------------------------- |
| read_csv()        | Reads CSV dataset             |
| head()            | Displays first five rows      |
| tail()            | Displays last five rows       |
| info()            | Displays dataset information  |
| describe()        | Generates statistical summary |
| fillna()          | Fills missing values          |
| groupby()         | Groups data                   |
| sort_values()     | Sorts data                    |
| drop_duplicates() | Removes duplicate records     |
| dropna()          | Removes missing values        |
| to_csv()          | Saves processed dataset       |

### Learning Outcome

After completing this program, students will be able to:

* Import datasets
* Clean datasets
* Filter and sort data
* Perform aggregation
* Export processed data
* Create basic graphs

---

# Program 2: Importing Data from Multiple Sources

## Objective

This program demonstrates how to import data from different sources such as CSV files, Excel files, and online datasets.

### Libraries Used

* Pandas

### Data Sources

* CSV File
* Excel File
* Online Dataset (GitHub URL)

### Operations Performed

* Read CSV file
* Read Excel file
* Read data from URL
* Display datasets
* Handle missing values using Forward Fill
* Handle missing values using Backward Fill
* Remove missing records
* Save processed CSV file
* Save processed Excel file

### Functions Used

| Function     | Description                   |
| ------------ | ----------------------------- |
| read_csv()   | Reads CSV files               |
| read_excel() | Reads Excel files             |
| ffill()      | Forward fills missing values  |
| bfill()      | Backward fills missing values |
| dropna()     | Removes missing values        |
| to_csv()     | Saves CSV file                |
| to_excel()   | Saves Excel file              |

### Learning Outcome

Students learn how to:

* Import datasets from different formats
* Handle missing values
* Export cleaned datasets
* Work with online datasets

---

# Program 3: Exploratory Data Analysis Using Titanic Dataset

## Objective

The objective of this program is to perform Exploratory Data Analysis (EDA) on the Titanic dataset and understand relationships among different passenger attributes using statistical analysis and visualization.

### Dataset

Titanic Passenger Dataset

### Libraries Used

* Pandas
* Seaborn
* Matplotlib

### Dataset Analysis

The program displays:

* First and last records
* Dataset dimensions
* Column names
* Data types
* Missing values
* Duplicate records
* Statistical summary

### Statistical Analysis

The following analyses are performed:

* Passenger survival count
* Gender distribution
* Passenger class distribution
* Embarked port distribution
* Average fare by passenger class
* Average age by gender
* Average fare based on survival
* Correlation matrix
* Highest fare passengers
* Oldest passengers

### Visualizations

The program generates the following plots:

1. Survival Count Plot
2. Gender Distribution Plot
3. Passenger Class Distribution
4. Age Histogram
5. Fare Histogram
6. Fare Box Plot by Passenger Class
7. Age vs Fare Scatter Plot
8. Age Distribution by Survival (Violin Plot)
9. Average Fare by Passenger Class (Bar Plot)
10. Correlation Heatmap
11. Pair Plot

### Functions Used

| Function      | Description                          |
| ------------- | ------------------------------------ |
| countplot()   | Displays frequency counts            |
| histplot()    | Displays histogram                   |
| boxplot()     | Shows outliers and spread            |
| violinplot()  | Shows density and distribution       |
| scatterplot() | Shows relationship between variables |
| barplot()     | Displays average values              |
| heatmap()     | Displays correlation matrix          |
| pairplot()    | Compares multiple variables          |

### Learning Outcome

Students understand:

* Exploratory Data Analysis
* Feature relationships
* Correlation analysis
* Distribution analysis
* Data visualization techniques

---

# Program 4: Univariate Statistical Analysis Using Pima Indians Diabetes Dataset

## Objective

The objective of this program is to perform univariate statistical analysis on numerical attributes of the Pima Indians Diabetes dataset.

### Dataset

Pima Indians Diabetes Dataset

### Libraries Used

* Pandas
* NumPy
* SciPy

### Numerical Features

* Glucose
* Blood Pressure
* Skin Thickness
* Insulin
* BMI
* Diabetes Pedigree Function
* Age

### Statistical Measures Calculated

* Mean
* Median
* Mode
* Minimum
* Maximum
* Range
* Variance
* Standard Deviation
* Skewness
* Kurtosis

### Additional Analysis

* Outcome distribution
* Correlation matrix

### Statistical Terms

**Mean**

Average value of the dataset.

**Median**

Middle value after arranging the observations.

**Mode**

Most frequently occurring value.

**Variance**

Measures how much the data varies from the mean.

**Standard Deviation**

Measures the spread of observations around the mean.

**Skewness**

Measures the symmetry of the distribution.

* Positive → Right-skewed
* Negative → Left-skewed
* Zero → Symmetric

**Kurtosis**

Measures the peakedness of the distribution.

* Positive → Heavy tails
* Negative → Light tails
* Zero → Normal distribution

### Learning Outcome

Students learn:

* Descriptive statistics
* Statistical analysis
* Healthcare data analysis
* Data interpretation
* Correlation analysis

---

# Libraries Used

| Library    | Purpose                            |
| ---------- | ---------------------------------- |
| Pandas     | Data manipulation and analysis     |
| NumPy      | Numerical computations             |
| Matplotlib | Basic plotting                     |
| Seaborn    | Advanced statistical visualization |
| SciPy      | Statistical calculations           |

---

# Common Pandas Functions

| Function          | Purpose                  |
| ----------------- | ------------------------ |
| read_csv()        | Import CSV file          |
| read_excel()      | Import Excel file        |
| head()            | Display first records    |
| tail()            | Display last records     |
| info()            | Dataset information      |
| describe()        | Statistical summary      |
| groupby()         | Group data               |
| sort_values()     | Sort records             |
| fillna()          | Fill missing values      |
| dropna()          | Remove missing values    |
| drop_duplicates() | Remove duplicate records |
| value_counts()    | Frequency count          |
| corr()            | Correlation matrix       |
| to_csv()          | Export CSV               |
| to_excel()        | Export Excel             |

---

# Visualization Techniques

| Visualization | Purpose                                                   |
| ------------- | --------------------------------------------------------- |
| Histogram     | Displays numerical data distribution                      |
| Bar Plot      | Compares categories                                       |
| Count Plot    | Shows frequency of categories                             |
| Scatter Plot  | Shows relationship between numerical variables            |
| Box Plot      | Detects outliers and spread                               |
| Violin Plot   | Shows density and distribution                            |
| Heatmap       | Displays correlation matrix                               |
| Pair Plot     | Compares relationships among multiple numerical variables |

---

# Overall Learning Outcomes

By completing these four programs, students will be able to:

* Import datasets from CSV, Excel, and online sources.
* Clean and preprocess datasets.
* Handle missing values and duplicate records.
* Perform descriptive statistical analysis.
* Filter, sort, group, and aggregate data using Pandas.
* Export processed datasets into CSV and Excel formats.
* Perform Exploratory Data Analysis (EDA) on real-world datasets.
* Generate professional visualizations using Matplotlib and Seaborn.
* Interpret statistical measures such as mean, median, mode, variance, standard deviation, skewness, and kurtosis.
* Analyze relationships among variables using correlation matrices, scatter plots, heatmaps, and pair plots.
* Apply data analysis techniques to business, healthcare, finance, research, and machine learning datasets.
