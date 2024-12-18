# Telecom Customer Churn Prediction
This project predicts customer churn in a telecom company using machine learning. The application is built with Flask and uses a pre-trained Random Forest model to classify customers as Churners or Non-Churners based on their demographic and service-related information.

## Features
Web Interface: Simple UI for entering customer data.
Prediction: Classifies customer churn using a trained machine learning model.
Preprocessing: Imbalanced dataset handled using SMOTE; features engineered with Pandas and Numpy.
Model: RandomForest Classifier with hyperparameter tuning via RandomizedSearchCV.

## Getting Started
### Prerequisites
Python 3.x
Flask
Required libraries: numpy, pandas, matplotlib, sklearn

## Input Fields
Tenure: Number of months the customer has stayed with the company.
MonthlyCharges: Monthly charges incurred by the customer.
TotalCharges: Total charges incurred by the customer.
Demographic and Service Details: Includes Gender, Senior Citizen, Partner, Dependents, PhoneService, etc.

## Output
* Non-Churner: The customer is likely to stay with the company.
"*" Churner: The customer is likely to leave the company.

## Data and Model Details
"*" Data Collection and Preprocessing:
  "*" Performed using Numpy, Pandas, and Matplotlib.
  "*" Handled missing values and outliers during preprocessing.
  "*" Balanced the dataset using SMOTE (Synthetic Minority Over-sampling Technique) to address class imbalance.

"*" Model:

RandomForest Classifier was utilized for prediction.
Hyperparameters were optimized using RandomizedSearchCV for better accuracy and generalization.
The trained model is saved as model.pkl.
Files in the Repository
app.py: Flask application handling the backend logic.
model.pkl: Pre-trained machine learning model for predictions.
Telcom-churn.ipynb: Jupyter Notebook used for training and evaluating the model.
templates/homepage.html: HTML file for the web interface (not provided in this repository but required for functionality).

