# Write a program that categorizes BMI (Body Mass Index) into underweight (<18.5), normal weight (<24.9), overweight (<29.9) and obesity (<30.0). (formula = kg/m^2) 


weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

height_in_meters = height / 100

bmi = weight / (height_in_meters ** 2)

if bmi < 18.5:
    category = "Underweight"

elif bmi >= 18.5 and bmi < 24.9:
    category = "Normal weight"

elif bmi >= 24.9 and bmi < 29.9:
    category = "Overweight"

else:
    category = "Obesity"

print(f"Your BMI is {bmi}, which is categorized as {category}.")
