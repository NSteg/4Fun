#!/usr/bin/python
##########***************************************
#####-Nicholas-Stegelman-************************
#####-Created:2020-03-18-************************
#####-spiro.py-**********************************
#####-NoStarchPress: Python Playground-**********
###-A toy program taken from chapter 2 of a-*****
#-No Starch Press Book.-*************************
#-The purpose of the program is to replicate a-**
#-Spirograph using the 'turtles' module-*********
#####-Version:1.00.0-****************************
#####-Updated:2020-03-18-************************

import sys, random, argparse
import numpy as np
import math
import turtle
from PIL import Image
from datetime import datetime

descStr = "This program draws spirographs."

### THE SPIRO CONSTRUCTOR
##----------------------------------------------------------------------------
# A Class that Draws a Spirograph
class Spiro:
    # Define the Constructor
    def __init__ (self, xc, yc, col, R, r, l):
        #Create turtle object
        self.t = turtle.Turtle()
        #Set cursor shape
        self.t.shape('turtle')
        #Set step size -- In degrees
        self.step = 5
        #Set drawing complete flag
        self.drawingComplete = False

        #Set parameters
        self.setparams(xc, yc, col, R, r, l)

        #Initialize the drawing
        self.restart()
    # END_CONSTRUCTOR
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

    ### SETUP FUNCTIONS
    #   #---------------------------------------------------------------------
    # Set the parameters
    def setparams(self, xc, yc, col, R, r, l):
        # The Spirograph parameters
        self.xc = xc
        self.yc = yc
        self.col = col
        self.R = int(R)
        self.r = int(r)
        self.l = l
        # Reduce r/R to it's smallest form using the _G_reatest _C_ommon
            # _D_ivisor function 
            # -- fractions.gcd() is depricated; using math.gdc()
        gcdVal = math.gcd(self.r, self.R)
        self.nRot = self.r//gcdVal # Double slash is integer division
        # Get ratio of radii
        self.k = r/float(R)
        # Set the color
        self.t.color(*col)
        # Store Current Angle
        self.a = 0
    # END_SETPARAMS_FUNC
    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    ## The Restart Method
    # Restart the Drawing
    def restart(self):
        # Set Drawing Complete Flag
        self.drawingComplete = False
        # Show the turtle
        self.t.showturtle()
        # Go to First Point
        self.t.up()
        R, k, l = self.R, self.k, self.l
        a = 0.0
        x = R*((1-k)*math.cos(a) + l*k*math.cos((1-k) * a/k))
        y = R*((1-k)*math.sin(a) - l*k*math.sin((1-k) * a/k))
        self.t.setpos(self.xc + x, self.yc + y)
        self.t.down()
    # END_SPIRO.RESTART_FUNC
    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    ## The Draw Method
    # Draw the Thing
    def draw(self):
        # Draw the rest of the points
        R, k, l = self.R, self.k, self.l
        for i in range(0, 360*self.nRot + 1, self.step):
            a = math.radians(i)
            x = R*((1-k)*math.cos(a) + l*k*math.cos((1-k)* a/k))
            y = R*((1-k)*math.sin(a) - l*k*math.sin((1-k)* a/k))
            self.t.setpos(self.xc+x, self.yc+y)
        # END_FOR_LOOP
        # Drawing is now done, hide the turtle
        self.t.hideturtle()
    # END_DRAW_FUNC
    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    ### ANIMATION FUNCTIONS
    ##------------------------------------------------------------------------
    # Update by one step
    def update(self):
        # Skip the rest of the if all other steps are done.
        if self.drawingComplete:
            return
        # Increment the angle
        self.a += self.step
        # Draw a step
        R, k, l = self.R, self.k, self.l
        # Set the angle
        a = math.radians(self.a)
        x = R*((1-k)*math.cos(a) + l*k*math.cos((1-k)* a/k))
        y = R*((1-k)*math.sin(a) - l*k*math.sin((1-k)* a/k))
        self.t.setpos(self.xc+x, self.yc+y)
        # If drawing is complete, set flag
        if self.a >= 360*self.nRot:
            self.drawingComplete = True
            # Drawing is now complete, hide cursor
            self.t.hideturtle()
    # END_SPIRO.UPDATE_FUNC
    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    ### THE CLEAR METHOD
    ##------------------------------------------------------------------------
    # Clear all Spiros
    def clear(self):
        self.t.clear()
#*****************************************************************************
# END_SPIRO_CLASS

