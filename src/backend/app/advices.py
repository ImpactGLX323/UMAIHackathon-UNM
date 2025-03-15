import os
import traceback
from datetime import datetime
from flask_mail import Mail, Message

# Initialize Flask-Mail
mail = Mail()

def calculate_age(dob):
    """
    Calculate age based on the date of birth (dob).
    """
    today = datetime.today()
    birth_date = datetime.strptime(dob, "%Y-%m-%d")
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

def generate_advice(category, schedule):
    """
    Generate advice based on the selected category and schedule.
    """
    advice_data = {
        "category": category,
        "schedule": schedule,
        "advice": {}
    }

    if category == "stress":
        if schedule == "morning":
            advice_data["advice"] = {
                "Wake-Up Routine": "🌅 6:00 AM – Stretch, drink warm lemon water",
                "Breakfast": "Oats + banana + flaxseeds + chamomile tea",
                "Midday Break": "Walk/stretch (10 min)",
                "Lunch": "Salmon + quinoa + spinach + olive oil",
                "Afternoon Relaxation": "Music, nature walk, journaling",
                "Evening Activity": "Gym (light cardio) or Tai Chi",
                "Dinner": "Magnesium-rich foods (nuts, leafy greens)",
                "Night Routine": "Digital detox (1 hour before bed)",
                "Sleep": "🛏️ 10:30 PM – 6:00 AM",
                "Supplements": "Ashwagandha, omega-3, vitamin B",
                "Weekend Focus": "Outdoor time, socializing",
                "Screen Time Limit": "📱 Off by 9:30 PM",
                "Caffeine Intake": "☕ Before 2 PM",
                "Stress Tracking": "Rate stress & sleep quality daily",
                "Additional Relaxation": "Aromatherapy, soft music",
                "Bonus Tips": "Hydration: Drink 2.5–3L water/day, Avoid caffeine, alcohol, sugar, ultra-processed foods"
            }
        elif schedule == "night":
            advice_data["advice"] = {
                "Wake-Up Routine": "🌙 4:00 PM – Light stretching, herbal tea",
                "Breakfast": "Eggs + avocado + smoothie",
                "Midday Break": "Meditation (10 min)",
                "Lunch": "Chicken + brown rice + steamed veggies",
                "Afternoon Relaxation": "Short nap, deep breathing",
                "Evening Activity": "Strength training (low intensity)",
                "Dinner": "Light meal + chamomile tea",
                "Night Routine": "Deep breathing, guided meditation",
                "Sleep": "🛏️ 8:00 AM – 4:00 PM",
                "Supplements": "Magnesium, L-theanine",
                "Weekend Focus": "Creative hobbies, nature exposure",
                "Screen Time Limit": "📱 Limit blue light 1 hr before bed",
                "Caffeine Intake": "☕ Avoid 6 hrs before sleep",
                "Stress Tracking": "Adjust routine for better sleep",
                "Additional Relaxation": "Gratitude journaling",
                "Bonus Tips": "Hydration: Drink 2.5–3L water/day, Avoid caffeine, alcohol, sugar, ultra-processed foods"
            }
        elif schedule == "flexible":
            advice_data["advice"] = {
                "Wake-Up Routine": "☀️ 7:00 AM / 9:00 AM – Yoga, sun exposure",
                "Breakfast": "High-protein meal + green tea",
                "Midday Break": "Hobby or deep breathing",
                "Lunch": "Home-cooked balanced meal",
                "Afternoon Relaxation": "Socializing, creative activities",
                "Evening Activity": "Brisk walk, cycling, or dancing",
                "Dinner": "Protein + fiber-rich meal",
                "Night Routine": "Chamomile tea + slow breathing",
                "Sleep": "🛏️ 10:00 PM – 6:00 AM or 12:00 AM – 8:00 AM",
                "Supplements": "Adapt based on stress levels",
                "Weekend Focus": "Digital detox, self-care",
                "Screen Time Limit": "📱 Reduce evening screen time",
                "Caffeine Intake": "☕ Moderation (1-2 cups max)",
                "Stress Tracking": "Identify top 3 habits to keep",
                "Additional Relaxation": "Sauna, massage, nature therapy",
                "Bonus Tips": "Hydration: Drink 2.5–3L water/day, Avoid caffeine, alcohol, sugar, ultra-processed foods"
            }

    elif category == "diabetes":
        # Add similar logic for diabetes, hypertension, BMI, and healthy categories
        pass

    return advice_data

def send_advice_email(email, advice):
    """
    Send the generated advice to the user's email.
    """
    try:
        msg = Message("Your Custom Health Advice", recipients=[email])
        msg.body = f"""
        Here is your custom health advice:

        Category: {advice.get("category")}
        Schedule: {advice.get("schedule")}

        Advice:
        {advice.get("advice")}

        Thank you for using our Diabetes Advisory Service!

        Regards,
        GlucAware Advisory Team
        """

        mail.send(msg)
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False