
import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Student Placement Prediction", page_icon="🎓")

st.title("🎓 Student Placement Prediction")
st.write("Enter student details to predict placement status.")

@st.cache_resource
def load_model():
    return joblib.load("placement_model.pkl")

try:
    model = load_model()
except Exception:
    st.error("Model file not found. Please upload placement_model.pkl to GitHub.")
    st.stop()

with st.form("student_form"):
    gender = st.selectbox("Gender", ["Male", "Female"])
    city = st.selectbox("City", ["Ahmedabad", "Mumbai", "Kolkata", "Jaipur", "Pune", "Other"])
    college_tier = st.selectbox("College Tier", ["Tier1", "Tier2", "Tier3"])
    stream = st.selectbox("Stream", ["ECE", "IT", "CS", "Mechanical", "Civil", "Other"])
    specialisation = st.selectbox("Specialisation", ["Networking", "DataScience", "AI", "Other"])
    hostel = st.selectbox("Hostel", ["Yes", "No"])
    backlogs = st.selectbox("History Of Backlogs", ["Yes", "No"])

    cgpa = st.slider("CGPA", 0.0, 10.0, 7.0)
    attendance = st.slider("Attendance (%)", 0.0, 100.0, 80.0)
    internships = st.number_input("Internships", 0, 20, 1)
    projects = st.number_input("Projects", 0, 30, 2)
    workshops = st.number_input("Workshops", 0, 30, 2)
    certifications = st.number_input("Certifications", 0, 30, 2)
    publications = st.number_input("Publications", 0, 20, 0)
    aptitude = st.slider("Aptitude Test Score", 0.0, 100.0, 60.0)
    soft_skills = st.slider("Soft Skills Rating", 0.0, 5.0, 3.0)
    coding = st.slider("Coding Test Score", 0.0, 100.0, 60.0)
    interview = st.slider("Mock Interview Score", 0.0, 100.0, 60.0)
    extracurricular = st.selectbox("Extra Curricular", ["Yes", "No"])

    if st.form_submit_button("Predict Placement"):
        st.warning(
            "This demo needs all model input columns with the exact categories "
            "used during training. Please ensure the app input fields match "
            "the training dataset before using predictions."
        )
