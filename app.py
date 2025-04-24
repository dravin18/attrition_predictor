import streamlit as st
import utils

st.title("Akaike Attrition Predictor")

age = st.slider('Age', min_value=18, max_value=60, value=30)
business_travel = st.selectbox('Travel', options=['Travel_Rarely', 'Travel_Frequently', 'Non-Travel'])
daily_rate = st.number_input('DailyRate', min_value=100, max_value=1500, value=1000)
department = st.selectbox('Department', options=['Sales', 'Research & Development', 'Human Resources'])

distance = st.slider('Distance', min_value=1, max_value=30, value=5)
education = st.slider('Education', min_value=1, max_value=5, value=3)
education_field = st.selectbox('Edu Field', options=['Life Sciences', 'Medical', 'Marketing', 'Technical Degree', 'Other', 'Human Resources'])
env_satisfaction = st.slider('EnvSat', min_value=1, max_value=4, value=3)

gender = st.selectbox('Gender', options=['Male', 'Female'])
hourly_rate = st.number_input('HourlyRate', min_value=30, max_value=100, value=60)
job_involvement = st.slider('JobInv', min_value=1, max_value=4, value=3)
job_level = st.slider('JobLvl', min_value=1, max_value=5, value=2)

job_role = st.selectbox('Job Role', options=[
    'Sales Executive', 'Research Scientist', 'Laboratory Technician',
    'Manufacturing Director', 'Healthcare Representative', 'Manager',
    'Sales Representative', 'Research Director', 'Human Resources'])
job_satisfaction = st.slider('JobSat', min_value=1, max_value=4, value=3)
marital_status = st.selectbox('Marital', options=['Single', 'Married', 'Divorced'])
monthly_income = st.number_input('MonthInc', min_value=1000, max_value=20000, value=5000)
monthly_rate = st.number_input('MonthRate', min_value=2000, max_value=27000, value=20000)
num_companies = st.slider('NumComp', min_value=0, max_value=10, value=1)

overtime = st.selectbox('Overtime', options=['Yes', 'No'])
percent_hike = st.slider('Hike%', min_value=10, max_value=25, value=15)
performance_rating = st.slider('Perf', min_value=1, max_value=4, value=3)
rel_satisfaction = st.slider('RelSat', min_value=1, max_value=4, value=3)
stock_option = st.slider('StockOpt', min_value=0, max_value=3, value=1)
total_work_years = st.slider('TotWorkYrs', min_value=0, max_value=40, value=8)
training_times = st.slider('TrainYrs', min_value=0, max_value=6, value=3)
work_life_balance = st.slider('WLB', min_value=1, max_value=4, value=3)
years_at_company = st.slider('YrsCompany', min_value=0, max_value=40, value=5)
years_in_role = st.slider('YrsInRole', min_value=0, max_value=20, value=3)
years_since_promo = st.slider('YrsSincePromo', min_value=0, max_value=20, value=1)
years_with_mgr = st.slider('YrsWithMgr', min_value=0, max_value=20, value=2)

if st.button("Predict"):
    input_dict = {
    'Age': age,
    'BusinessTravel': business_travel,
    'DailyRate': daily_rate,
    'Department': department,
    'DistanceFromHome': distance,
    'Education': education,
    'EducationField': education_field,
    'EnvironmentSatisfaction': env_satisfaction,
    'Gender': gender,
    'HourlyRate': hourly_rate,
    'JobInvolvement': job_involvement,
    'JobLevel': job_level,
    'JobRole': job_role,
    'JobSatisfaction': job_satisfaction,
    'MaritalStatus': marital_status,
    'MonthlyIncome': monthly_income,
    'MonthlyRate': monthly_rate,
    'NumCompaniesWorked': num_companies,
    'OverTime': overtime,
    'PercentSalaryHike': percent_hike,
    'PerformanceRating': performance_rating,
    'RelationshipSatisfaction': rel_satisfaction,
    'StockOptionLevel': stock_option,
    'TotalWorkingYears': total_work_years,
    'TrainingTimesLastYear': training_times,
    'WorkLifeBalance': work_life_balance,
    'YearsAtCompany': years_at_company,
    'YearsInCurrentRole': years_in_role,
    'YearsSinceLastPromotion': years_since_promo,
    'YearsWithCurrManager': years_with_mgr,
}
    prediction = utils.running_model(input_dict)
    st.write(f"Prediction if employee will leave : {prediction}")