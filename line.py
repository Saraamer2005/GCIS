"""
This program allows the user to draw a line of pixels with specified colors.

The user can input a string of characters to represent colors. Each character 
corresponds to a color choice:
'0': 'black', '1': 'white', '2': 'red', '3': 'yellow', '4': 'orange', '5': 'green',
'6': 'yellowgreen', '7': 'sienna', '8': 'tan', '9': 'gray', 'A': 'darkgray'


Usage:
- Run the program. It will prompt the user to enter a string of color codes.
- Input a string using the color codes provided in the prompt.
- The turtle graphics window will display a line of pixels with the chosen colors.
- Close the turtle graphics window when done by clicking on it.
"""



import turtle

win = turtle.Screen()
win.bgcolor('light blue')
lolo = turtle.Turtle()
lolo.speed(1)
PIXEL_SIZE = 30
ROWS = 20
COLUMNS = 20

def initialisation():
    lolo.speed(0)
    lolo.up()
    lolo.pensize(1)
    lolo.pencolor('black')
    lolo.fillcolor('white')

def draw_pixel(pixel_color):
    lolo.pendown()
    lolo.begin_fill()
    lolo.fillcolor(pixel_color)
    idx = 0
    while idx < 4:
        lolo.fd(PIXEL_SIZE)
        lolo.right(90)
        idx = idx + 1
    lolo.end_fill()
    lolo.fd(PIXEL_SIZE)
    lolo.penup()

def get_color(number):
    if number == '0':
        return 'black'
    elif number == '1':
        return 'white'
    elif number == '2':
        return 'red'
    elif number == '3':
        return 'yellow'
    elif number == '4':
        return 'orange'
    elif number == '5':
        return 'green'
    elif number == '6':
        return 'yellowgreen'
    elif number == '7':
        return 'sienna'
    elif number == '8':
        return 'tan'
    elif number == '9':
        return 'gray'
    elif number == 'A':
        return 'darkgray'
    else:
        return 'black'  # Default to black if input is invalid

def draw_pixels(string_color):
    index = 0
    while index < len(string_color):
        color_value = string_color[index]
        color_pixel = get_color(color_value)
        draw_pixel(color_pixel)
        index = index + 1

def main():
    initialisation()
    string_color = input("Enter the colors for each pixel as a string (example, '0123456789A'):  '0': 'black','1': 'white','2': 'red','3': 'yellow','4': 'orange','5': 'green','6': 'yellowgreen','7': 'sienna','8': 'tan','9': 'gray','A': 'darkgray' ")
    draw_pixels(string_color)
    win.exitonclick()

def move(ROWS, COLUMNS):
    xcor = lolo.xcor()
    ycor = lolo.ycor()
    ycor = ycor - ROWS * PIXEL_SIZE
    xcor = xcor + COLUMNS * PIXEL_SIZE
    lolo.goto(xcor, ycor)
    lolo.up()

if __name__ == '__main__':
    main()