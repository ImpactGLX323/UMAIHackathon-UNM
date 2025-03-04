from flask import Flask, render_template, request, jsonify, redirect, url_for, session, flash
import numpy as np
import firebase_admin
from firebase_admin import credentials, auth, initialize_app
import os
import traceback

# Get absolute path of the JSON key
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Gets the app/ directory path
JSON_PATH = os.path.join(BASE_DIR, "src/backend/config/firebase-adminsdk.json")  # Moves up one level

# Initialize Firebase
cred = credentials.Certificate(JSON_PATH)  # ✅ Use the correct path

if not firebase_admin._apps: # Check whether firebase has been initialized before or not
    firebase_app = initialize_app(cred) 

def configure_routes(app):
    from .model import predict_diabetes  # Using relative import
    
    @app.route("/")
    def home():
        return render_template("home.html")

    @app.route("/login", methods=["GET", "POST"])
    def login():
        if request.method == "POST":
            email = request.form.get("email")
            password = request.form.get("password")

            try:
                user = auth.get_user_by_email(email)
                session["user_id"] = user.uid  # Store user session
                flash("Login successful!", "success")
                return redirect(url_for("home"))
            except firebase_admin.auth.UserNotFoundError:
                flash("User not found. Please check your email.", "error")
                return render_template("login.html")
        
        return render_template("login.html")

    @app.route("/register", methods=["GET", "POST"])
    def register():
        if request.method == "POST":
            email = request.form.get("email")
            password = request.form.get("password")
            confirm_password = request.form.get("confirm_password")

            if password != confirm_password:
                flash("Passwords do not match!", "error")
                return render_template("register.html")

            try:
                user = auth.create_user(email=email, password=password)
                flash("Registration successful! Please log in.", "success")
                return redirect(url_for("login"))
            except firebase_admin._auth_utils.DuplicateEmailError:
                flash("Email already in use. Try another one.", "error")
                return render_template("register.html")

        return render_template("register.html")
    
    @app.route("/questionnaire")
    def questionnaire():
        return render_template("questionnaire.html")
    
    @app.route("/test")
    def test():
        return render_template("test.html")

    @app.route("/predict", methods=["POST"])
    def predict():
        try:
            age = float(request.form.get('feature0', 0))
            blood_pressure = int(request.form.get('feature1', 0))
            heart_disease = int(request.form.get('feature2', 0))
            bmi = float(request.form.get('feature3', 0))
            hba1c_level = float(request.form.get('feature4', 0))
            blood_sugar_level = float(request.form.get('feature5', 0))
            gender = int(request.form.get('feature6', 0))
            is_male = int(request.form.get('feature7', 0))
            smoking_history = int(request.form.get('feature8', 0))
            no_info = int(request.form.get('feature9', 0))
            never = int(request.form.get('feature10', 0))
            ever = int(request.form.get('feature11', 0))
            former = int(request.form.get('feature12', 0))
            not_current = int(request.form.get('feature13', 0))

            features = np.array([[age, blood_pressure, heart_disease, bmi, hba1c_level,
                                  blood_sugar_level, gender, is_male, smoking_history,
                                  no_info, never, ever, former, not_current]])

            response = predict_diabetes(features)
            if "error" in response:
                return jsonify(response), 500

            return jsonify(response)

        except Exception as e:
            print("Error in /predict:", traceback.format_exc())  # Full traceback
            return jsonify({'error': 'Internal Server Error. Check logs.'}), 500

