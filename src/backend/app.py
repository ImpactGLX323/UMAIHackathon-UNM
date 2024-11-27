import numpy as np
from flask import Flask, request, render_template, jsonify
import joblib
import os 

# Create Flask app
flask_app = Flask(__name__,
                 template_folder = "templates",
                 static_folder = "static")

# Load the model
model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "stacking_classifier.pkl")
model = joblib.load(model_path)

# List to map prediction values to status
status_order = ['non diabetic', 'stress induced prediabetic', 'stress induced type 2 diabetic', 'prediabetic', 'diabetic']


# Route for the questionnaire page
@flask_app.route("/")
def questionnaire():
    return render_template("questionnaire.html")

# Prediction route
@flask_app.route("/predict", methods=["POST"])
def predict():
    try:
        # Retrieve form data and convert to float or int
        age = float(request.form.get('feature0'))
        blood_pressure = int(request.form.get('feature1'))
        heart_disease = int(request.form.get('feature2'))
        bmi = float(request.form.get('feature3'))
        hba1c_level = float(request.form.get('feature4'))
        blood_sugar_level = float(request.form.get('feature5'))
        gender = int(request.form.get('feature6'))
        is_male = int(request.form.get('feature7'))
        smoking_history = int(request.form.get('feature8'))
        no_info = int(request.form.get('feature9'))
        never = int(request.form.get('feature10'))
        ever = int(request.form.get('feature11'))
        former = int(request.form.get('feature12'))
        not_current = int(request.form.get('feature13'))

        # Prepare the feature array for prediction
        features = np.array([[age, blood_pressure, heart_disease, bmi, hba1c_level,
                              blood_sugar_level, gender, is_male, smoking_history,
                              no_info, never, ever, former, not_current]])

        # Predict using the loaded model
        prediction = model.predict(features)
        prediction_status = status_order[prediction[0]]

        # Return JSON response
        return jsonify({'prediction': prediction_status})

    except Exception as e:
        print(f"Error occurred: {e}")
        return jsonify({'error': 'Error occurred during prediction. Please try again.'}), 500

# Run the Flask app
if __name__ == "__main__":
    flask_app.run(debug=True)

