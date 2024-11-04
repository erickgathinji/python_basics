#dates
from datetime import date, timedelta, datetime

today = date.today()
print(today)

#https://www.w3schools.com/python/python_datetime.asp
formatted_date = today.strftime("%A, %d-%b-%Y") #y gives two digits for year
print(formatted_date)

after_forty_days = today + timedelta(days=40) #(ctrl + click function to see description) if time back use - not +)
print(after_forty_days)

dob = "1999-02-26"
#convert to date object
date_of_birth = datetime.strptime(dob, "%Y-%m-%d") #strptime converts the string to date object
age = today.year - date_of_birth.year
print("I am ", age, " years old")

age_in_days = datetime.today() - date_of_birth
print("I am ", age_in_days, " days old")
print(age_in_days // 365)

