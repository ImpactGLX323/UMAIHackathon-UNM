import numpy as np
from flask import Flask, request, render_template
import joblib

# Create Flask app
flask_app = Flask(__name__)
model = joblib.load("model/stacking_classifier.pkl")

# List to map prediction values to status
status_order = ['non diabetic', 'stress induced prediabetic', 'stress induced type 2 diabetic', 'prediabetic', 'diabetic']

# Home route
@flask_app.route("/")
def Home():
    return render_template("index.html")

# Questionnaire route
@flask_app.route("/questionnaire")
def questionnaire():
    return render_template("questionnaire.html")

# Prediction route
@flask_app.route("/predict", methods=["POST"])
def predict():
    # Retrieve features from the form
    feature0 = float(request.form['feature0'])  # Age
    feature1 = int(request.form['feature1'])  # Hypertension (Yes: 1, No: 0)
    feature2 = int(request.form['feature2'])  # Heart Disease (Yes: 1, No: 0)
    feature3 = float(request.form['feature3'])  # BMI
    feature4 = float(request.form['feature4'])  # HbA1c Level
    feature5 = float(request.form['feature5'])  # Blood Glucose Level

    # Gender options (assuming 1 for Female, 0 for Male)
    feature6 = int(request.form['feature6'])  # Gender: 1 for Female, 0 for Male

    # Smoking History (mapping the option to 0 for Yes, 1 for No)
    smoking_history = {
        "Yes": 0,  # Yes for smoking history
        "No": 1,   # No for smoking history
    }
    feature7 = smoking_history.get(request.form['feature7'], 1)  # Defaulting to No if invalid
    feature8 = smoking_history.get(request.form['feature8'], 1)
    feature9 = smoking_history.get(request.form['feature9'], 1)
    feature10 = smoking_history.get(request.form['feature10'], 1)
    feature11 = smoking_history.get(request.form['feature11'], 1)
    feature12 = smoking_history.get(request.form['feature12'], 1)
    feature13 = smoking_history.get(request.form['feature13'], 1)

    # Create feature array
    features = np.array([[feature0, feature1, feature2, feature3, feature4, feature5, 
                          feature6, feature7, feature8, feature9, feature10, feature11, feature12, feature13]])
    
    # Predict using the model
    prediction = model.predict(features)
    
    # Map prediction index to status
    prediction_status = status_order[prediction[0]]

    # Determine which template to render based on the request's referring page
    if "questionnaire" in request.referrer:  # If the request came from the questionnaire page
        return render_template("questionnaire.html", prediction_text="The diabetes status is {}".format(prediction_status))
    else:  # Default to rendering the index page
        return render_template("index.html", prediction_text="The diabetes status is {}".format(prediction_status))
    
# Run the Flask app
if __name__ == "__main__":
    flask_app.run(debug=True)
