#TurtleGraphics.py
#Name:
#Date:
#Assignment:

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)
def drawPolygon(bob, sides):
    for s in range(sides):
        bob.forward(50)
        bob.right(360/sides)
def fillCorner(greg, corner):
    #draw big square
    drawSquare(greg, 100)
    
    if corner == 1:
        greg.begin_fill()
        drawSquare(greg, 50)
        greg.end_fill()
    elif corner == 2:
        greg.forward(50)
        greg.begin_fill()
        drawSquare(greg, 50)
        greg.end_fill()
    elif corner == 3:
        greg.forward(50)
        greg.right(90)
        greg.penup()
        greg.forward(50)
        greg.pendown()
        greg.begin_fill()
        drawSquare(greg, 50)
        greg.end_fill()
    elif corner == 4:
        greg.forward(100)
        greg.right(90)
        greg.forward(50)
        greg.begin_fill()
        drawSquare(greg, 50)
        greg.end_fill()
def squaresInSquares(bob, num):
    count = 0
    size = 0
    while count <= num:
        size += 20
        bob.penup()
        bob.goto(-size / 2, size / 2)
        bob.pendown()
        drawSquare(bob, size)
        count += 1
def main():
    myTurtle = turtle.Turtle()
    
    #drawSquare(myTurtle, 100)
    #drawPolygon(myTurtle, 5) #draws a pentagon
    #drawPolygon(myTurtle, 8) #draws an octogon
    #drawPolygon(myTurtle, 3)
    
    #fillCorner(myTurtle, 2) #draws a square with top right corner filled in.
    #fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.

    #squaresInSquares(myTurtle, 8) #draws 5 concentric squares
    #squaresInSquares(myTurtle, 3) #draws 3 concentric squares


main()
