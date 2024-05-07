# Nicholas Evans
# 06 March 2024
# P2HW1
# A program for calculating travel expenses. Converts user input into a float and outputs expenses with two decimal places.

# enter budget (var_budget int): user input
# enter destination (var_destination string): user input
# gas expense (exp_gas int): user input
# lodging expense (exp_lodge int): user input
# food expense (exp_food int): user input
# exp_gas + exp_lodge + exp_food = total_expense
# remaining_bal = var_budget - total_expense
# ---Travel Expenses---
# Location: var_destination
# Budget: var_budget
# space
# Fuel: exp_gas
# Lodge: exp_lodge
# food: exp_food
# space
# final expense: total_expense
# remaining balance: remaining_bal 

#!/usr/bin/env python3

print('This program calculates and displays travel expenses.')
user_budget = float(input('\nEnter budget: '))

user_dest = (input('\nEnter your travel destination: '))

user_gas = float(input('\nEnter estimated gas expense: '))

user_lodge = float(input('\nEnter estimated lodging expense: '))

user_food = float(input('\nEnter estimated food expense: '))

final_expense = user_gas + user_lodge + user_food
remaining_bal = user_budget - final_expense
print('\n-----Travel Expenses-----\n')
print('Your destination is: ', user_dest, '\nInitial Budget: $' f'{user_budget:.2f}')
print('\nFuel: $' f'{user_gas:.2f}', '\nLodging: $' f'{user_lodge:.2f}', '\nFood: $' f'{user_food:.2f}', '\n')
print('Your final expense is: $' f'{final_expense:.2f}')
print('Your remaining balance is: $' f'{remaining_bal:.2f}')



