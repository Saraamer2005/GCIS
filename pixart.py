""" 
This program uses the turtle graphics library to draw various patterns, including 
representations of famous characters like Yoda, a star, Luigi, and Mario.

The program provides a user interaction to choose which drawing to display.

Functions:
- draw_pixle(x, y, fill_color): Draws a square (pixel) at the specified coordinates 
  with the specified fill color.
- draw_yoda(): Draws a representation of Yoda using a predefined pattern.
- draw_star(): Draws a representation of a star using a predefined pattern.
- draw_luigi(): Draws a representation of Luigi using a predefined pattern.
- draw_mario(): Draws a representation of Mario using a predefined pattern.

Usage:
- Run the program. It will prompt the user to choose which drawing to display by 
  entering one of the following options: 'star', 'yoda', 'mario', 'luigi'.
- The selected drawing will be displayed using turtle graphics in a window.
- Close the turtle graphics window when done by clicking on it.

Note:
- The drawings are generated using predefined patterns stored as strings.
- Each character in the pattern string corresponds to a color code.
- The patterns are interpreted to draw the corresponding colors on the screen.

Examples:
- To draw Yoda, enter 'yoda' when prompted.
- To draw a star, enter 'star' when prompted.

"""


import turtle as t

# Set up the Turtle window
window = t.Screen()
t.tracer(False)
lolo = t.Turtle()  # turtle name is lolo



# Function to draw a square for a given pattern
def draw_pixle(x, y, fill_color):
    """
    this function draw a squares (pixles)
    it take the following parameters:
    x = point on x axis 
    y = point on y axis
    fill_color = the color of the pixle 

    """
    lolo.penup()
    lolo.fillcolor(fill_color)
    lolo.goto(x, y)
    lolo.pendown()
    lolo.begin_fill()
    for _ in range(4):
        lolo.forward(20)
        lolo.right(90)
    lolo.end_fill()

# Drawings functions

# Drawing 1 (Yoda)
def draw_yoda():
    """
    this function draw yoda using a specific string for each color 
    it use loops and if statments to generate the drawing 

    """
    lolo.clear()
    #lolo.speed(10)
    yoda_pattern = [
    "0000000000000000000000000",
    "0111111111111111111111110",
    "0111111111100011111111110",
    "0111111110066600111111110",
    "0111111106656566011111110",
    "0111111096666666901110110",
    "0111000965656565690006010",
    "0110666666666666666665010",
    "0106556555666555666650110",
    "0110005101606101665501110",
    "0111110666666666660011110",
    "0111111066000666601111110",
    "0111111106666666011111110",
    "0111111110066660111111110",
    "0111111100A8778A011111110",
    "011111106AA8778AA01111110",
    "0111110770A8008A601111110",
    "0111111070A8778A011111110",
    "0111111070660066011111110",
    "0111111101001100111111110",
    "0111111111111111111111110",
    "0000000000000000000000000"
    ]
    pattern_width = len(yoda_pattern[0])
    pattern_height = len(yoda_pattern)

    for i, row in enumerate(yoda_pattern):
        for j, color_code in enumerate(row):
            x = (j - pattern_width / 2) * 20
            y = (-i + pattern_height / 2) * 20
            fill_color = "black"  
            if color_code == "1":
                fill_color = "white"
            elif color_code == "2":
                fill_color = "tan"
            elif color_code == "3":
                fill_color = "green"
            elif color_code == "6":
                fill_color = "yellowgreen"
            elif color_code == "7":
                fill_color = "sienna"
            elif color_code == "8":
                fill_color = "tan"
            elif color_code == "9":
                fill_color = "grey"
            elif color_code == "A":
                fill_color = "silver"

            
            draw_pixle(x, y, fill_color)

