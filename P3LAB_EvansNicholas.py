#Nicholas Evans
#14 March 2024
#P3Lab
#Determines if a year is a leap year or not using if/else and true/false statements.
#determine if input is divisible by 4, and if so, if it is also divisible by 100
#if input is divisible by 4 and NOT by 100, input is a leap year (it is divisible by 4 and not a century year: eg, 2024)
#determine if input is divisible by 100 and NOT by 400
#if input IS divisible by 100 and NOT divisible by 400, it is a century year but NOT a leap year (1700 is divisible by both 4 and 100, but not by 400)
#if input IS divisible by both 100 AND 400, it is a century leap year (1600, 2000, 1200)


#!/usr/bin/env python3

is_leap_year = False
   
input_year = int(input())

if (input_year % 4 == 0) and (input_year % 100 != 0):
    is_leap_year = True
elif (input_year % 100 == 0) and (input_year % 400 != 0): 
    is_leap_year = False
elif (input_year % 100 == 0) and (input_year % 400 == 0):
    is_leap_year = True

if is_leap_year == True:
    print(input_year, '- leap year')
else:
    print(input_year, '- not a leap year')
