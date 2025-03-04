import os
import numpy as np
import joblib

#Loading the model
model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"../model/stacking_classifier.pkl")

try:
    model = joblib.load(model_path)
except FileNotFoundError:
    print("Error: Model file not found")
    model = None

#List to map the prediction values to status 
status_order = ['non diabetic', 'stress induced prediabetic', 'stress induced type 2 diabetic', 'prediabetic', 'diabetic']\

def predict_diabetes(features):
    if model is None:
        return {'error': 'Model not loaded'} 
    
    prediction = model.predict(features)
    return{'prediction': status_order[prediction[0]],}