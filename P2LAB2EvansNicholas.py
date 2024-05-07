#Nicholas Evans
#March 01 2024
#P2LAB2

#calculate the product and average, converting between float and integer
#I did no such conversions, but my code passed all tests in the zybook lab
#I am not changing it


#!/usr/bin/env python3

num1 = float(input())
num2 = float(input())
num3 = float(input())
num4 = float(input())

product = num1 * num2 * num3 * num4
avg = (num1 + num2 + num3 + num4) / 4
print(f'{product:.0f}', f'{avg:.0f}')
print(f'{product:.3f}', f'{avg:.3f}')
