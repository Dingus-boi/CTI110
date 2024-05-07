# Nicholas Evans

# April 25 2024

# P5LAB

# Utilizes functions to determine if an input year is or is not a leap year

#!/usr/bin/env python3


def days_in_feb(user_year):
    days_feb = 28
    if (user_year % 4 == 0) and (user_year % 100 != 0):
        days_feb = 29
    elif (user_year % 100 == 0) and (user_year % 400 != 0):
        days_feb = 28
    elif (user_year % 100 == 0) and (user_year % 400 == 0):
        days_feb = 29
		
    return days_feb

if __name__ == '__main__':
    user_input = int(input())
    days_print = days_in_feb(user_input)

    print(f'{user_input} has {days_print} days in February.')