# Drawing 2 (Star)
def draw_star():

    """
    this function draw a star using a specific string for each color 
    it use loops and if statments to generate the drawing 
     
    """

    lolo.clear()
    #lolo.speed(10)
    star_pattern = [
    "00000000000000000000",
    "01111111111111111110",
    "01111111111111111110",
    "01111111100111111110",
    "01111111033011111110",
    "01111110333301111110",
    "01000000333300000010",
    "01033333333333333010",
    "01104333033033340110",
    "01110433033033401110",
    "01111043033034011110",
    "01111043333334011110",
    "01110433333333401110",
    "01110433333333401110",
    "01104334400443340110",
    "01104440011004440110",
    "01044001111110044010",
    "01000111111111100010",
    "01111111111111111110",
    "00000000000000000000"
    ]
    pattern_width = len(star_pattern[0])
    pattern_height = len(star_pattern)

    for i, row in enumerate(star_pattern):
        for j, color_code in enumerate(row):
            x = (j - pattern_width / 2) * 20
            y = (-i + pattern_height / 2) * 20
            fill_color = "black"  
            if color_code == "1":
                fill_color = "white"
            elif color_code == "2":
                fill_color = "tan"
            elif color_code == "3":
                fill_color = "yellow"
            elif color_code == "4":
                fill_color = "orange"

            
            draw_pixle(x, y, fill_color)



# Drawing 3 (Luigi)
def draw_luigi():

    """
    this function draw luigi using a specific string for each color 
    it use loops and if statments to generate the drawing 

    """

    lolo.clear()
    #lolo.speed(10)
    luigi_pattern = [
    "00000000000000000000",
    "09999999999999999990",
    "09999995555559999990",
    "09999555555555999990",
    "09999998080000999990",
    "09999888088808099990",
    "09998880888008099990",
    "09999000088880099990",
    "09999988888889999990",
    "09999999111511999990",
    "09999111511511199990",
    "09991111555511119990",
    "09998815155151889990",
    "09998885555558889990",
    "09998855555555889990",
    "09999955599555999990",
    "09999000999900099990",
    "09990000999900009990",
    "09999999999999999990",
    "00000000000000000000"
    ]
    pattern_width = len(luigi_pattern[0])
    pattern_height = len(luigi_pattern)

    for i, row in enumerate(luigi_pattern):
        for j, color_code in enumerate(row):
            x = (j - pattern_width / 2) * 20
            y = (-i + pattern_height / 2) * 20
            fill_color = "black"  
            if color_code == "1":
                fill_color = "white"
            elif color_code == "2":
                fill_color = "tan"
            elif color_code == "3":
                fill_color = "green"
            elif color_code == "5":
                fill_color = "green"
            elif color_code == "8":
                fill_color = "tan"
            elif color_code == "9":
                fill_color = "grey"

            
            draw_pixle(x, y, fill_color)


# Drawing 4 (Mario)
def draw_mario():

    """
    this function draw mario using a specific string for each color 
    it use loops and if statments to generate the drawing
    
    """
    lolo.clear()
    #lolo.speed(10)
    mario_pattern = [
    "00000000000000000000",
    "01111111111111111110",
    "01111112222221111110",
    "01111122222222211110",
    "01111177778781111110",
    "01111787888788811110",
    "01111787788878881110",
    "01111778888777711110",
    "01111118888888111110",
    "01111177277711111110",
    "01111777277277711110",
    "01117777222277771110",
    "01118872822827881110",
    "01118882222228881110",
    "01118822222222881110",
    "01111122211222111110",
    "01111777111177711110",
    "01117777111177771110",
    "01111111111111111110",
    "00000000000000000000"
    ]
    pattern_width = len(mario_pattern[0])
    pattern_height = len(mario_pattern)

    for i, row in enumerate(mario_pattern):
        for j, color_code in enumerate(row):
            x = (j - pattern_width / 2) * 20
            y = (-i + pattern_height / 2) * 20
            fill_color = "black"  
            if color_code == "1":
                fill_color = "white"
            elif color_code == "2":
                fill_color = "red"
            elif color_code == "7":
                fill_color = "sienna"
            elif color_code == "8":
                fill_color = "tan"

            
            draw_pixle(x, y, fill_color)

# interact with the user
while True:
    user_input = input("choose the drawing you want to see (star/yoda/mario/luigi)? ").lower()
    
    if user_input == "star":
        draw_star()
    elif user_input == "yoda":
        draw_yoda()
    elif user_input == "mario":
        draw_mario()
    elif user_input == "luigi":
        draw_luigi()

    else:
        print("Invalid. Please enter one of the following drawings 'star', 'yoda', 'mario', 'luigi'")

# Close the turtle graphics window when done
window.exitonclick()