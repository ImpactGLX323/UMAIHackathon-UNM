from flask import Flask, render_template, request, jsonify, redirect, url_for, session, flash
import numpy as np
import firebase_admin
from firebase_admin import credentials, auth, initialize_app
import os
import traceback
import requests


# Get absolute path of the JSON key
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Gets the app/ directory path
JSON_PATH = os.path.join(BASE_DIR, "../config/firebase-adminsdk.json")  # Moves up one level

FIREBASE_API_KEY = "AIzaSyCMjC4N4MvkIFvIuJhon_FMi2zOo9eyja8"  # Replace with your Firebase API Key

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
                # Firebase REST API endpoint for authentication
                url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={FIREBASE_API_KEY}"

                payload = {
                    "email": email,
                    "password": password,
                    "returnSecureToken": True
                }

                headers = {"Content-Type": "application/json"}

                # Send request to Firebase Authentication
                response = requests.post(url, json=payload, headers=headers)
                data = response.json()

                if "error" in data:
                    flash("Invalid email or password. Please try again.", "error")
                    return render_template("login.html")

                # Successful login, store user session
                session["user_id"] = data["localId"]  # Store Firebase UID in session
                session["id_token"] = data["idToken"]  # Store authentication token
                flash("Login successful!", "success")
                return redirect(url_for("home"))

            except Exception as e:
                flash("An error occurred. Please try again.", "error")
                print("Error in login:", traceback.format_exc())  # Debugging output

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
                # Firebase REST API for account creation
                url = f"https://identitytoolkit.googleapis.com/v1/accounts:signUp?key={FIREBASE_API_KEY}"
                payload = {"email": email, "password": password, "returnSecureToken": True}
                headers = {"Content-Type": "application/json"}

                response = requests.post(url, json=payload, headers=headers)
                data = response.json()

                if "error" in data:
                    flash("Email already in use or invalid. Try another one.", "error")
                    return render_template("register.html")

                flash("Registration successful! Please log in.", "success")
                return redirect(url_for("login"))

            except Exception as e:
                flash("An error occurred. Please try again.", "error")
                print("Error in register:", traceback.format_exc())

        return render_template("register.html")
    
    @app.route("/forgot_password", methods=["GET", "POST"])
    def forgot_password():
        if request.method == "POST":
            email = request.form.get("email")
            print(f"Received email: {email}")  # ✅ Check if email is received correctly

            try:
                reset_link = auth.generate_password_reset_link(email)
                print(f"Generated reset link: {reset_link}")  # ✅ See if Firebase generates a link
                
                flash("Password reset link sent! Check your email.", "success")
                return redirect(url_for("login"))
            except firebase_admin.auth.UserNotFoundError:
                flash("No account found with this email!", "error")
                print("Error: User not found!")  # ✅ Debugging output
            except Exception as e:
                flash("An error occurred. Please try again later.", "error")
                print("Error in forgot_password:", traceback.format_exc())  # ✅ Print full error stack

        return render_template("forgot_password.html")

    
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
