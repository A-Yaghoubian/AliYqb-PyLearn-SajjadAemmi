import turtle
import os
t = turtle.Turtle()
t.shape('turtle')

for i in range(6):
    t.penup()
    t.goto(0 + (8 * i), 0 - (8 * i))
    t.pendown()
    
    for j in range(i + 3):
        t.left(180 - ((i+1)*180)/(i+3)) 
        t.forward(40 + (12 * i))
        
os.system('PAUSE')
