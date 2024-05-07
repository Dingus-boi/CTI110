#Nicholas Evans
#April 7 2024
#P4LAB1
#while loops make the turtle draw a square, then a triangle
#the turtle's name is vedal
#say hi to vedal

#!/usr/bin/env python3

import turtle
wn = turtle.Screen()
vedal = turtle.Turtle()

i = -1

while i <= 2:
	vedal.forward(50)
	vedal.left(90)
	i += 1
	
vedal.forward(100)

while i <= 5:
	vedal.left(120)
	vedal.forward(50)
	i += 1

wn.mainloop()


