"""
This program generates a grid of colored pixels using the turtle graphics library.

It defines functions to draw individual pixels, rows, and the overall grid. The grid 
has a specified size, with the number of rows and columns controlled by ROWS and 
COLUMNS constants. The pixel size is determined by the PIXEL_SIZE constant.

Functions:
- reposition(x, y): Moves the turtle to the specified coordinates (x, y).
- pixel(color1): Draws a colored pixel with the specified fill color.
- row(color2, color3): Draws a row of alternating colored pixels.
- grid(color4, color5): Draws a grid of alternating rows of pixels.
- main(): Sets up the initial position and calls the grid function.

Usage:
- Ensure that the turtle graphics window is open before running the program.
- If executed as a standalone script (using __name__ == "__main__"), the main 
  function will be called, which generates the grid. The turtle graphics window can 
  be closed by clicking on it.

"""


import turtle

turtle.tracer(False)

lolo = turtle.Turtle()

PIXEL_SIZE = 30
ROWS = 20
COLUMNS = 20
lolo.fillcolor("white")
lolo.color("black")

assert (ROWS == COLUMNS)

def reposition(x,y):
    lolo.up()
    lolo.setpos(x,y)
    lolo.down()
    return x,y

def pixel(color1):
    lolo.fillcolor(color1)
    lolo.begin_fill()
    for i in range(4):
        lolo.forward(PIXEL_SIZE)
        lolo.right(90)
    lolo.end_fill()

def row(color2,color3):
    for z in range(int(ROWS/2)):
        pixel(color2)
        lolo.forward(30)
        pixel(color3)
        lolo.forward(30)

def grid(color4,color5):
    for w in range(int(COLUMNS/2)):
        row(color4,color5)
        lolo.right(90)
        lolo.forward(PIXEL_SIZE*2)
        lolo.right(90)
        row(color4,color5)
        lolo.left(180)

def main():
    reposition(-300,300)
    grid("red","black")
    

if __name__ =="__main__":
   main()
turtle.exitonclick()