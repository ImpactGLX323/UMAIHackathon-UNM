import os
from flask import Flask
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def create_app():
    app = Flask(__name__, 
                template_folder="templates", 
                static_folder="static")

    # Use the secret key from the environment variable
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default-secret-key')

    from app.routes import configure_routes

    # Ensure app context is active when configuring routes
    with app.app_context():
        configure_routes(app)  

    return app
