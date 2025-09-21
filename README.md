# GlucAware&Advisory App: Diabetes Advisory and Prediction Web App

GlucAware&Advisory App is a web application designed to predict diabetes risk and provide lifestyle recommendations using a user-friendly, accessible interface and a machine learning model. It supports five prediction outcomes unlike traditional models and takes your stress into account, health advisory charts, and multi-language health resources.

![Homepage Screenshot 1](docs/screenshots/firstpic.png)

## System Architecture

The system is built using a modular design comprising:

- **Frontend** (HTML/CSS/JS with Jinja2 templates)
- **Backend** (Python Flask)
- **Machine Learning Model** (ML Libraries in Python)
- **Firestore Database** (User profiles and prediction history)
- **Firebase Authentication** (Login, Registration, Password Reset)

### Prediction Flow

1. Users access a questionnaire to input medical data.
2. Backend validates and sends data to the ML model.
3. ML model returns:
   - Diabetes status: Diabetic, Prediabetic, Non-diabetic, Stress-induced Diabetic, or Stress-induced Prediabetic
   - Hypertension status
   - BMI status
4. Results are shown on the frontend and optionally saved if user is logged in.
=======
GlucAware&Advisory App is a web application designed to predict diabetes risk and provide lifestyle recommendations using a user-friendly, accessible interface and a machine learning model with extremely high accuracy (98.25%). It supports **five prediction outcomes** unlike traditional models and includes stress-sensitive diagnostics, health advisory charts, and multilingual health resources.

---

 ![Homepage Screenshot 1](docs/screenshots/firstpic.png)
 
## System Architecture

The system is built using a modular architecture:

- **Frontend:** HTML/CSS/JavaScript (Jinja2 templating via Flask)
- **Backend:** Python Flask
- **ML Model:** Trained in Python
- **Firestore:** Stores user profiles & prediction histories
- **Firebase Auth:** Manages login, registration, and password reset

---

## Prediction Flow

1. Users complete a health questionnaire.
2. Backend sends data to ML model for prediction.
3. ML Model returns:
   - Diabetes status (5 possible outcomes)
   - Hypertension status
   - BMI classification
4. Results are shown on screen. If logged in, they’re stored.
>>>>>>> 8e5715e4c87571c91493ab68d7b1298e5e0ffda1

---

## Home Page

<<<<<<< HEAD
- Provides an overview of the app's purpose and features
- Navigation bar + footer links for easy routing
- Contains general diabetes advice, embedded relaxation music
- Available for both guests and registered users

---

## Questionnaire & Results

- Open to all users (guests & registered)
- Inputs collected:
  - Gender
  - Age
  - Weight & Height
  - Smoking history
  - Blood pressure
  - Heart disease status
  - Blood sugar level
  - HbA1c
- Outputs shown:
  - Diabetes outcome
  - Hypertension status
  - BMI classification

![Questionnaire](docs/screenshots/secondpic.png)
![Results](docs/screenshots/thirdpic.png)

### Features
- Inputs editable post-submission
- Predictions flagged with red indicators if critical
- Flash messages for status updates

---

## User Authentication (Firebase)

- Sign-up, login, and password reset with Firebase Authentication
- Secure sessions for viewing and storing predictions
- Input validations and friendly flash messaging
=======
- Provides app overview and features
- Includes:
  - Navigation bar
  - Footer links
  - Diabetes awareness + relaxing music
- Same for guests & registered users

---

## Questionnaire & Prediction Results

- Inputs:
  - Gender, Age, Weight, Height
  - Smoking History
  - Blood Pressure
  - Heart Disease Status
  - Blood Sugar Level
  - HbA1c (%)
- Outputs:
  - Diabetes (5 outcomes)
  - BMI category
  - Hypertension status

![Questionnaire](docs/screenshots/secondpic.png)
![Results](docs/screenshots/thirdpic.png)
 
 
Features:
- Inputs are editable even post-submission
- Critical indicators (like high BP) flagged red
- Flash messaging included

---

## User Authentication

- **Firebase Authentication**
- Handles sign-up, login, and password resets
- Sessions + Flash messages for feedback
- Secure form validations
>>>>>>> 8e5715e4c87571c91493ab68d7b1298e5e0ffda1

---

## User Profile & History

<<<<<<< HEAD
- Stores:
  - Username, email, DOB, gender, medical conditions
  - Full prediction history with timestamps
- Features:
  - Track health trends
  - Quick navigation to diet/lifestyle chart generator
=======
- Displays:
  - Username, DOB, Email, Gender, Medical Conditions
  - Prediction history with timestamps
- Features:
  - Acts as health tracker
  - Direct access to personalized chart generator
>>>>>>> 8e5715e4c87571c91493ab68d7b1298e5e0ffda1

---

## Chart Generator

