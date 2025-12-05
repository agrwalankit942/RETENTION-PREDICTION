import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("job_change_model.pkl")

# Streamlit UI
st.title("🔍 Job Change Prediction App")
st.write("Enter the candidate's details to predict if they will change jobs.")

# User input fields
city_development_index = st.number_input("City Development Index(Standardized)", min_value=-3.0, max_value=3.0, step=0.01)
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
relevent_experience = st.selectbox("Relevant Experience", ["Has experience", "No experience"])
enrolled_university = st.selectbox("Enrolled in University", ["No enrollment", "Full time", "Part time"])
education_level = st.selectbox("Education Level", ["Primary School", "High School", "Graduate", "Masters", "Phd"])
major_discipline = st.selectbox("Major Discipline", ["STEM", "Business", "Arts", "Other"])
experience = st.number_input("Years of Experience", min_value=0, max_value=20, step=1)
experience_bin = st.slider("Experience Bin", min_value=0, max_value=5, step=1)
company_size = st.selectbox("Company Size", ["<10", "10-50", "50-100", "100-500", "500-1000", "1000-5000", "5000-10000", "10000+"])
company_type = st.selectbox("Company Type", ["Startup", "Product", "Service", "Other"])
last_new_job = st.number_input("Years Since Last Job", min_value=0, max_value=5, step=1)
training_hours = st.number_input("Training Hours", min_value=0, max_value=500, step=1)

# Convert categorical values to match the model's encoding
gender_mapping = {"Male": 0, "Female": 1, "Other": 2}
relevent_experience_mapping = {"Has experience": 1, "No experience": 0}
enrolled_university_mapping = {"No enrollment": 0, "Full time": 1, "Part time": 2}
education_level_mapping = {"Primary School": 0, "High School": 1, "Graduate": 2, "Masters": 3, "Phd": 4}
major_discipline_mapping = {"STEM": 0, "Business": 1, "Arts": 2, "Other": 3}
company_size_mapping = {"<10": 0, "10-50": 1, "50-100": 2, "100-500": 3, "500-1000": 4, "1000-5000": 5, "5000-10000": 6, "10000+": 7}
company_type_mapping = {"Startup": 0, "Product": 1, "Service": 2, "Other": 3}

# Prepare input data for prediction
input_data = pd.DataFrame({
    'city_development_index': [city_development_index],
    'gender': [gender_mapping[gender]],
    'relevent_experience': [relevent_experience_mapping[relevent_experience]],
    'enrolled_university': [enrolled_university_mapping[enrolled_university]],
    'education_level': [education_level_mapping[education_level]],
    'major_discipline': [major_discipline_mapping[major_discipline]],
    'experience': [experience],
    'experience_bin': [experience_bin],
    'company_size': [company_size_mapping[company_size]],
    'company_type': [company_type_mapping[company_type]],
    'last_new_job': [last_new_job],
    'training_hours': [training_hours]
})

required_columns = model.feature_name_ 
for col in required_columns:
    if col not in input_data.columns:
        input_data[col] = 0 

input_data = input_data[required_columns]

# Predict
if st.button("Predict Job Change"):
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.success("🔴 The candidate is likely to change job.")
    else:
        st.success("🟢 The candidate is not like  to change job.")
