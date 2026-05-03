# CREAM-SALES-USING-SARIMA-MODEL-BY-MUNEEB-12-3-1-020-2025
#  Ice Cream Sales Prediction using SARIMA Model

##  About the Project
This project is related to prediction of monthly ice cream sales.
The project uses Python based SARIMA (Seasonal ARIMA) Model to forecast ice cream sales in next 12 months.

SARIMA Model takes into account:
- Trends
- Seasonal Patterns
- Monthly differences

This information is useful for businesses for planning their production, inventory and marketing.

---

##  Objectives of the Project
- Prediction of future monthly sales of ice cream
- Analysis of the seasonal effect on sales of ice cream
- Long-term sales trend study

---

##  Programming languages and Tools
- Python
- Pandas
- NumPy
- Matplotlib
- Statsmodels (ARIMA / SARIMA)
- Scikit-learn

---

##  Technical Details of the Model
- Model Used: SARIMA
- ARIMA Order: (2,1,2)
- Seasonal Order: (1,1,1,12)

Above mentioned model order was selected as best fit for the dataset.

---

##  Working of the Model

### 1. Data Collection
- Used ice cream sales data
- Column Name: Date, Units Sold

### 2. Data Preprocessing
- Sorting of data according to date
- Date is used as an index
- Check for null values

### 3. Model Building
- SARIMA model built using ARIMA function
- Training of model with data

### 4. Prediction
- Predict sales in next 12 months

### 5. Model Evaluation
- R² Score
- Mean Squared Error (MSE)

### 6. Visualization of Result
- Plot of Sales
- Predicted data by the Model
- Prediction for Next 12 Months

---

## Output of the Project
Project provides following results:
- Plot of historical sales data
-  Future forecast of 12 month
-  Evaluation Metrics of the model

---

##  Output Results Explanation
-  Black Line -> Actual Sales of Ice cream  
-  Orange Line -> Predicted Data  
-  Green Line -> Forecast data for Next 12 months

From above chart you can see that the model is able to capture both trend and seasonality in data.

---

##  File Structure of the Project
Project files:
- main.py -> Contains main code of the program
- ice_cream.csv -> Contains ice cream sales data 
- output.csv -> Contains future sales forecasted by the model
- Graphs produced by the program

---

##  Developed By
- Muhammad Muneeb (12-3-1-020-2025)

Department of Metallurgy and Material Engineering

---

##  Date of Submission
Monday, 4th May 2026

---

##  Cloud Storage Links
- Google Drive Link
- https://drive.google.com/drive/folders/139i8FQcd_kiP7KzkplH2tpwCeD92ZWo_?usp=sharing



##Conclusion
In this project we developed SARIMA model which is quite successful in predicting sales of the Ice Cream.
