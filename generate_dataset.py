import pandas as pd
import random

rows = []

for i in range(1,1001):

    age = random.randint(18,65)
    gender = random.choice(["Male","Female"])

    height = random.randint(150,190)
    weight = random.randint(45,110)

    bmi = round(weight / ((height/100)**2),2)

    heart = random.randint(60,120)

    steps = random.randint(1000,18000)

    exercise = random.randint(10,120)

    sleep = round(random.uniform(4,9),1)

    calories = int(weight*exercise*0.12 + random.randint(20,150))

    rows.append([
        i,
        age,
        gender,
        height,
        weight,
        bmi,
        heart,
        steps,
        exercise,
        sleep,
        calories
    ])

df = pd.DataFrame(rows,columns=[
"Patient_ID",
"Age",
"Gender",
"Height_cm",
"Weight_kg",
"BMI",
"Heart_Rate",
"Steps",
"Exercise_Minutes",
"Sleep_Hours",
"Calories_Burned"
])

df.to_csv("dataset/healthcare_dataset.csv",index=False)

print("Dataset Created Successfully")
print(df.head())