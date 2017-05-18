 from datetime import date 
2 import calendar 
3 current_year=int(input("Enter current year; ")) 
4 day=int(input("Enter date of birth(1-31); ")) 
5 month=int(input("Enter the month you were born in(1-12); ")) 
6 age=int(input("Enter your age; ")) 
7 x=int(input("Enter 1 if your birthday has passed this year else 2")) 
8 if x==1: 
9   year=current_year-age 
10 else: 
11   year=current_year-age-1 
12 birthday=date(year, month, day) 
13 print(birthday.strftime("You were born on %d %A %b %Y")) 
14 input("Press enter") 
