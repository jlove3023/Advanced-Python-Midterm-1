import datetime

workout_log = []

def log_workout(exercise, duration, calories):
    """Logs a workout session."""
    workout_log.append({
        'date': datetime.date.today().strftime('%Y-%m-%d'),
        'exercise': exercise, 
        'duration': duration,
        'calories': calories
    })

def get_total_calories():
    """Returns total calories burned."""
    return sum(workout['calories'] for workout in workout_log)

def get_workout_history():
    """Returns logged workout sessions."""
    return workout_log
