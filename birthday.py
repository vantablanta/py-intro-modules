from datetime import date

age = int(input("Enter age "))
year = date.today().year

yob = year - age
print (yob)
y80 = yob + 80
print(y80)

