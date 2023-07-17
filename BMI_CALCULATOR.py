# 🚨 Enter height and weight
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

# BMI calculator
BMI_cal = weight/(height*height)
if BMI_cal <18.5:
    BMI = round(BMI_cal,0)
    print(f"Your BMI is {BMI}, you are underweight.")
elif BMI_cal >18.5 and BMI_cal < 25:
    BMI = int(round(BMI_cal,0))
    print(f"Your BMI is {BMI}, you have a normal weight.")
elif BMI_cal > 25 and BMI_cal < 30:
    BMI = int(round(BMI_cal,0))
    print(f"Your BMI is {BMI}, you are slightly overweight.")
elif BMI_cal > 30 and BMI_cal < 35:
    BMI = int(round(BMI_cal,0))
    print(f"Your BMI is {BMI}, you are obese.")
elif BMI_cal > 35:
    BMI = int(round(BMI_cal,0))
    print(f"Your BMI is {BMI}, you are clinically obese.")