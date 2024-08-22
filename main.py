month = int(input())
day = int(input())

days_before = 0
days_in_month = 0

if month == 1:
    days_before = 0
    days_in_month = 31
elif month == 2:
    days_before = 31
    days_in_month = 29
elif month == 3:
    days_before = 60
    days_in_month = 31
elif month == 4:
    days_before = 91
    days_in_month = 30
elif month == 5:
    days_before = 121
    days_in_month = 31
elif month == 6:
    days_before = 152
    days_in_month = 30
elif month == 7:
    days_before = 182
    days_in_month = 31
elif month == 8:
    days_before = 213
    days_in_month = 31
elif month == 9:
    days_before = 244
    days_in_month = 30
elif month == 10:
    days_before = 274
    days_in_month = 31
elif month == 11:
    days_before = 305
    days_in_month = 30
elif month == 12:
    days_before = 335
    days_in_month = 31

if month >= 1 and month <= 12 and day >= 1 and day <= days_in_month :
    total_days = days_before + (day - 1)
     # January 1, 2024 is a Monday (1)
    day_of_week_number = (total_days + 1) % 7
    day_of_week = ""

    if day_of_week_number == 0:
        day_of_week = "Sunday"
    elif day_of_week_number == 1:
        day_of_week = "Monday"
    elif day_of_week_number == 2:
        day_of_week = "Tuesday"
    elif day_of_week_number == 3:
        day_of_week = "Wednesday"
    elif day_of_week_number == 4:
        day_of_week = "Thursday"
    elif day_of_week_number == 5:
        day_of_week = "Friday"
    elif day_of_week_number == 6:
        day_of_week = "Saturday"
    
    print(day_of_week)
else:
    print("Invalid Date")