<<<<<<< HEAD
- Provides personalized schedules for:
  - Hypertension prevention
  - Stress management
  - BMI control
  - Diabetes management
  - General wellness
- Available schedules:
  - Day shift
  - Night shift
  - Flexible routine
- Chart delivery via email supported
=======
- Generates customized advisory charts for:
  - Hypertension prevention
  - Stress management
  - Weight/BMI control
  - Diabetes care
  - General health & wellness

- Timetable options:
  - Morning/Day-shift
  - Night-shift
  - Flexible routines

- Chart delivery via email supported
- Accessible by both guests and logged-in users
>>>>>>> 8e5715e4c87571c91493ab68d7b1298e5e0ffda1

---

## Resources Page

<<<<<<< HEAD
- Educational articles, videos, blogs, and courses
- Available in:
  - English
  - French
  - Malay
  - Hindi
  - Mandarin

---

## User Interface Design

- Clean, minimalist layout
- Theme colors: Blue, Dark Magenta, White (diabetes awareness)
- Fixed top navbar and clear navigation states
- Carousel slides on homepage
- Responsive buttons with hover effects
- Consistent theme across all pages
- Accessible layout adaptable to various screen sizes
- Chunked content to reduce cognitive overload
- Flash messaging and strong error handling

---

## Contact

Users can reach the developer through the `/contact_us` form with stored messages in Firestore.

=======
- Offers curated:
  - Articles, blogs, videos, free courses
- Languages supported:
  - English, French, Malay, Hindi, Mandarin
- Aimed at:
  - Diabetes prevention
  - Stress, BMI, hypertension management

---

## User Interface Highlights

- Clean, minimal, accessible design
- Theme Colors: Blue (awareness), Dark Magenta, White
- Fixed top navbar + page indicators
- Carousel on homepage
- Responsive buttons (hover animations)
- Consistent font/colors/sections
- Chunked layout to reduce overload
- Flash messaging & form error handling
- Input review/editing post-submission

---

## Contact Developer

- `/contact_us` form available for feedback
>>>>>>> 8e5715e4c87571c91493ab68d7b1298e5e0ffda1
---

## Deployment

<<<<<<< HEAD
- Hosted on **Heroku**
- Firebase credentials stored securely via `heroku config:set FIREBASE_CREDENTIALS`
- ML model and auth handled entirely in Python/Flask
=======
- Deployed via **Heroku**
- Firebase credentials set via:
```bash
heroku config:set FIREBASE_CREDENTIALS="$(cat config/firebase-adminsdk.json | jq -c .)"
heroku config:set FIREBASE_API_KEY=your_firebase_api_key
```
>>>>>>> 8e5715e4c87571c91493ab68d7b1298e5e0ffda1

---

## Live Preview

<<<<<<< HEAD
> [App Link](https://glucaware-e4e2c8fc9a82.herokuapp.com)

---

## RUN THIS SOFTWARE?

readme_path = "/mnt/data/README.md"

## 💻 How to Run the Code

### STEP 1. Clone the Repository
```bash
git clone https://github.com/yourusername/diabetes-advisory-app.git
cd diabetes-advisory-app

### STEP 2. Setup the Virtual Environment
python -m venv venv
On Mac: source venv/bin/activate
On Windows: venv\\Scripts\\activate

### STEP 3. Install relevant dependencies
pip install -r requirements.txt

### STEP 4. Setup the env & firebase
Create a .env file in the root directory with the following variables:

FIREBASE_API_KEY=your_firebase_api_key #get it from firebase app
FIREBASE_CREDENTIALS_JSON=contents_of_your_service_account_json_file

### STEP 5. Run the application locally
Once you set up the venv and install dependencies in the venv
proceed to the backend folder by cd src backend
then RUN>>
python run.py
Then visit: http://127.0.0.1:5000







=======
🔗 [View App](https://glucaware-e4e2c8fc9a82.herokuapp.com)

---

## How to Run the Code

### STEP 1: Clone the repository
```bash
git clone https://github.com/yourusername/diabetes-advisory-app.git
cd diabetes-advisory-app
```

### STEP 2: Setup the virtual environment
```bash
python -m venv venv
# On Mac/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### STEP 3: Install dependencies
```bash
pip install -r requirements.txt
```

### STEP 4: Configure environment variables

Create a `.env` file in the root directory and add:
```
FIREBASE_API_KEY=your_firebase_api_key
FIREBASE_CREDENTIALS_JSON=<paste one-line JSON of service account>
```

**Note:** You can generate the `FIREBASE_CREDENTIALS_JSON` using:
```bash
cat config/firebase-adminsdk.json | jq -c .
```

### STEP 5: Run the app
```bash
cd src backend
python run.py
```

Now open: [http://127.0.0.1:5000](http://127.0.0.1:5000)

this will eventually lead to the flask server running the web application.
>>>>>>> 8e5715e4c87571c91493ab68d7b1298e5e0ffda1
