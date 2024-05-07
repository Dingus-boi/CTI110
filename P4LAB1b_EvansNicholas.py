#Nicholas Evans
#April 11 2024
#P4LAB1
#turtle graphics to write initials
#the turtle's name is still vedal

import turtle
wn = turtle.Screen()
vedal = turtle.Turtle()

vedal.color("green")
vedal.speed(1)

vedal.left(90)
vedal.forward(50)
vedal.right(145)
vedal.forward(55)
vedal.left(145)
vedal.forward(50)

vedal.penup()
vedal.right(180)
vedal.forward(50)
vedal.left(90)
vedal.forward(30)
vedal.pendown()

vedal.forward(50)
vedal.left(180)
vedal.forward(50)
vedal.right(90)
vedal.forward(25)
vedal.right(90)
vedal.forward(50)
vedal.left(180)
vedal.forward(50)
vedal.right(90)
vedal.forward(25)
vedal.right(90)
vedal.forward(50)


wn.mainloop()

