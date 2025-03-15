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
    print(f"Generating advice for category: {category}, schedule: {schedule}")  # Debugging
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
        if schedule == "morning":
            advice_data["advice"] = {
                "Wake-Up Routine": "🌅 6:00 AM – Lemon water, light stretching",
                "Breakfast": "Oats + chia seeds + nuts + eggs",
                "Lunch": "Grilled chicken/fish + quinoa + leafy greens",
                "Dinner": "Light meal (soup + whole-grain bread)",
                "Snacks": "Nuts, hummus, dark chocolate (small piece)",
                "Physical Activity": "Walk after meals, strength training",
                "Yoga & Meditation": "Pranayama breathing, mindful eating",
                "Sleep": "🛏️ 10:30 PM – 6:00 AM",
                "Supplements": "Cinnamon, Berberine, Omega-3",
                "Bonus Tips": "Monitor blood sugar, maintain regular meal times, and avoid refined carbs."
            }
        elif schedule == "night":
            advice_data["advice"] = {
                "Wake-Up Routine": "🌙 4:00 PM – Hydration + mobility exercises",
                "Breakfast": "High-protein smoothie (Greek yogurt, berries, flaxseeds)",
                "Lunch": "Brown rice + lentils + veggies",
                "Dinner": "High-fiber meal (veggies + legumes)",
                "Snacks": "Greek yogurt, almonds",
                "Physical Activity": "Light cardio before work",
                "Yoga & Meditation": "Gentle yoga before sleep",
                "Sleep": "🛏️ 8:00 AM – 4:00 PM",
                "Supplements": "Magnesium, Fenugreek",
                "Bonus Tips": "Monitor blood sugar, maintain regular meal times, and avoid refined carbs."
            }
        elif schedule == "flexible":
            advice_data["advice"] = {
                "Wake-Up Routine": "☀️ 7:00 AM / 9:00 AM – Yoga, 15 min walk",
                "Breakfast": "Scrambled tofu/chicken + whole-grain toast",
                "Lunch": "Salad with avocado + lean protein",
                "Dinner": "Protein-rich, low-carb meal",
                "Snacks": "Apple + peanut butter",
                "Physical Activity": "Cycling, swimming, HIIT",
                "Yoga & Meditation": "Evening meditation",
                "Sleep": "🛏️ 10:00 PM – 6:00 AM",
                "Supplements": "Alpha-lipoic acid (ALA)",
                "Bonus Tips": "Monitor blood sugar, maintain regular meal times, and avoid refined carbs."
            }

    elif category == "hypertension":
        if schedule == "morning":
            advice_data["advice"] = {
                "Wake-Up Routine": "🌅 6:30 AM – Hydration + breathing exercises",
                "Breakfast": "Whole-grain toast + avocado + eggs",
                "Lunch": "Grilled salmon + spinach + sweet potato",
                "Dinner": "Low-sodium soup + whole grains",
                "Snacks": "Walnuts, dark chocolate, pomegranate juice",
                "Physical Activity": "Brisk walking, swimming",
                "Yoga & Meditation": "Slow yoga (Shavasana, Anulom Vilom)",
                "Sleep": "🛏️ 10:30 PM – 6:00 AM",
                "Supplements": "Omega-3, CoQ10, Magnesium",
                "Bonus Tips": "Limit sodium intake, avoid processed foods, and stay physically active."
            }
        elif schedule == "night":
            advice_data["advice"] = {
                "Wake-Up Routine": "🌙 4:30 PM – Warm herbal tea, light yoga",
                "Breakfast": "Oatmeal + nuts + berries",
                "Lunch": "Brown rice + lean protein + leafy greens",
                "Dinner": "Steamed fish + quinoa",
                "Snacks": "Banana, almonds",
                "Physical Activity": "Light strength training",
                "Yoga & Meditation": "Guided relaxation",
                "Sleep": "🛏️ 8:00 AM – 4:00 PM",
                "Supplements": "Ashwagandha, L-theanine",
                "Bonus Tips": "Limit sodium intake, avoid processed foods, and stay physically active."
            }
        elif schedule == "flexible":
            advice_data["advice"] = {
                "Wake-Up Routine": "☀️ 7:00 AM / 9:00 AM – Sunlight + deep breathing",
                "Breakfast": "Chia pudding + Greek yogurt",
                "Lunch": "Mixed greens + chicken + olive oil dressing",
                "Dinner": "Light meal with healthy fats",
                "Snacks": "Carrot sticks + hummus",
                "Physical Activity": "Cycling, yoga",
                "Yoga & Meditation": "Gratitude practice",
                "Sleep": "🛏️ 10:00 PM – 6:00 AM",
                "Supplements": "Garlic extract, Potassium",
                "Bonus Tips": "Limit sodium intake, avoid processed foods, and stay physically active."
            }

    elif category == "BMI":
        if schedule == "morning":
            advice_data["advice"] = {
                "Wake-Up Routine": "🌅 6:00 AM – Hydration + 5 min movement",
                "Breakfast": "High-protein (eggs, spinach, whole wheat)",
                "Lunch": "Grilled chicken + quinoa + salad",
                "Dinner": "Light meal (soup + salad)",
                "Snacks": "Apple + peanut butter, dark chocolate",
                "Physical Activity": "Strength training + HIIT",
                "Yoga & Meditation": "Power yoga, Surya Namaskar",
                "Sleep": "🛏️ 10:30 PM – 6:00 AM",
                "Supplements": "Green tea extract, CLA",
                "Bonus Tips": "Stay hydrated, get quality sleep, and avoid crash diets."
            }
        elif schedule == "night":
            advice_data["advice"] = {
                "Wake-Up Routine": "🌙 4:00 PM – Lemon water + stretching",
                "Breakfast": "Protein smoothie (whey, berries, nuts)",
                "Lunch": "Lentils + brown rice + steamed veggies",
                "Dinner": "Lean protein + non-starchy vegetables",
                "Snacks": "Greek yogurt, nuts",
                "Physical Activity": "Cardio + flexibility exercises",
                "Yoga & Meditation": "Breathing techniques",
                "Sleep": "🛏️ 8:00 AM – 4:00 PM",
                "Supplements": "Omega-3, L-carnitine",
                "Bonus Tips": "Stay hydrated, get quality sleep, and avoid crash diets."
            }
        elif schedule == "flexible":
            advice_data["advice"] = {
                "Wake-Up Routine": "☀️ 7:00 AM / 9:00 AM – Fasted walk",
                "Breakfast": "Omelet + whole grain toast",
                "Lunch": "Stir-fry veggies + tofu",
                "Dinner": "High-fiber meal",
                "Snacks": "Green tea, cottage cheese",
                "Physical Activity": "Weightlifting, dance, HIIT",
                "Yoga & Meditation": "Bodyweight yoga",
                "Sleep": "🛏️ 10:00 PM – 6:00 AM",
                "Supplements": "Protein powder, B-complex",
                "Bonus Tips": "Stay hydrated, get quality sleep, and avoid crash diets."
            }

    elif category == "healthy":
        if schedule == "morning":
            advice_data["advice"] = {
                "Wake-Up Routine": "🌅 6:00 AM – Lemon water, sun exposure",
                "Breakfast": "Scrambled eggs + avocado + greens",
                "Lunch": "Whole grains + lean protein + veggies",
                "Dinner": "Balanced (protein, fiber, healthy fats)",
                "Snacks": "Mixed nuts, fruit, yogurt",
                "Physical Activity": "Strength training, brisk walking",
                "Yoga & Meditation": "Cobra pose, Warrior pose, deep breathing",
                "Sleep": "🛏️ 10:30 PM – 6:00 AM",
                "Supplements": "Vitamin D, Probiotics",
                "Bonus Tips": "Prioritize mental health, stay hydrated, and avoid highly processed foods."
            }
        elif schedule == "night":
            advice_data["advice"] = {
                "Wake-Up Routine": "🌙 4:00 PM – Hydration, light exercise",
                "Breakfast": "Smoothie (berries, flaxseeds, nuts)",
                "Lunch": "Healthy wrap + nuts",
                "Dinner": "Light meal, herbal tea",
                "Snacks": "Dark chocolate, seeds",
                "Physical Activity": "Yoga, cardio",
                "Yoga & Meditation": "Relaxation techniques",
                "Sleep": "🛏️ 8:00 AM – 4:00 PM",
                "Supplements": "Adaptogens, Magnesium",
                "Bonus Tips": "Prioritize mental health, stay hydrated, and avoid highly processed foods."
            }
        elif schedule == "flexible":
            advice_data["advice"] = {
                "Wake-Up Routine": "☀️ 7:00 AM / 9:00 AM – Morning stretches",
                "Breakfast": "Oatmeal + almond butter",
                "Lunch": "Stir-fry + chicken",
                "Dinner": "Lean protein + veggies",
                "Snacks": "Green smoothie, hummus",
                "Physical Activity": "Cycling, swimming",
                "Yoga & Meditation": "Meditation, cold showers",
                "Sleep": "🛏️ 10:00 PM – 6:00 AM",
                "Supplements": "Multivitamins, Antioxidants",
                "Bonus Tips": "Prioritize mental health, stay hydrated, and avoid highly processed foods."
            }

    print(f"Generated advice: {advice_data}")  # Debugging
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
        print(f"Email sent to {email}")  # Debugging
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False