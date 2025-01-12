#python calculator
operator = input("Enter an operator (+ - * /): ")
num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))

if operator == "+":
  result = num1 + num2
  print(f"The result is : {result}")
elif operator == "-":
  result = num1 - num2
  print(f"The result is : {result}")

elif operator == "*":
  result = num1 * num2
  print(f"The result is : {result}")

elif operator == "/":
  result = num1 / num2
  print(f"The result is : {result}")

else:
  print(f"The {operator} is not valid operator")




  
