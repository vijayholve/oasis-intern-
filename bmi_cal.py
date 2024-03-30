name=input("enter your name :")
weight=int(input(f"{name},enter weight in kilograms :"))
height=int(input(f"{name},enter height in meters:"))
bmi = weight / (height ** 2)
print(bmi)

if bmi>0:
    if bmi < 18.5:
        print("Underweight")
    elif 18.5 <= bmi < 25:
        print("Normal weight")
    elif 25 <= bmi < 30:
        print("overweight")
    else:
        print("Obese")
else:
    print("Enter valid input")