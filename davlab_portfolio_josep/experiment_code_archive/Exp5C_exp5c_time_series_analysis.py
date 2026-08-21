"""
Experiment 5C: Time Series Analysis
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.arima.model import ARIMA

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PIMA_DIABETES_PATH = os.path.join(BASE_DIR, "data", "raw", "pima_diabetes.csv")
PLOTS_DIR = os.path.join(BASE_DIR, "data", "processed", "plots")


def run_experiment_5c():
    print("==================================================")
    print("EXPERIMENT 5C: TIME SERIES ANALYSIS")
    print("==================================================")

    if not os.path.exists(PIMA_DIABETES_PATH):
        from src.utils.dataset_loader import load_all_datasets

        load_all_datasets()

    os.makedirs(PLOTS_DIR, exist_ok=True)

    diabetes_data = pd.read_csv(PIMA_DIABETES_PATH)

    print("Dataset Head:")
    print(diabetes_data.head())

    # Time series line plot
    ts_plot = os.path.join(PLOTS_DIR, "exp5c_timeseries_glucose.png")
    plt.figure(figsize=(12, 4))
    plt.plot(diabetes_data["Glucose"], label="Glucose Level", color="blue")
    plt.xlabel("Index")
    plt.ylabel("Glucose")
    plt.title("Time Series of Glucose Levels")
    plt.legend()
    plt.tight_layout()
    plt.savefig(ts_plot)
    plt.close()

    # Seasonal decomposition
    decompose_plot = os.path.join(PLOTS_DIR, "exp5c_seasonal_decompose.png")
    decomposition = seasonal_decompose(diabetes_data["Glucose"], model="additive", period=30)
    fig = decomposition.plot()
    fig.set_size_inches(12, 8)
    fig.tight_layout()
    fig.savefig(decompose_plot)
    plt.close(fig)

    # Moving average and ARIMA forecast
    diabetes_data["Glucose_MA"] = diabetes_data["Glucose"].rolling(window=7).mean()
    train_size = int(len(diabetes_data) * 0.8)
    train = diabetes_data["Glucose"][:train_size]
    test = diabetes_data["Glucose"][train_size:]

    model = ARIMA(train, order=(2, 1, 2))
    fitted_model = model.fit()
    forecast = fitted_model.forecast(steps=len(test))

    forecast_plot = os.path.join(PLOTS_DIR, "exp5c_moving_avg_and_forecast.png")
    plt.figure(figsize=(12, 5))
    plt.plot(diabetes_data["Glucose"], label="Original", alpha=0.4)
    plt.plot(diabetes_data["Glucose_MA"], label="7-point Moving Average", color="red")
    plt.legend()
    plt.title("Moving Average Smoothing")
    plt.tight_layout()
    plt.savefig(forecast_plot)
    plt.close()

    arima_plot = os.path.join(PLOTS_DIR, "exp5c_arima_forecast.png")
    plt.figure(figsize=(12, 5))
    plt.plot(range(len(test)), test.values, label="Actual", color="blue")
    plt.plot(range(len(test)), forecast.values, label="Forecast", color="orange")
    plt.xlabel("Index")
    plt.ylabel("Glucose")
    plt.title("ARIMA Forecast vs Actual")
    plt.legend()
    plt.tight_layout()
    plt.savefig(arima_plot)
    plt.close()

    print(f"Saved plot: {ts_plot}")
    print(f"Saved plot: {decompose_plot}")
    print(f"Saved plot: {forecast_plot}")
    print(f"Saved plot: {arima_plot}")


if __name__ == "__main__":
    run_experiment_5c()
