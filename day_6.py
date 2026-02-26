birth_year = int(input("enter the year you were born in numbers only:"))
age = 2026 - int(birth_year)
if age <0 or age > 130:
    print("invalid input")
else:print("you will be: ", age ," years old in 2026")