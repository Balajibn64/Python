age = int(input("Enter your age: "))
if age < 0:
 print("Age cannot be negative. Please enter a valid age.")
elif age == 0:
 print("You are just a baby!")
elif 0 < age < 18:
 print("You are a minor.")
elif 18 <= age < 65:
 print("You are an adult.")
else:
 print("You are a senior citizen.")