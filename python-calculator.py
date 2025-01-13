#python calculator (Youtube - 01:01:00)
operator = input("Enter an operator (+ - * /): ")
num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))

if operator == "+":
  result = num1 + num2
  print(f"The result is : {result}")
elif operator == "-":
  result = num1 - num2
  print("The result is : {result}")

elif operator == "*":
  result = num1 * num2
  print(f"The result is : {result}")

elif operator == "/":
  result = num1 / num2
  print(f"The result is : {result}")

else:
  print(f"The {operator} is not valid operator")

#python weight converter (pound to kg / kg to pound)

weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds? (K or L): ")

if unit == "K":
  weight = weight * 2.02
  unit = "Lbs"
  print (f"Your weight is: {round(weight, 1)} {unit}")
elif unit == "L":
  weight = weight / 2.02 
  unit = "Kg"
  print (f"Your weight is {round(weight, 1)} {unit}")
else:
  print (f"{unit} is not valid")

# Temprature conversion program

unit = input("Is this temprature in Celcius or Fahrenite? (C/F): ")
temp = float(input("Enter the temprature value: "))

if unit == "C":
  temp = 5/9 * ({temp} - 32)
  print(f"The temprature in fahrenite is: {temp}")
elif unit == "F":
  temp = (9/5) * temp + 32
  print(f"The temprature in celcius is: {temp}")
else:
  print(f"{unit} unit is invalid")




  









  
