import datetime
import random

# Simulated "databases"
users = {}
workout_log = {}
macro_log = {}

def validate_user(username, password):
    return users.get(username) == password

def register_user(username, password):
    if username in users:
        return False
    users[username] = password
    workout_log[username] = []
    macro_log[username] = []
    return True

def log_workout(username, exercise, duration, calories):
    workout_log[username].append({
        'date': datetime.date.today().isoformat(),
        'exercise': exercise,
        'duration': duration,
        'calories': calories
    })

def get_total_calories(username):
    return sum(w['calories'] for w in workout_log.get(username, []))

def get_workout_history(username):
    return workout_log.get(username, [])

def get_workout_recommendation():
    recommendations = ["Push-ups", "Jumping Jacks", "Plank", "Squats", "Jogging"]
    return random.choice(recommendations)

def log_macros(username, carbs, protein, fat):
    macro_log[username].append({
        'date': datetime.date.today().isoformat(),
        'carbs': carbs,
        'protein': protein,
        'fat': fat
    })

def get_total_macros(username):
    data = macro_log.get(username, [])
    return {
        'carbs': sum(d['carbs'] for d in data),
        'protein': sum(d['protein'] for d in data),
        'fat': sum(d['fat'] for d in data),
    }

def calculate_bmi(height_cm, weight_kg):
    height_m = height_cm / 100
    return weight_kg / (height_m ** 2)

