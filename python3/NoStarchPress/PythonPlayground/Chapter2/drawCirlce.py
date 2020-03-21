#!/usr/bin/python
##########***************************************
#####-Nicholas-Stegelman-************************
#####-Created:2020-03-18-************************
#####-drawCircle.py-*****************************
#####-NoStarchPress: Python Playground-**********
###-A toy program taken from chapter 2 of a-*****
#-No Starch Press Book.-*************************
#-The purpose of the program is to draw a-*******
#-circle using the 'turtles' module-*************
#####-Version:1.00.0-****************************
#####-Updated:2020-03-18-************************

import math
import turtle

# A function that draws a cirlce with a turtle.
def turtleCircle(x, y, r):
  # Move turtle to start of circle
  turtle.up()
  turtle.setpos(x+r, y)
  turtle.down()
  # Begin Drawing
  for i in range(0, 365, 5):
    a = math.radians(i)
    turtle.setpos(x + r*math.cos(a), y + r*math.sin(a))

turtleCircle(100, 100, 50)
turtle.mainloop()