#Example-1
#if = Do some code only if some condition is True
# Else do something else
 
age = int(input("Enter your age: "))
if age >= 100:
  print ("You are too old to sign up")
elif age >= 18:
  print ("You are now signed up")
elif age < 0:
  print ("You are not born yet")
else:
  print("You must be 18+ to signed up")

#Example-1

response = input("Do you like food? (Y/N): ")

if response == "Y":
  print("Have some food")
else:
  print("No food for you")

#Example-3

name = input("Enter Your name: ")

if name == "":
  print("You have not entered your name")
else:
  print(f"Hello {name}")

#Example-4 (Boolean)
for_sale = True
if for_sale:
  print("This item is for sale")
else:
  print("This item is for sale")
  
online = True
if online:
  print("The user is online")
else:
  print("The user is offline")












