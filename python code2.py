

name = input("Enter your name: ")
yob = int(input("Enter your year of birth: "))

from datetime import datetime
current_year = datetime.now().year

age = current_year - yob

print("Name:", name)
print("Age:", age)

if age >= 60:
    print("Senior Citizen")
else:
    print("Not a Senior Citizen")
