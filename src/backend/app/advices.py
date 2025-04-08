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
                "Breakfast Options": [
                    "1. Oats with banana, flaxseeds, and chamomile tea",
                    "2. Greek yogurt with berries and walnuts",
                    "3. Scrambled eggs with spinach and whole-grain toast"
                ],
                "Midday Break": "Walk/stretch (10 min)",
                "Lunch Options": [
                    "1. Salmon with quinoa and spinach salad with olive oil",
                    "2. Grilled chicken with sweet potato and steamed broccoli",
                    "3. Lentil soup with whole-grain bread and avocado"
                ],
                "Afternoon Relaxation": "Music, nature walk, journaling",
                "Evening Activity": "Gym (light cardio) or Tai Chi",
                "Dinner Options": [
                    "1. Magnesium-rich foods: Nuts, leafy greens, and brown rice",
                    "2. Baked turkey with roasted vegetables",
                    "3. Stir-fried tofu with mixed vegetables and quinoa"
                ],
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
                "Breakfast Options": [
                    "1. Eggs with avocado and a green smoothie",
                    "2. Oatmeal with almond butter and banana",
                    "3. Cottage cheese with pineapple and flaxseeds"
                ],
                "Midday Break": "Meditation (10 min)",
                "Lunch Options": [
                    "1. Chicken with brown rice and steamed vegetables",
                    "2. Quinoa salad with chickpeas and tahini dressing",
                    "3. Whole-grain wrap with turkey and vegetables"
                ],
                "Afternoon Relaxation": "Short nap, deep breathing",
                "Evening Activity": "Strength training (low intensity)",
                "Dinner Options": [
                    "1. Light meal with chamomile tea (soup and salad)",
                    "2. Baked cod with roasted asparagus",
                    "3. Stir-fried vegetables with tempeh"
                ],
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
                "Breakfast Options": [
                    "1. High-protein meal: Eggs with whole-grain toast and green tea",
                    "2. Smoothie bowl with protein powder and mixed toppings",
                    "3. Chia pudding with almond milk and fresh fruit"
                ],
                "Midday Break": "Hobby or deep breathing",
                "Lunch Options": [
                    "1. Home-cooked balanced meal: Protein + grains + vegetables",
                    "2. Buddha bowl with quinoa, roasted veggies, and tahini",
                    "3. Whole-grain pasta with chicken and vegetable sauce"
                ],
                "Afternoon Relaxation": "Socializing, creative activities",
                "Evening Activity": "Brisk walk, cycling, or dancing",
                "Dinner Options": [
                    "1. Protein + fiber-rich meal: Fish with lentils and greens",
                    "2. Stuffed bell peppers with lean ground turkey",
                    "3. Vegetable curry with brown rice"
                ],
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
                "Breakfast Options": [
                    "1. Oats with chia seeds, nuts, and eggs",
                    "2. Greek yogurt with berries and flaxseeds",
                    "3. Scrambled tofu with spinach and whole-grain toast"
                ],
                "Lunch Options": [
                    "1. Grilled chicken/fish with quinoa and leafy greens",
                    "2. Lentil soup with whole-grain bread",
                    "3. Turkey and avocado wrap with side salad"
                ],
                "Dinner Options": [
                    "1. Light meal: Soup with whole-grain bread",
                    "2. Baked salmon with roasted vegetables",
                    "3. Stir-fried tofu with broccoli and brown rice"
                ],
                "Snack Options": [
                    "1. Nuts (almonds, walnuts)",
                    "2. Hummus with vegetable sticks",
                    "3. Small piece of dark chocolate (85% cocoa)"
                ],
                "Physical Activity": "Walk after meals, strength training",
                "Yoga & Meditation": "Pranayama breathing, mindful eating",
                "Sleep": "🛏️ 10:30 PM – 6:00 AM",
                "Supplements": "Cinnamon, Berberine, Omega-3",
                "Bonus Tips": "Monitor blood sugar, maintain regular meal times, and avoid refined carbs."
            }
        elif schedule == "night":
            advice_data["advice"] = {
                "Wake-Up Routine": "🌙 4:00 PM – Hydration + mobility exercises",
                "Breakfast Options": [
                    "1. High-protein smoothie (Greek yogurt, berries, flaxseeds)",
                    "2. Scrambled eggs with avocado and whole-grain toast",
                    "3. Cottage cheese with nuts and cinnamon"
                ],
                "Lunch Options": [
                    "1. Brown rice with lentils and vegetables",
                    "2. Grilled chicken salad with olive oil dressing",
                    "3. Quinoa with roasted vegetables and tahini"
                ],
                "Dinner Options": [
                    "1. High-fiber meal: Vegetables with legumes",
                    "2. Baked cod with cauliflower rice",
                    "3. Turkey meatballs with zucchini noodles"
                ],
                "Snack Options": [
                    "1. Greek yogurt with almonds",
                    "2. Celery with peanut butter",
                    "3. Hard-boiled egg"
                ],
                "Physical Activity": "Light cardio before work",
                "Yoga & Meditation": "Gentle yoga before sleep",
                "Sleep": "🛏️ 8:00 AM – 4:00 PM",
                "Supplements": "Magnesium, Fenugreek",
                "Bonus Tips": "Monitor blood sugar, maintain regular meal times, and avoid refined carbs."
            }
        elif schedule == "flexible":
            advice_data["advice"] = {
                "Wake-Up Routine": "☀️ 7:00 AM / 9:00 AM – Yoga, 15 min walk",
                "Breakfast Options": [
                    "1. Scrambled tofu/chicken with whole-grain toast",
                    "2. Chia pudding with almond milk and nuts",
                    "3. Omelet with vegetables and feta cheese"
                ],
                "Lunch Options": [
                    "1. Salad with avocado and lean protein",
                    "2. Grilled salmon with roasted vegetables",
                    "3. Chicken and vegetable stir-fry with quinoa"
                ],
                "Dinner Options": [
                    "1. Protein-rich, low-carb meal: Fish with greens",
                    "2. Stuffed peppers with lean ground turkey",
                    "3. Cauliflower crust pizza with vegetables"
                ],
                "Snack Options": [
                    "1. Apple with peanut butter",
                    "2. Handful of mixed nuts",
                    "3. Cheese slices with cucumber"
                ],
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
                "Breakfast Options": [
                    "1. Whole-grain toast with avocado and eggs",
                    "2. Oatmeal with walnuts and banana",
                    "3. Greek yogurt with granola and berries"
                ],
                "Lunch Options": [
                    "1. Grilled salmon with spinach and sweet potato",
                    "2. Quinoa salad with chickpeas and vegetables",
                    "3. Turkey burger (no bun) with side salad"
                ],
                "Dinner Options": [
                    "1. Low-sodium soup with whole grains",
                    "2. Baked chicken with roasted vegetables",
                    "3. Stir-fried tofu with brown rice"
                ],
                "Snack Options": [
                    "1. Walnuts and dark chocolate",
                    "2. Sliced apple with almond butter",
                    "3. Pomegranate juice with mixed nuts"
                ],
                "Physical Activity": "Brisk walking, swimming",
                "Yoga & Meditation": "Slow yoga (Shavasana, Anulom Vilom)",
                "Sleep": "🛏️ 10:30 PM – 6:00 AM",
                "Supplements": "Omega-3, CoQ10, Magnesium",
                "Bonus Tips": "Limit sodium intake, avoid processed foods, and stay physically active."
            }
        elif schedule == "night":
            advice_data["advice"] = {
                "Wake-Up Routine": "🌙 4:30 PM – Warm herbal tea, light yoga",
                "Breakfast Options": [
                    "1. Oatmeal with nuts and berries",
                    "2. Scrambled eggs with whole-grain toast",
                    "3. Smoothie with spinach, banana, and flaxseeds"
                ],
                "Lunch Options": [
                    "1. Brown rice with lean protein and leafy greens",
                    "2. Lentil soup with whole-grain bread",
                    "3. Grilled chicken salad with olive oil dressing"
                ],
                "Dinner Options": [
                    "1. Steamed fish with quinoa",
                    "2. Vegetable stir-fry with tofu",
                    "3. Turkey meatballs with zucchini noodles"
                ],
                "Snack Options": [
                    "1. Banana with almonds",
                    "2. Greek yogurt with honey",
                    "3. Celery sticks with hummus"
                ],
                "Physical Activity": "Light strength training",
                "Yoga & Meditation": "Guided relaxation",
                "Sleep": "🛏️ 8:00 AM – 4:00 PM",
                "Supplements": "Ashwagandha, L-theanine",
                "Bonus Tips": "Limit sodium intake, avoid processed foods, and stay physically active."
            }
        elif schedule == "flexible":
            advice_data["advice"] = {
                "Wake-Up Routine": "☀️ 7:00 AM / 9:00 AM – Sunlight + deep breathing",
                "Breakfast Options": [
                    "1. Chia pudding with Greek yogurt",
                    "2. Avocado toast with poached eggs",
                    "3. Smoothie bowl with mixed toppings"
                ],
                "Lunch Options": [
                    "1. Mixed greens with chicken and olive oil dressing",
                    "2. Quinoa bowl with roasted vegetables",
                    "3. Whole-grain wrap with turkey and avocado"
                ],
                "Dinner Options": [
                    "1. Light meal with healthy fats: Salmon with greens",
                    "2. Stuffed bell peppers with lean ground turkey",
                    "3. Vegetable curry with brown rice"
                ],
                "Snack Options": [
                    "1. Carrot sticks with hummus",
                    "2. Handful of mixed nuts",
                    "3. Dark chocolate with almonds"
                ],
                "Physical Activity": "Cycling, yoga",
                "Yoga & Meditation": "Gratitude practice",
                "Sleep": "🛏️ 10:00 PM – 6:00 AM",
                "Supplements": "Garlic extract, Potassium",
                "Bonus Tips": "Limit sodium intake, avoid processed foods, and stay physically active."
            }

    elif category.lower()== "bmi":
        advice_data["category"] = "BMI"
        if schedule == "morning":
            advice_data["advice"] = {
                "Wake-Up Routine": "🌅 6:00 AM – Hydration + 5 min movement",
                "Breakfast Options": [
                    "1. High-protein: Eggs with spinach and whole wheat toast",
                    "2. Greek yogurt with granola and berries",
                    "3. Protein smoothie with banana and peanut butter"
                ],
                "Lunch Options": [
                    "1. Grilled chicken with quinoa and salad",
                    "2. Turkey and avocado wrap with side vegetables",
                    "3. Lentil soup with whole-grain bread"
                ],
                "Dinner Options": [
                    "1. Light meal: Soup with salad",
                    "2. Baked salmon with roasted vegetables",
                    "3. Stir-fried tofu with brown rice"
                ],
                "Snack Options": [
                    "1. Apple with peanut butter",
                    "2. Small portion of dark chocolate",
                    "3. Handful of mixed nuts"
                ],
                "Physical Activity": "Strength training + HIIT",
                "Yoga & Meditation": "Power yoga, Surya Namaskar",
                "Sleep": "🛏️ 10:30 PM – 6:00 AM",
                "Supplements": "Green tea extract, CLA",
                "Bonus Tips": "Stay hydrated, get quality sleep, and avoid crash diets."
            }
        elif schedule == "night":
            advice_data["advice"] = {
                "Wake-Up Routine": "🌙 4:00 PM – Lemon water + stretching",
                "Breakfast Options": [
                    "1. Protein smoothie (whey, berries, nuts)",
                    "2. Scrambled eggs with whole-grain toast",
                    "3. Oatmeal with protein powder and banana"
                ],
                "Lunch Options": [
                    "1. Lentils with brown rice and steamed veggies",
                    "2. Grilled chicken salad with olive oil dressing",
                    "3. Quinoa bowl with roasted vegetables"
                ],
                "Dinner Options": [
                    "1. Lean protein with non-starchy vegetables",
                    "2. Baked cod with cauliflower mash",
                    "3. Turkey meatballs with zucchini noodles"
                ],
                "Snack Options": [
                    "1. Greek yogurt with almonds",
                    "2. Cottage cheese with berries",
                    "3. Hard-boiled eggs"
                ],
                "Physical Activity": "Cardio + flexibility exercises",
                "Yoga & Meditation": "Breathing techniques",
                "Sleep": "🛏️ 8:00 AM – 4:00 PM",
                "Supplements": "Omega-3, L-carnitine",
                "Bonus Tips": "Stay hydrated, get quality sleep, and avoid crash diets."
            }
        elif schedule == "flexible":
            advice_data["advice"] = {
                "Wake-Up Routine": "☀️ 7:00 AM / 9:00 AM – Fasted walk",
                "Breakfast Options": [
                    "1. Omelet with whole grain toast",
                    "2. Chia pudding with almond milk and nuts",
                    "3. Protein pancakes with berries"
                ],
                "Lunch Options": [
                    "1. Stir-fry veggies with tofu",
                    "2. Grilled chicken with sweet potato and greens",
                    "3. Lentil salad with feta cheese"
                ],
                "Dinner Options": [
                    "1. High-fiber meal: Salmon with lentils",
                    "2. Stuffed peppers with lean ground turkey",
                    "3. Vegetable curry with brown rice"
                ],
                "Snack Options": [
                    "1. Green tea with almonds",
                    "2. Cottage cheese with cucumber",
                    "3. Protein bar (low sugar)"
                ],
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
                "Breakfast Options": [
                    "1. Scrambled eggs with avocado and greens",
                    "2. Greek yogurt with granola and berries",
                    "3. Smoothie bowl with mixed toppings"
                ],
                "Lunch Options": [
                    "1. Whole grains with lean protein and veggies",
                    "2. Quinoa salad with chickpeas and tahini",
                    "3. Grilled salmon with sweet potato and greens"
                ],
                "Dinner Options": [
                    "1. Balanced meal: Protein, fiber, healthy fats",
                    "2. Baked chicken with roasted vegetables",
                    "3. Stir-fried tofu with brown rice"
                ],
                "Snack Options": [
                    "1. Mixed nuts and fruit",
                    "2. Yogurt with honey and granola",
                    "3. Dark chocolate with almonds"
                ],
                "Physical Activity": "Strength training, brisk walking",
                "Yoga & Meditation": "Cobra pose, Warrior pose, deep breathing",
                "Sleep": "🛏️ 10:30 PM – 6:00 AM",
                "Supplements": "Vitamin D, Probiotics",
                "Bonus Tips": "Prioritize mental health, stay hydrated, and avoid highly processed foods."
            }
        elif schedule == "night":
            advice_data["advice"] = {
                "Wake-Up Routine": "🌙 4:00 PM – Hydration, light exercise",
                "Breakfast Options": [
                    "1. Smoothie (berries, flaxseeds, nuts)",
                    "2. Scrambled eggs with whole-grain toast",
                    "3. Oatmeal with almond butter and banana"
                ],
                "Lunch Options": [
                    "1. Healthy wrap with nuts",
                    "2. Grilled chicken salad with olive oil dressing",
                    "3. Lentil soup with whole-grain bread"
                ],
                "Dinner Options": [
                    "1. Light meal with herbal tea",
                    "2. Baked fish with quinoa and greens",
                    "3. Vegetable stir-fry with tofu"
                ],
                "Snack Options": [
                    "1. Dark chocolate and seeds",
                    "2. Greek yogurt with honey",
                    "3. Cottage cheese with pineapple"
                ],
                "Physical Activity": "Yoga, cardio",
                "Yoga & Meditation": "Relaxation techniques",
                "Sleep": "🛏️ 8:00 AM – 4:00 PM",
                "Supplements": "Adaptogens, Magnesium",
                "Bonus Tips": "Prioritize mental health, stay hydrated, and avoid highly processed foods."
            }
        elif schedule == "flexible":
            advice_data["advice"] = {
                "Wake-Up Routine": "☀️ 7:00 AM / 9:00 AM – Morning stretches",
                "Breakfast Options": [
                    "1. Oatmeal with almond butter",
                    "2. Avocado toast with poached eggs",
                    "3. Chia pudding with fresh fruit"
                ],
                "Lunch Options": [
                    "1. Stir-fry with chicken",
                    "2. Quinoa bowl with roasted vegetables",
                    "3. Whole-grain wrap with turkey and avocado"
                ],
                "Dinner Options": [
                    "1. Lean protein with veggies",
                    "2. Salmon with lentils and greens",
                    "3. Stuffed bell peppers with lean ground turkey"
                ],
                "Snack Options": [
                    "1. Green smoothie",
                    "2. Hummus with vegetable sticks",
                    "3. Mixed nuts and dried fruit"
                ],
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
    Send the generated advice to the user's email in a well-formatted HTML email.
    """
    try:
        # Format meal options as HTML lists
        formatted_advice = {}
        for key, value in advice.get("advice", {}).items():
            if isinstance(value, list):
                formatted_advice[key] = "<ul>" + "".join(f"<li>{item}</li>" for item in value) + "</ul>"
            else:
                formatted_advice[key] = value

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
                .advice-table {{
                    width: 100%;
                    border-collapse: collapse;
                    margin-top: 20px;
                }}
                .advice-table th, .advice-table td {{
                    border: 1px solid #ddd;
                    padding: 12px;
                    text-align: left;
                }}
                .advice-table th {{
                    background-color: #4ba2d5;
                    color: white;
                }}
                .advice-table tr:nth-child(even) {{
                    background-color: #f2f2f2;
                }}
                .footer {{
                    margin-top: 30px;
                    font-size: 14px;
                    color: #777;
                }}
                ul {{
                    margin: 0;
                    padding-left: 20px;
                }}
                li {{
                    margin-bottom: 5px;
                }}
            </style>
        </head>
        <body>
            <h1>Your Custom Health Advice</h1>
            <p>Here is your custom health advice based on your selected category and schedule:</p>

            <h2>Category: {advice.get("category", "N/A")}</h2>
            <h2>Schedule: {advice.get("schedule", "N/A")}</h2>

            <table class="advice-table">
                <tr>
                    <th>Activity</th>
                    <th>Details</th>
                </tr>
                {"".join(
                    f"<tr><td>{key}</td><td>{formatted_advice.get(key, '')}</td></tr>"
                    for key in advice.get("advice", {}).keys()
                )}
            </table>

            <div class="footer">
                <p>Thank you for using our Health Advisory Service!</p>
                <p>Regards,<br>Health Advisory Team</p>
            </div>
        </body>
        </html>
        """

        # Create the email message
        msg = Message(
            subject="Your Custom Health Advice",
            recipients=[email],
            html=html_body  # Use HTML for the email body
        )

        # Send the email
        mail.send(msg)
        print(f"Email sent to {email}")  # Debugging
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False