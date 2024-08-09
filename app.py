
from flask import Flask, render_template, request
import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

model = pickle.load(open('model1.pkl', 'rb'))
app = Flask(__name__,template_folder='templates')

@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/send', methods=['POST'])
def get_data():
    tenure = float(request.form.get('tenure'))
    MonthlyCharges = float(request.form.get('MonthlyCharges'))
    TotalCharges = float(request.form.get('TotalCharges'))
    gender = request.form.get('gender')
    SeniorCitizen = request.form.get('SeniorCitizen')
    Partner = request.form.get('Partner')
    Dependents = request.form.get('Dependents')
    PhoneService = request.form.get('PhoneService')
    MultipleLines = request.form.get('MultipleLines')
    InternetService = request.form.get('InternetService')
    OnlineSecurity = request.form.get('OnlineSecurity')
    OnlineBackup = request.form.get('OnlineBackup')
    DeviceProtection = request.form.get('DeviceProtection')
    TechSupport = request.form.get('TechSupport')
    StreamingTV = request.form.get('StreamingTV')
    StreamingMovies = request.form.get('StreamingMovies')
    Contract = request.form.get('Contract')
    PaperlessBilling = request.form.get('PaperlessBilling')
    PaymentMethod = request.form.get('PaymentMethod')

    result=model.predict(np.array([tenure, MonthlyCharges, TotalCharges,gender,SeniorCitizen,
                          Partner,Dependents,PhoneService,MultipleLines,InternetService,
                          OnlineSecurity,OnlineBackup,DeviceProtection,TechSupport,
                          StreamingTV,StreamingMovies,Contract,PaperlessBilling,
                          PaymentMethod]).reshape(1, 19))

    if result[0] == 0:
        outcome = 'Non-Churner'
        
    else:
        outcome = 'Churner'
        
        
    return render_template('homepage.html', result = outcome)



if __name__=="__main__":
    app.run(debug=True)