### THE SPIROANIMATOR CLASS
##----------------------------------------------------------------------------
# A Class for animating Spirographs
class SpiroAnimator:
    # Constructor
    def __init__(self, N):
        # Set timer value in milliseconds
        self.deltaT = 10
        # Get Window dimmensions
        self.width = turtle.window_width()
        self.height = turtle.window_height()
        # Create Spiro objects
        self.spiros = []
        for i in range(N):
            # Generage Random Parameters
            rParams = self.genRandomParams()
            # Set Spiro parameters
            spiro = Spiro(*rParams)
            self.spiros.append(spiro)
        # END_FOR_LOOP
        # Call Timer
        turtle.ontimer(self.update, self.deltaT)
    # END_CONSTRUCTOR
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

    ### THE GENRANDOMPARAMS METHOD
    ##------------------------------------------------------------------------
    # Generage Random Parameters
    def genRandomParams(self):
        height, width = self.height, self.width
        R = random.randint(50, min(width, height)//2)
        r = random.randint(10, 9*R//10)
        l = random.uniform(0.1, 0.9)
        xc = random.randint(-width//2, width//2)
        yc = random.randint(-height//2, height//2)
        col = (random.random(),
               random.random(),
               random.random())
        return (xc, yc, col, R, r, l)
    # END_GENRANDOMPARAMS_FUNC
    #*************************************************************************
    ### RESTARTING THE PROGRAM
    ##------------------------------------------------------------------------
    # Restart Spiro Drawing
    def restart(self):
        for spiro in self.spiros:
            # Clear
            spiro.clear()
            # Generage Random Parameters
            rparams = self.genRandomParams()
            # Set the spiro parameters
            spiro.setparams(*rparams)
            # Restart Drawing
            spiro.restart()
        # END_FOR_LOOP
    # END_SPIROANIMATOR.RESTART_FUNC
    #*************************************************************************

      ### THE UPDATE METHOD
    ##------------------------------------------------------------------------
    # Update all Spiros
    def update(self):
        nComplete = 0
        for spiro in self.spiros:
            # Update
            spiro.update()
            # Count Completed Spiros
            if spiro.drawingComplete:
                nComplete += 1
            # END_IF
        # END_FOR_LOOP
        # Restart IF all spiros are complete
        if nComplete == len(self.spiros):
            self.restart()
        # END_IF
        # Call the Timer
        turtle.ontimer(self.update(), self.deltaT)
    # END_SPIROANIMATOR.UPDATE_FUNC
    #*************************************************************************

    ### SHOWING AND HIDING THE CURSOR
    ##------------------------------------------------------------------------
    # Toggle the turtle ON/OFF
    def toggleTurtles(self):
        for spiro in self.spiros:
            if spiro.t.isvisible():
                spiro.t.hideturtle()
            else:
                spiro.t.showturtle()
    # END_TOGGLETURTLES_FUNC
  #***************************************************************************
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

### SAVING THE SPIROGRAPHS
##--------------------------------------------------------------------------
# Save Drawings as .PNG files
def saveDrawing():
    # Hide the Turtle cursor
    turtle.hideturtle()
      # Generate Unique Filename
    dateStr = (datetime.now()).strftime("%d%b%Y-%H%M%S")
    fileName = "Spiro-" + dateStr
    print('Saving drawing to %s.eps/png' % fileName)
    # Get the TKinter Canvas
    canvas = turtle.getcanvas()
    # Save Drawing as Postscript image
    canvas.postscript(file = fileName + '.eps')
    # Use the Pillow module to convert the Postscript image file to PNG
    img = Image.open(fileName + '.eps')
    img.save(fileName + '.png', 'png')
    # Show the turtle cursor
    turtle.showturtle()
# END_SAVEDRAWING

def main():
    parser = argparse.ArgumentParser(description=descStr)
    # Add expected Arguments
    parser.add_argument('--sparams', nargs=3, dest='sparams', required=False,
        help="The three arguments in sparams: R, r, l")
    # Parse Arguments
    args = parser.parse_args()

    # Set the width of the drawing screen to be 80% of the screen width
    turtle.setup(width=0.8)
    # Set the Cursor shape to turtle
    turtle.shape('turtle')
    # Set the Title
    turtle.title("Spirographs!")
    # Set the key handler to save drawings
    turtle.onkey(saveDrawing, "s")
    # Start listening
    turtle.listen()

    # Hide the Main Turtle Cursor
    turtle.hideturtle()

    # Check for any arguments sent to '--sparams' and draw the Spirographs
    if args.sparams:
        params = [float(x) for x in args.sparams]
        # Draw the Spirograph with the given parameters
        col = (0.0, 0.0, 0.0)
        spiro = Spiro(0, 0, col, *params)
        spiro.draw()
    else:
        # Create Animator object
        spiroAnim = SpiroAnimator(4)
        # Add a Key handler to toggle the turtle cursor
        turtle.onkey(spiroAnim.toggleTurtles(), "t")
        # Add a Key handler to restart the animation
        turtle.onkey(spiroAnim.restart(), "space")
    # Start the turtle mainloop
    turtle.mainloop()

### Call MAIN()
if __name__ == '__main__':
    main()