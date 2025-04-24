import joblib
import pandas as pd
import xgboost
import os
import sklearn

current_file_path = os.path.realpath(__file__)
cwd = os.path.dirname(current_file_path)
scaler_model_path = os.path.join(cwd,'models/scaler.pkl')
scaler_loaded = joblib.load(scaler_model_path)

def create_derived_features(df):
    df['Stability'] = df['YearsInCurrentRole'] / (df['YearsAtCompany'] + 1e-6)
    df['PromotionRate'] = df['YearsSinceLastPromotion'] / (df['YearsAtCompany'] + 1e-6)
    df['IncomePerYear'] = df['MonthlyIncome'] * 12 / (df['TotalWorkingYears'] + 1e-6)
    df['IsManager'] = (df['JobLevel'] >= 4).astype(int)
    df['LoyaltyIndex'] = df['YearsWithCurrManager'] / (df['TotalWorkingYears'] + 1e-6)
    df['JobHopRate'] = df['NumCompaniesWorked'] / (df['TotalWorkingYears'] + 1e-6)
    df['IsRecentlyPromoted'] = (df['YearsSinceLastPromotion'] <= 2) .astype(int)
    df['IsNewJoiner'] = (df['YearsAtCompany'] <= 2).astype(int)
    return df


numerical_cols = ["Age","BusinessTravel","DailyRate","DistanceFromHome","Education","EnvironmentSatisfaction",
                  "HourlyRate","JobInvolvement","JobLevel","JobSatisfaction","MonthlyIncome","MonthlyRate","NumCompaniesWorked",
                  "PercentSalaryHike","PerformanceRating","RelationshipSatisfaction","StockOptionLevel","TotalWorkingYears",
                  "TrainingTimesLastYear","WorkLifeBalance","YearsAtCompany","YearsInCurrentRole","YearsSinceLastPromotion","YearsWithCurrManager"]


useless_cols = ['EmployeeCount', 'EmployeeNumber', 'Over18', 'StandardHours']


def preprocessing(df,original_df):

    business_travel_map = {
        'Non-Travel': 0,
        'Travel_Rarely': 1,
        'Travel_Frequently': 2
    }

    overtime_map = {
        'No': 0,
        'Yes': 1
    }

    attrition_map = {
        'No': 0,
        'Yes': 1
    }


    df["BusinessTravel"] = df["BusinessTravel"].map(business_travel_map)
    df["OverTime"] = df["OverTime"].map(overtime_map)
    df = pd.get_dummies(df, columns=["Department","EducationField","Gender","JobRole","MaritalStatus"], drop_first=False,dtype=float)
    return df


def scale_data(df):
    df_scaled = df.copy()
    df_scaled[numerical_cols] = scaler_loaded.transform(df_scaled[numerical_cols])
    return df_scaled

def running_model(input_dict):
    current_file_path = os.path.realpath(__file__)
    cwd = os.path.dirname(current_file_path)

    data_path = os.path.join(cwd,'data/WA_Fn-UseC_-HR-Employee-Attrition.csv')
    df_original = pd.read_csv(data_path)
    input_df = pd.DataFrame(input_dict,index=[0])

    input_df = create_derived_features(input_df)
    input_df = preprocessing(input_df,df_original)

    model_path = os.path.join(cwd,'models/model.pkl')
    model_columns_path = os.path.join(cwd,'models/model_columns.pkl')
    model_loaded  = joblib.load(model_path)
    model_columns = joblib.load(model_columns_path)

    for col in model_columns:
        if col not in input_df.columns:
            input_df[col] = 0

    input_df = input_df[model_columns]
    input_df = scale_data(input_df)
    prediction = model_loaded.predict(input_df)[0]

    prediction = "Yes" if prediction == 1 else "No"
    return prediction