# Import Package
import rapidjson
import pandas as pd
import numpy as np
# JSON Object as String or Input as JSON file
json_str = '[{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 }, { "Gender": "Male", "HeightCm": 161, "WeightKg":85 }, { "Gender": "Male", "HeightCm": 180, "WeightKg": 77 }, { "Gender": "Female", "HeightCm": 166,"WeightKg": 62}, {"Gender": "Female", "HeightCm": 150, "WeightKg": 70}, {"Gender": "Female","HeightCm": 167, "WeightKg": 82}]'
data = rapidjson.loads(json_str) 
json_df = pd.DataFrame.from_records(data)
json_df["BMI"] = round((json_df["WeightKg"] / ((json_df["HeightCm"]/100)**2)),1)
Conditions_BMI = [(json_df['BMI'] <= 18.4),(json_df['BMI'] >= 18.5) & (json_df['BMI'] <= 24.9),(json_df['BMI'] >= 25) & (json_df['BMI'] <= 29.9),(json_df['BMI'] >= 30) & (json_df['BMI'] <= 34.9),(json_df['BMI'] >= 35) & (json_df['BMI'] <= 39.9),(json_df['BMI'] >= 40)]
Find_BMI_Category = ['Underweight', 'Normal weight', 'Overweight', 'Moderately obese', 'Severely obese', 'Very severely obese']
Find_Healthrisk = ['Malnutrition risk', 'Low risk', 'Enhanced risk', 'Medium risk', 'High risk', 'Very high risk']
json_df['BMI_Category'] = np.select(Conditions_BMI, Find_BMI_Category)
json_df['Health_risk'] = np.select(Conditions_BMI, Find_Healthrisk)
# Print Output
print("1. Output 1 - Adding 3 New Column")
print(json_df)
print("2. Output 2 - Count of Overweight category")
print("Count:" + str((json_df.BMI_Category.values == 'Overweight').sum()))
final_json = json_df.to_json(orient='records')
final_json = rapidjson.loads(final_json)
print("3. Output 3 - Back to JSON")
print(final_json)
