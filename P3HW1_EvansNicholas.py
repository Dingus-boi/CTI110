# Nicholas Evans
# P3HW1
# 14 March 2024
# program debugging.
# This program takes a number grade, determines average and displays letter grade for average.

#!/usr/bin/env python3


mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))


grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

lowest_grade = min(grades)
highest_grade = max(grades)
sum_grade = sum(grades)
avg_grade = sum_grade / 6

print('------Results------')
print(f'Lowest Grade:  {lowest_grade:.1f}')
print(f'Highest Grade: {highest_grade:.1f}')
print(f'Sum of Grades: {sum_grade:.1f}')
print(f'Average:       {avg_grade:.2f}')
print('-------------------')

if avg_grade >= 90:
	print('Your grade is: A')
elif (avg_grade >= 80) and (avg_grade <= 89.9):
	print('Your grade is: B')
elif (avg_grade >= 71) and (avg_grade <= 79.9):
	print('Your grade is: C')
elif (avg_grade >= 60) and (avg_grade <= 70.9):
	print('Your grade is: D')
elif avg_grade <= 59.9:
	print('Your grade is: F')






