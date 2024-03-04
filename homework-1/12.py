# Get birth year from years old

import datetime

years_old = int(input("Enter your age: "))
today_year = datetime.date.today().year

print(f"You were born in {today_year - years_old}")
