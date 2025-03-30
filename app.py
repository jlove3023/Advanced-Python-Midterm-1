import streamlit as st 
from fitness_utils import log_workout, get_total_calories, get_workout_history

st.title("Fitness Tracker")

# Workout logging  
st.header("Log a Workout")
exercise = st.text_input("Exercise Name")
duration = st.number_input("Duration (minutes)", min_value=1)
calories = st.number_input("Calories Burned", min_value=0)

if st.button("Add Workout"):
    log_workout(exercise, duration, calories)
    st.success("Workout added successfully")

# Workout History
st.header("Workout History")
history = get_workout_history()

if history:
    for entry in history: 
     st.write(f"{entry['date']} - {entry['exercise']} ({entry['duration']} min) - {entry['calories']} kcal")
else: 
   st.info("No workouts logged yet. Start tracking your workouts")
   
# Total Calories Burned 
st.header("Total Calories Burned")
st.write(f"{get_total_calories()} kcal") 
