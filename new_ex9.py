year=int(input("Enter a year :"))
if year%4==0 and year%100!=0 or year%400==0:
    print(f"Yoy Enter {year} a leap Year!")
else:
    print(f"You Enter {year} not a leap year!")