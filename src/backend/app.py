import numpy as np
from flask import Flask, request, render_template
import joblib

# Create Flask app
flask_app = Flask(__name__)
model = joblib.load("../../model/stacking_classifier.pkl")

# List to map prediction values to status
status_order = ['non diabetic', 'stress induced prediabetic', 'stress induced type 2 diabetic', 'prediabetic', 'diabetic']

@flask_app.route("/")
def Home():
    return render_template("index.html")

@flask_app.route("/predict", methods=["POST"])
def predict():
    # Retrieve features from the form
    float_features = [float(request.form[f'feature{i}']) for i in range(14)]
    features = [np.array(float_features)]
    
    # Predict using the model
    prediction = model.predict(features)
    
    # Map prediction index to status
    prediction_status = status_order[prediction[0]]
    
    # Return the result to the frontend
    return render_template("index.html", prediction_text="The diabetes status is {}".format(prediction_status))

if __name__ == "__main__":
    flask_app.run(debug=True)
