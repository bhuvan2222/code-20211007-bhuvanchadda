bmi_data = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 }, { "Gender": "Male", "HeightCm": 161, "WeightKg":
85 }, { "Gender": "Male", "HeightCm": 180, "WeightKg": 77 }, { "Gender": "Female", "HeightCm": 166,
"WeightKg": 62}, {"Gender": "Female", "HeightCm": 150, "WeightKg": 70}, {"Gender": "Female",
"HeightCm": 167, "WeightKg": 82}]



for i in bmi_data:
    weight = i.get("WeightKg")
    height = i.get("HeightCm")
    height = (float)(height / 100)
    print(height)
    bmi = weight/(height ** 2)
    i['BMI']= bmi
    if bmi <= 18.4:
        i['Category'] = "Underweight"
        i['Health Risk'] = "Malnutrition risk"
    elif bmi >= 18.5 and bmi <= 24.9:
        i['Category'] = "Normal Weight"
        i['Health Risk'] = " Low risk"
    elif bmi >= 25 and bmi <= 29.9:
        i['Category'] = "Overweight"
        i['Health Risk'] = " Enhanced risk"
    elif bmi >= 30 and bmi <= 34.9:
        i['Category'] = "Moderately obese"
        i['Health Risk'] = " Medium risk"
    elif bmi >=35 and bmi <= 39.9:
        i['Category'] = " Severely obese"
        i['Health Risk'] = " High risk"
    else:
        i['Category'] = " Very severely obese"
        i['Health Risk'] = "Very high risk"
        
print(bmi_data)    