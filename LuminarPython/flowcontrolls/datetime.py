date=int(input("Enter your birth date"))
month=int(input("Enter your birth month"))
year=int(input("Enter your birth year"))

currentdate=23
currentmonth=7
currentyear=2020

age=(currentyear-year)

if(currentmonth<=month):
        age=age-1
print("age:",age)



