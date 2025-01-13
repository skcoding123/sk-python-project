# logical operators = evaluate multiple condition (or, and, not)
#            or = at least one condition must be true
#            and = both conditions must be true
#            not = inverts the condition (not False, not True)
#or
temp = 20
is_raining = True

if temp > 25 or temp < 0 or is_raining:
  print("The concert is cancelled")
else:
  print("The concert is on schedule")

#and
temp = 20
is_sunny = True

if temp >= 28 and is_sunny:
  print("Outside weather is HOT")
  print("Its sunny outside")
elif temp <= 0 and is_sunny:
  print("Outside weather is cool")
  print("Its sunny outside")

#not

temp = 20
is_sunny = True

if temp >= 28 and not is_sunny:
  print("Outside weather is HOT")
  print("Its sunny outside")
elif temp <= 0 and not is_sunny:
  print("Outside weather is cool")
  print("Its sunny outside")
