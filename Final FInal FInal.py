import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import r2_score, mean_squared_error
import warnings

# Suppress warnings
warnings.filterwarnings("ignore")

# ============================================================
# 📌 1. LOAD DATA
# ============================================================
df = pd.read_csv("ice_cream.csv", parse_dates=["Date"])
df.set_index("Date", inplace=True)
df = df.sort_index()


print(df.head(10))

plt.figure(figsize=(15, 5))
plt.plot(df , color='blue', label='Original')
plt.title('Time series Graph')
plt.show()

# ============================================================
# 📌 2. TRAIN SARIMA MODEL (Full Data)
# ============================================================
# Train on ALL data to ensure the future forecast uses all history
arima_model = ARIMA(df['Units Sold'], order=(2,1,2), seasonal_order=(1,1,1,12))
arima_fit = arima_model.fit()

# ============================================================
# 📌 3. FUTURE FORECAST (Next 12 Months)
# ============================================================
future_months = 12
future_index = pd.date_range(df.index[-1] + pd.offsets.MonthBegin(1),
                             periods=future_months, freq='MS')

arima_forecast = arima_fit.forecast(steps=future_months)
arima_forecast.index = future_index


print("\n==================== NEXT 12-MONTH FORECASTS ====================\n")

print("📌 SARIMA Forecast:")
print(arima_forecast)


# ============================================================
# 📌 4. PREPARE DATA FOR PLOTTING & EVALUATION
# ============================================================
# Get model predictions for the past
fitted_values = arima_fit.fittedvalues

# Create a comparison dataframe
comparison_df = pd.DataFrame({
    'Actual': df['Units Sold'],
    'Predicted': fitted_values
})

# Filter: We only want to show the MODEL PREDICTION line starting from 2010
start_date = '2010-01-01'
prediction_subset = comparison_df[comparison_df.index >= start_date]

# ============================================================
# 📌 5. PLOTTING
# ============================================================
plt.figure(figsize=(14, 8))

# Plot 1: Actual Data (FULL HISTORY)
plt.plot(df.index, df['Units Sold'], label='Actual Sales (Full History)', color='black', linewidth=2)

# Plot 2: Model Predictions (From 2010 ONLY)
plt.plot(prediction_subset.index, prediction_subset['Predicted'], label='Model Prediction (Starting 2010)', color='orange', linestyle='--', linewidth=2)

# Plot 3: Future Forecast
plt.plot(arima_forecast.index, arima_forecast, label='Future Forecast (Next 12M)', color='green', marker='o', linestyle='--')

plt.title("Ice Cream Sales: Full History with Predictions from 2010", fontsize=14)
plt.xlabel("Date")
plt.ylabel("Units Sold")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# ============================================================
# 📌 6. MODEL EVALUATION (2010 Onwards)
# ============================================================
# We evaluate accuracy only where we showed the prediction line (2010+)
r2 = r2_score(prediction_subset['Actual'], prediction_subset['Predicted'])
mse = mean_squared_error(prediction_subset['Actual'], prediction_subset['Predicted'])


metrics_df = pd.DataFrame({
    "Metric": ["R2 Score", "MSE"],
    "Value": [r2, mse]
})

print("\n--- Model Accuracy (Evaluated on 2010-Present) ---")
print(metrics_df)

# Prdecting result by s[ecifing date

while True:
    user_input = input("\nEnter a date for prediction (YYYY-MM): ")
    target_date = pd.to_datetime(user_input)
    prediction_result = arima_fit.predict(start=target_date, end=target_date)
    print(prediction_result)
    check=input("\n Do you want to continue or not (y/n)").lower()
    if check !='y':
        break




# ============================================================
# 📌 7. EXPORT RESULTS
# ============================================================
# We combine the full history + future forecast for the export
# export_df = pd.concat([df[['Units Sold']], 
#                        arima_forecast.to_frame(name='Units Sold')])
# export_df.to_csv("ice_cream_final_forecast.csv", index=True)
# print("\nFile 'ice_cream_final_forecast.csv' exported successfully!")
