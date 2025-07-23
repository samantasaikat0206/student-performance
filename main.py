import streamlit as st
import numpy as np
import joblib

model =joblib.load("performance_model.pkl")

st.title("Students Performance Prediction")
st.markdown("---")

# 

# bedrooms =st.number_input("Enter the  bedroom values",min_value=0 ,value=0)
# bathrooms =st.number_input("Enter the  bathrooms values",min_value=0 ,value=0)
# living_area =st.number_input("Enter the living area",min_value=0 ,value=2000)
# Area =st.number_input("Enter the  area",min_value=0 ,value=2000)
# grade=st.number_input("Enter the grade",min_value=4 ,value=4)
# school =st.number_input("Enter the school",min_value=0 ,value=0)

Study_Hours_per_Week = st.number_input("Enter the study hours per week", min_value=0, max_value=70, value = 0)
Attendance_Rate = st.number_input("Enter the attendance rate (0-100)", min_value=0, max_value=100, value=0)
Past_Exam_Scores = st.number_input("Enter the past exam scores (0-100)", min_value=0, max_value=100, value=0)
Final_Exam_Score = st.number_input("Enter the final exam score (0-100)", min_value=0, max_value=100, value=0)
# Pass_Fail = st.selectbox("Select Pass/Fail", options=["Pass", "Fail"])

st.markdown("---")

X=[[Study_Hours_per_Week,	Attendance_Rate,	Past_Exam_Scores,	Final_Exam_Score]]

prediction=st.button("Predict")

if prediction:
    X_array=np.array(X)
    a=model.predict(X_array)
    if a[0] == 1:
        st.success("The student is likely to pass.")
    else:
        st.error("The student is likely to fail.")