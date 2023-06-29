"""
File: bmi_1.py
Author: Becky Wong
Date completed: 4/11/23
Description: Program calculates BMI with user input of weight (lbs) and height (inches)
"""

# Prompt user for weight (lbs) and height (inches)
weight_lb = int(input("Enter weight in lbs: "))
height_inches = int(input("Enter height in inches: "))

# Convert weight and height to kg and meters, respectively
weight_kg = weight_lb * 0.454
height_meters = height_inches * 0.0254

# Calculate bmi
bmi = (weight_kg) / (height_meters ** 2)

# Print CDC standard weight categories
if bmi < 18.5:
    print(f"BMI is {bmi}, CDC weight status category is underweight")
elif 18.5 <= bmi <= 24.9:
    print(f"BMI is {bmi}, CDC weight status category is normal")
elif 25.0 <= bmi <= 29.9:
    print(f"BMI is {bmi}, CDC weight status category is overweight")
else:
    print(f"BMI is {bmi}, CDC weight status category is obese")