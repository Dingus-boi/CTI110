# Nicholas Evans
# 20 Feb 2024
# P1HW2
# A program for calculating travel expenses.

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
user_budget = int(input('\nEnter budget: '))

user_dest = (input('\nEnter your travel destination: '))

user_gas = int(input('\nEnter estimated gas expense: '))

user_lodge = int(input('\nEnter estimated lodging expense: '))

user_food = int(input('\nEnter estimated food expense: '))

final_expense = user_gas + user_lodge + user_food

print('\n-----Travel Expenses-----\n')
print('Your destination is: ', user_dest, '\nInitial Budget: ', user_budget)
print('\nFuel: ', user_gas, '\nLodging: ', user_lodge, '\nFood: ', user_food, '\n')
print('Your final expense is: ', final_expense)
print('Your remaining balance is: ', user_budget - final_expense)


