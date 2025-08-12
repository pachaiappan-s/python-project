print("BMI Calculator")

height_cm = float(input("Enter your height in centimeters: "))
weight = float(input("Enter your weight in kg: "))


height_m = height_cm / 100


bmi = weight / (height_m ** 2)
print("Your Body Mass Index is:", round(bmi, 2))

if bmi > 0:
    if bmi <= 16:
        print("You are severely underweight")
    elif bmi <= 18.5:
        print("You are underweight")
    elif bmi <= 25:
        print("You are normal weight")
    elif bmi <= 30:
        print("You are overweight")
    else:
        print("You are obese")
else:
    print("Enter valid details")