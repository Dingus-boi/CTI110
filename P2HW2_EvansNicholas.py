#Nicholas Evans
#06 March 2024
#P2HW2
#A program that accepts float inputs and outputs the lowest grade, highest grade, sum of grades, and grade average using a list.

#module_scores = list of module grades
#module grade = input (score)
#score appended to module_scores
#grade average = sum of module_scores / length of module_scores

#!/usr/bin/env python3


module_scores = []

score = float(input('Enter grade for Module 1: '))
module_scores.append(score)
score = float(input('Enter grade for Module 2: '))
module_scores.append(score)
score = float(input('Enter grade for Module 3: '))
module_scores.append(score)
score = float(input('Enter grade for Module 4: '))
module_scores.append(score)
score = float(input('Enter grade for Module 5: '))
module_scores.append(score)
score = float(input('Enter grade for Module 6: '))
module_scores.append(score)

print('\n-------Results-------')
print('Lowest Grade:  ', min(module_scores))
print('Highest Grade: ', max(module_scores))
print('Sum of Grades: ', sum(module_scores))
print('Average:       ', f'{(sum(module_scores) / len(module_scores)):.2f}')
print('-----------------------')
