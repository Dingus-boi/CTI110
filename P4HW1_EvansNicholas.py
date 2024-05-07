#Nicholas Evans
#April 12 2024
#P4HW1
#score calculator using loops.


#ask user for number of inputs
#create a loop to obtain the specified number of test scores
	#evaluate if the input is valid - between 0 and 100
	#if it is not valid, print a notification and ask for a valid input
#add valid scores to list
#display lowest score
#display all scores after dropping lowest score
#average score after dropping lowest score
#display a letter grade

#!/usr/bin/env python3

number_scores = 0							#number of scores entered

loop_it = 1								#iteration of score entry loop

score_list = []								#list containing entered scores

input_validity = "true"							#true/false value needed for input validation loop

grade = "tbd"								#letter grade displayed at the end of the program


number_scores = int(input('How many scores do you want to enter? '))

while loop_it <= number_scores:						#loop iteration counter based on number of scores input by user
	score = float(input(f'Enter score #{loop_it}: '))

	if (score >= 0) and (score <= 100):
		input_validity = "true"
		score_list.append(score)
		loop_it += 1
	elif (score < 0) or (score > 100):				#initial output for invalid score input
		input_validity = "false"
		print('INVALID Score entered!!!!\nScore should be between 0 and 100')
		score = float(input(f'Enter score #{loop_it} again: '))
		while input_validity == "false":			#loop for repeated invalid scores
			if (score < 0) or (score > 100):
				print('INVALID Score entered!!!!\nScore should be between 0 and 100')
				score = float(input(f'Enter score #{loop_it} again: '))
			elif (score >= 0) and (score <= 100):		#breaks invalid input loop and appends valid score to score_list
				score_list.append(score)
				input_validity = "true"
				loop_it += 1
				

print('-----------------Results----------------')
print(f'lowest score   : {min(score_list)}')
score_list.remove(min(score_list))	
print(f'Modified list  : {score_list}')
print(f'Scores Average : {(sum(score_list) / len(score_list)):.2f}')


#logic that calculates grade from score averages

avg_grade = (sum(score_list) / len(score_list))

if avg_grade >= 90:
	grade = "A"
elif (avg_grade >= 80) and (avg_grade <= 89.9):
	grade = "B"
elif (avg_grade >= 71) and (avg_grade <= 79.9):
	grade = "C"
elif (avg_grade >= 60) and (avg_grade <= 70.9):
	grade = "D"
elif avg_grade <= 59.9:
	grade = "F"

print(f'Grade          : {grade}')
print('--------------------------------------------')
	




