# Nicholas Evans

# April 25 2024

# P5HW

# Math quiz game utilizing functions and while loops
# Functions add_function and sub_function contain code for adding/subtracting games
# While loops iterate through failure states and tallies the number of guesses until the correct answer is given
# main while loop cycles through adding/subtracting games, calling each as a function, until the
# termination command is entered

# !/usr/bin/env python3

import random

def add_function():
	int_1 = random.randint(1, 100)
	int_2 = random.randint(1, 100)
	answer = int_1 + int_2
	i = 1
	print(f'  {int_1}')
	print(f'+ {int_2}')
	print('\nEnter answer.')
	user_guess = int(input())
	
	result = int(answer) - int(user_guess)

	while result != 0:
		if result > 0:
			print('Sorry, guess is too low.')
			i += 1
			user_guess = (input('Try again: '))
			result = int(answer) - int(user_guess)
		elif result < 0:
			print('Sorry, guess is too high.')
			i += 1
			user_guess = (input('Try again: '))
			result = int(answer) - int(user_guess)
			
	print('Congradulations!!!! Your answer is correct.')
	print(f'Number of guesses: {i}')

	rtn_str = ''
	return rtn_str

def sub_function():
	int_1 = random.randint(1, 100)
	int_2 = random.randint(1, 100)
	answer = int_1 - int_2
	i = 1
	print(f'  {int_1}')
	print(f'- {int_2}')
	print('\nEnter answer.')
	user_guess = int(input())
	
	result = int(answer) - int(user_guess)

	while result != 0:
		if result > 0:
			print('Sorry, guess is too low.')
			i += 1
			user_guess = (input('Try again: '))
			result = int(answer) - int(user_guess)
		elif result < 0:
			print('Sorry, guess is too high.')
			i += 1
			user_guess = (input('Try again: '))
			result = int(answer) - int(user_guess)
			
	print('Congradulations!!!! Your answer is correct.')
	print(f'Number of guesses: {i}')

	rtn_str = ''
	return rtn_str

print('Welcome to Math Quiz\n')
print('MAIN MENU')
print('----------------------------------------------------------')
print('1. Adding Random Numbers\n2. Subtracting Random Numbers\n3. Exit')
user_input = (input('Please choose one of the menu options: '))

while int(user_input) != 3:
	if int(user_input) == 1:
		print(f'{add_function()}')
		print('MAIN MENU')
		print('----------------------------------------------------------')
		print('1. Adding Random Numbers\n2. Subtracting Random Numbers\n3. Exit')
		user_input = (input('Please choose one of the menu options: '))
	
	elif int(user_input) == 2:
		print(f'{sub_function()}')
		print('MAIN MENU')
		print('----------------------------------------------------------')
		print('1. Adding Random Numbers\n2. Subtracting Random Numbers\n3. Exit')
		user_input = (input('Please choose one of the menu options: '))
		
	elif (int(user_input) != 3) or (int(user_input) != 2) or (int(user_input) != 1):
		print('!!ERROR!!\n1, 2, and 3 ARE ONLY ACCEPTABLE COMMANDS!!')
		user_input = input()
	
if int(user_input) == 3:
	print('Thank you for playing...\nBye!!')
