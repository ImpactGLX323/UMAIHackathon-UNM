import os
import traceback
import numpy as np
import requests
from flask import Flask, render_template, request, jsonify, redirect, url_for, session, flash
import firebase_admin
from firebase_admin import credentials, auth, initialize_app, firestore
from flask_mail import Mail, Message
from datetime import datetime
from app.model import predict_diabetes
from app.advices import generate_advice, send_advice_email, calculate_age
from functools import wraps

# Configuration and Firebase setup
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.getenv("FIREBASE_CREDENTIALS", os.path.join(BASE_DIR, "../config/firebase-adminsdk.json"))
FIREBASE_API_KEY = 'AIzaSyCMjC4N4MvkIFvIuJhon_FMi2zOo9eyja8'

if not firebase_admin._apps:
    cred = credentials.Certificate(JSON_PATH)
    firebase_app = initialize_app(cred)
    db = firestore.client()

def configure_routes(app):
    # Email configuration
    app.config.update(
        MAIL_SERVER='smtp.gmail.com',
        MAIL_PORT=587,
        MAIL_USE_TLS=True,
        MAIL_USERNAME='aipredict2025@gmail.com',
        MAIL_PASSWORD='fjzj xrxo owaa lwwh',
        MAIL_DEFAULT_SENDER='aipredict2025@gmail.com'
    )
    mail = Mail(app)

    # Error handling decorator
    def handle_errors(route_func):
        @wraps(route_func)
        def wrapper(*args, **kwargs):
            try:
                return route_func(*args, **kwargs)
            except Exception as e:
                app.logger.error(f"Error in {route_func.__name__}: {str(e)}")
                traceback.print_exc()
                flash("An error occurred. Please try again.", "error")
                if request.method == "POST":
                    return redirect(url_for(route_func.__name__))
                return render_template(f"{route_func.__name__}.html")
        wrapper.__name__ = route_func.__name__
        return wrapper

    # Routes
    @app.route("/")
    def home():
        return render_template("home.html")

    @app.route("/login", methods=["GET", "POST"])
    @handle_errors
    def login():
        if request.method == "POST":
            email = request.form.get("email", "").strip()
            password = request.form.get("password", "")

            if not email or not password:
                flash("Please enter both email and password", "error")
                return redirect(url_for("login"))

            try:
                auth_url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={FIREBASE_API_KEY}"
                auth_response = requests.post(
                    auth_url,
                    json={"email": email, "password": password, "returnSecureToken": True},
                    headers={"Content-Type": "application/json"}
                )
                auth_response.raise_for_status()  # This will raise for 4XX/5XX responses
                auth_data = auth_response.json()

                if "error" in auth_data:
                    error_msg = auth_data["error"].get("message", "Invalid credentials")
                    flash(f"Login failed: {error_msg}", "error")
                    return redirect(url_for("login"))

                session["user_id"] = auth_data["localId"]
                session["id_token"] = auth_data["idToken"]
                flash("Login successful!", "success")
                return redirect(url_for("profile"))

            except requests.exceptions.RequestException as e:
                app.logger.error(f"Login request failed: {str(e)}")
                flash("Could not connect to authentication service. Please try again later.", "error")
                return redirect(url_for("login"))
            except ValueError as e:
                app.logger.error(f"Invalid response from auth service: {str(e)}")
                flash("Invalid response from authentication service. Please try again.", "error")
                return redirect(url_for("login"))
            except Exception as e:
                app.logger.error(f"Unexpected login error: {str(e)}")
                flash("An unexpected error occurred during login. Please try again.", "error")
                return redirect(url_for("login"))

        return render_template("login.html")

    @app.route("/register", methods=["GET", "POST"])
    @handle_errors
    def register():
        if request.method == "POST":
            form_data = {
                "username": request.form.get("username", "").strip(),
                "email": request.form.get("email", "").strip(),
                "dob": request.form.get("dob", ""),
                "password": request.form.get("password", ""),
                "confirm_password": request.form.get("confirm_password", ""),
                "medical_history": request.form.getlist("medical_history"),
                "gender": request.form.getlist("gender")
            }

            # Validation
            if not all([form_data["username"], form_data["email"], form_data["dob"], 
                       form_data["password"], form_data["confirm_password"]]):
                flash("Please fill in all required fields", "error")
                return redirect(url_for("register"))

            if form_data["password"] != form_data["confirm_password"]:
                flash("Passwords do not match", "error")
                return redirect(url_for("register"))

            if len(form_data["password"]) < 8:
                flash("Password must be at least 8 characters", "error")
                return redirect(url_for("register"))

            try:
                # Create Firebase auth user
                auth_url = f"https://identitytoolkit.googleapis.com/v1/accounts:signUp?key={FIREBASE_API_KEY}"
                auth_response = requests.post(
                    auth_url,
                    json={"email": form_data["email"], "password": form_data["password"], "returnSecureToken": True},
                    headers={"Content-Type": "application/json"}
                )
                auth_data = auth_response.json()

                if "error" in auth_data:
                    error_msg = auth_data["error"].get("message", "Registration failed")
                    flash(f"Registration error: {error_msg}", "error")
                    return redirect(url_for("register"))

                # Store user data in Firestore
                user_data = {
                    "username": form_data["username"],
                    "email": form_data["email"],
                    "dob": form_data["dob"],
                    "medical_history": form_data["medical_history"],
                    "gender": form_data["gender"],
                    "created_at": datetime.now().isoformat()
                }
                db.collection("users").document(auth_data["localId"]).set(user_data)
                
                flash("Registration successful! Please log in.", "success")
                return redirect(url_for("login"))

            except Exception as e:
                flash("Registration failed. Please try again.", "error")
                app.logger.error(f"Registration error: {str(e)}")
                return redirect(url_for("register"))

        return render_template("register.html")

    @app.route("/forgot_password", methods=["GET", "POST"])
    @handle_errors
    def forgot_password():
        if request.method == "POST":
            email = request.form.get("email", "").strip()
            if not email:
                flash("Please enter your email address", "error")
                return redirect(url_for("forgot_password"))

            try:
                reset_url = f"https://identitytoolkit.googleapis.com/v1/accounts:sendOobCode?key={FIREBASE_API_KEY}"
                reset_response = requests.post(
                    reset_url,
                    json={"requestType": "PASSWORD_RESET", "email": email},
                    headers={"Content-Type": "application/json"}
                )
                reset_response.raise_for_status()  # Raises for HTTP errors
                reset_data = reset_response.json()

                if "error" in reset_data:
                    error_msg = reset_data["error"].get("message", "Failed to send reset email")
                    flash(error_msg, "error")
                else:
                    flash("Password reset email sent! Check your inbox.", "success")

                return redirect(url_for("login"))

            except requests.exceptions.RequestException as e:
                app.logger.error(f"Password reset request failed: {str(e)}")
                flash("Could not connect to password reset service. Please try again later.", "error")
                return redirect(url_for("forgot_password"))
            except ValueError as e:
                app.logger.error(f"Invalid response from password reset service: {str(e)}")
                flash("Invalid response from password reset service. Please try again.", "error")
                return redirect(url_for("forgot_password"))
            except Exception as e:
                app.logger.error(f"Unexpected password reset error: {str(e)}")
                flash("An unexpected error occurred during password reset. Please try again.", "error")
                return redirect(url_for("forgot_password"))

        return render_template("forgot_password.html")

    @app.route("/logout")
    def logout():
        session.clear()
        flash("You have been logged out successfully.", "success")
        return redirect(url_for("home"))

    @app.route("/profile")
    @handle_errors
    def profile():
        user_id = session.get("user_id")
        if not user_id:
            flash("Please log in to access your profile", "error")
            return redirect(url_for("login"))

        try:
            user_doc = db.collection("users").document(user_id).get()
            if not user_doc.exists:
                flash("User profile not found", "error")
                return redirect(url_for("home"))

            predictions = db.collection("users").document(user_id)\
                .collection("predictions")\
                .order_by("timestamp", direction=firestore.Query.DESCENDING)\
                .limit(10)\
                .stream()
            
            return render_template("profile.html", 
                                user=user_doc.to_dict(), 
                                predictions=[doc.to_dict() for doc in predictions])

        except Exception as e:
            flash("Failed to load profile data", "error")
            app.logger.error(f"Profile error: {str(e)}")
            return redirect(url_for("home"))
        
    @app.route("/test")
    def test():
        return render_template("test.html")

    @app.route("/predict", methods=["POST"])
    @handle_errors
    def predict():
        try:
            # Extract and validate features
            features = np.array([[
                float(request.form.get(f'feature{i}', 0))
                for i in range(14)
            ]])

            # Get prediction
            prediction = predict_diabetes(features)
            if "error" in prediction:
                return jsonify(prediction), 500

            # Store prediction if user is logged in
            user_id = session.get("user_id")
            if user_id:
                prediction_data = {
                    **{f"feature{i}": features[0][i] for i in range(14)},
                    "prediction_result": prediction.get("prediction", "Unknown"),
                    "timestamp": datetime.now().isoformat()
                }
                db.collection("users").document(user_id)\
                    .collection("predictions").add(prediction_data)
                flash("Prediction saved successfully", "success")

            return jsonify(prediction)

        except Exception as e:
            app.logger.error(f"Prediction error: {str(e)}")
            return jsonify({"error": "Prediction failed"}), 500

    @app.route("/chart", methods=["GET", "POST"])
    @handle_errors
    def chart():
        if request.method == "POST":
            category = request.form.get("category")
            schedule = request.form.get("schedule")
            email = request.form.get("email", "").strip()

            if not category or not schedule:
                flash("Please select both category and schedule", "error")
                return redirect(url_for("chart"))

            advice = generate_advice(category, schedule)
            
            if email:
                try:
                    send_advice_email(email, advice)
                    flash("Advice has been sent to your email!", "success")
                except Exception as e:
                    app.logger.error(f"Email error: {str(e)}")
                    flash("Could not send email, but advice is displayed below", "warning")

            return render_template("chart.html", advice=advice)

        return render_template("chart.html")
    
    @app.route("/questionnaire")
    def questionnaire():
        return render_template("questionnaire.html")
    
    @app.route("/history")
    def history():
        # Check if the user is logged in
        user_id = session.get("user_id")
        if not user_id:
            flash("You need to log in to access your history.", "error")
            return redirect(url_for("login"))

        try:
            # Fetch the user's prediction history from Firestore
            predictions_ref = db.collection("users").document(user_id).collection("predictions")
            predictions = [doc.to_dict() for doc in predictions_ref.stream()]

            # Render the history template with prediction data
            return render_template("history.html", predictions=predictions)

        except Exception as e:
            flash("An error occurred while retrieving your history.", "error")
            print("Error in /history route:", traceback.format_exc())
            return redirect(url_for("home"))

    
    from flask_mail import Message

    @app.route("/send_email", methods=["POST"])
    def send_email():
        try:
            data = request.json
            recipient_email = data['email']
            results = data['results']

            # Create an HTML-formatted email
            html_body = f"""
            <html>
            <head>
                <style>
                    body {{
                        font-family: 'Arial', sans-serif;
                        line-height: 1.6;
                        color: #333;
                        background-color: #f9f9f9;
                        padding: 20px;
                    }}
                    h1 {{
                        color: #4ba2d5;
                        font-size: 24px;
                        margin-bottom: 20px;
                    }}
                    h2 {{
                        color: #333;
                        font-size: 20px;
                        margin-top: 30px;
                        margin-bottom: 10px;
                    }}
                    p {{
                        margin: 10px 0;
                    }}
                    .results-table {{
                        width: 100%;
                        border-collapse: collapse;
                        margin-top: 20px;
                    }}
                    .results-table th, .results-table td {{
                        border: 1px solid #ddd;
                        padding: 12px;
                        text-align: left;
                    }}
                    .results-table th {{
                        background-color: #4ba2d5;
                        color: white;
                    }}
                    .results-table tr:nth-child(even) {{
                        background-color: #f2f2f2;
                    }}
                    .footer {{
                        margin-top: 30px;
                        font-size: 14px;
                        color: #777;
                    }}
                </style>
            </head>
            <body>
                <h1>Your Diabetes Prediction Results</h1>
                <p>Here are your submitted results:</p>

                <table class="results-table">
                    <tr>
                        <th>Category</th>
                        <th>Value</th>
                    </tr>
                    <tr>
                        <td>Gender</td>
                        <td>{results['gender']}</td>
                    </tr>
                    <tr>
                        <td>Age</td>
                        <td>{results['age']}</td>
                    </tr>
                    <tr>
                        <td>Blood Pressure</td>
                        <td>{results['bp']}</td>
                    </tr>
                    <tr>
                        <td>Heart Disease</td>
                        <td>{results['heartDisease']}</td>
                    </tr>
                    <tr>
                        <td>Smoking History</td>
                        <td>{results['smokingHistory']}</td>
                    </tr>
                    <tr>
                        <td>Height</td>
                        <td>{results['height']} cm</td>
                    </tr>
                    <tr>
                        <td>Weight</td>
                        <td>{results['weight']} kg</td>
                    </tr>
                    <tr>
                        <td>HbA1c Level</td>
                        <td>{results['HbA1c']}</td>
                    </tr>
                    <tr>
                        <td>Blood Sugar Level</td>
                        <td>{results['bloodSugar']}</td>
                    </tr>
                    <tr>
                        <td>BMI</td>
                        <td>{results['bmi']} ({results['bmiCategory']})</td>
                    </tr>
                    <tr>
                        <td>Hypertension Status</td>
                        <td>{results['hypertensionStatus']}</td>
                    </tr>
                    <tr>
                        <td>Diabetes Prediction</td>
                        <td>{results['diabetesPrediction']}</td>
                    </tr>
                </table>

                <div class="footer">
                    <p>Thank you for using our Diabetes Advisory Service!</p>
                    <p>Regards,<br>GlucAware Advisory Team</p>
                </div>
            </body>
            </html>
            """

            # Create the email message
            msg = Message(
                subject="Your Diabetes Prediction Results",
                recipients=[recipient_email],
                html=html_body  # Use HTML for the email body
            )

            # Send the email
            mail.send(msg)
            return jsonify({"message": "Email sent successfully"}), 200

        except Exception as e:
            print(f"Email error: {e}")
            return jsonify({"error": f"Failed to send email: {str(e)}"}), 500

    @app.route("/resources1")
    def resources1():
        return render_template("resources1.html")

    @app.route("/resources1/english")
    def resources_english():
        return render_template("resources1_english.html")

    @app.route("/resources1/malay")
    def resources_malay():
        return render_template("resources1_malay.html")

    @app.route("/resources1/french")
    def resources_french():
        return render_template("resources1_french.html")

    @app.route("/resources1/hindi")
    def resources_hindi():
        return render_template("resources1_hindi.html")

    @app.route("/resources1/chinese")
    def resources_chinese():
        return render_template("resources1_chinese.html")

    @app.route("/contact_us", methods=["GET", "POST"])
    def contact_us():
        if request.method == "POST":
            try:
                name = request.form.get("name", "").strip()
                email = request.form.get("email", "").strip()
                message = request.form.get("message", "").strip()

                # Validate
                if not name or not email or not message:
                    flash("Please fill out all fields.", "error")
                    return redirect(url_for("contact_us"))

                # Store to Firestore
                db.collection("messages_to_dev").add({
                    "name": name,
                    "email": email,
                    "message": message,
                    "timestamp": datetime.utcnow().isoformat()
                })

                flash("Message sent successfully!", "success")
                return redirect(url_for("contact_us"))

            except Exception as e:
                flash("An error occurred while sending your message.", "error")
                print(f"[Contact Error] {str(e)}")
                return redirect(url_for("contact_us"))

        return render_template("contact_us.html")

 