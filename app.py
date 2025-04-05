import streamlit as st
from fitness_utils import (
    log_workout, get_total_calories, get_workout_history,
    get_workout_recommendation, log_macros, get_total_macros,
    calculate_bmi, validate_user, register_user
)
import pandas as pd
import matplotlib.pyplot as plt # type: ignore

# Session State for authentication
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
if 'username' not in st.session_state:
    st.session_state.username = ""

# Authentication
st.sidebar.title("Login / Register")
auth_mode = st.sidebar.radio("Choose mode", ["Login", "Register"])
username = st.sidebar.text_input("Username")
password = st.sidebar.text_input("Password", type="password")

if auth_mode == "Login":
    if st.sidebar.button("Login"):
        if validate_user(username, password):
            st.session_state.authenticated = True
            st.session_state.username = username
            st.success(f"Welcome back, {username}!")
        else:
            st.error("Invalid credentials")
else:
    if st.sidebar.button("Register"):
        if register_user(username, password):
            st.success("Registration successful. Please login.")
        else:
            st.error("Username already exists.")

if not st.session_state.authenticated:
    st.stop()

# --- Main App ---
st.title(f"Fitness Tracker - {st.session_state.username}")

# Workout Logging
st.header("Log a Workout")
exercise = st.text_input("Exercise")
duration = st.number_input("Duration (minutes)", min_value=1)
calories = st.number_input("Calories Burned", min_value=0)

if st.button("Add Workout"):
    log_workout(st.session_state.username, exercise, duration, calories)
    st.success("Workout added successfully.")

# Macronutrient Logging
st.header("Log Macronutrients")
carbs = st.number_input("Carbs (g)", min_value=0)
protein = st.number_input("Protein (g)", min_value=0)
fat = st.number_input("Fat (g)", min_value=0)

if st.button("Add Macronutrients"):
    log_macros(st.session_state.username, carbs, protein, fat)
    st.success("Macros added.")

# History & Charts
st.header("Workout History & Progress")
history = get_workout_history(st.session_state.username)
if history:
    df = pd.DataFrame(history)
    st.dataframe(df)

    st.subheader("Calories Over Time")
    fig, ax = plt.subplots()
    df['date'] = pd.to_datetime(df['date'])
    ax.plot(df['date'], df['calories'], marker='o')
    ax.set_xlabel("Date")
    ax.set_ylabel("Calories Burned")
    st.pyplot(fig)
else:
    st.info("No workouts logged yet.")

# Total Burn
st.header("Total Calories Burned")
st.write(f"{get_total_calories(st.session_state.username)} kcal")

# Macronutrient Totals
st.header("Macronutrient Summary")
macros = get_total_macros(st.session_state.username)
st.write(f"Carbs: {macros['carbs']}g, Protein: {macros['protein']}g, Fat: {macros['fat']}g")

# BMI Calculator
st.header("BMI Calculator")
height = st.number_input("Height (cm)", min_value=50)
weight = st.number_input("Weight (kg)", min_value=10)
if height and weight:
    bmi = calculate_bmi(height, weight)
    st.write(f"Your BMI: {bmi:.2f}")

# Recommendation
st.header("Workout Recommendation")
rec = get_workout_recommendation()
st.write(f"Try this: **{rec}**")

