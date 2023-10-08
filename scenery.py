import turtle 
turta = turtle.Turtle()


"""

activity 1: Creating table, cake and candle

"""





def table (length, table_color):

    """

     Function for table 

    """

   
    turta.speed(5) # Adjusting the speed of turtle
    turta.begin_fill()
    turta.forward(length) #taking length of table from the input 
    turta.right(90)
    turta.forward(10)
    turta.right(90)
    turta.forward(length)
    turta.right(90)
    turta.forward (10)
    turta.fillcolor(table_color) #takes color of table from the input 
    turta.end_fill()
    turta.left(180)
    turta.forward(10)


    """

    creating legs for table

    """

    ## Taking position for legs of the table
    turta.left(90)
    turta.forward(length/15)
    turta.right(90)

  ## first pair of legs 
      
    turta.begin_fill()

    turta.forward(length/2)

    turta.left(90)

    turta.forward(length/20)

    turta.left(90)

    turta.forward(length/2)

    turta.left(90)

    turta.forward(length/20)

    turta.fillcolor(table_color)

    turta.end_fill()




    turta.right(180)

    turta.forward(length/12)

    turta.right(90)
    

     


    turta.begin_fill()

    turta.forward(length/2)

    turta.left(90)

    turta.forward(length/20)

    turta.left(90)

    turta.forward(length/2)

    turta.left(90)

    turta.forward(length/20)

    turta.fillcolor(table_color)

    turta.end_fill()

    turta.penup()

 ### Positioning for legs of table 

    turta.goto(0,-10)
    turta.right(180)
    turta.forward(length)
    
    ### second pair of legs 
    turta.pendown()
    turta.right(180)
    turta.forward(length/15)
    turta.left(90)


    turta.begin_fill()
    turta.forward(length/2)
    turta.right(90)
    turta.forward(length/20)
    turta.right(90)
    turta.forward(length/2)
    turta.right(90)
    turta.forward(length/20)
    turta.fillcolor(table_color)
    turta.end_fill()

    turta.right(180)
    turta.forward(length/12)
    turta.left(90)
     
    turta.begin_fill()
    turta.forward(length/2)
    turta.right(90)
    turta.forward(length/20)
    turta.right(90)
    turta.forward(length/2)
    turta.right(90)
    turta.forward(length/20)
    turta.fillcolor(table_color)
    turta.end_fill()

    turta.penup()
    turta.forward(length/12)
    turta.forward(length/15)
    turta.left(90)
    turta.forward(10)
    turta.left(90)
    turta.forward(length/2)
    turta.pendown 




    
   
    



def cake(size, base_color, second_color, third_color, topping_color, candle):


    """"

    function for cake using input for size of cake, colors of layers and color of candle.

    """
    #layer1 
    #filling first layer with input color
    turta.fillcolor(base_color) 
    turta.begin_fill()
    turta.right(180)
    turta.forward(size/2)
    turta.right(180)
    turta.forward(size)
    turta.right(90)
    turta.forward(25)
    turta.right(90)
    turta.forward(size)
    turta.right(90)
    turta.forward(25)
    turta.end_fill()

    #Layer2
    turta.penup()
    turta.right(180)
    turta.forward(25)
    turta.pendown()
    turta.fillcolor(second_color)
    turta.begin_fill()
    turta.forward(15)
    turta.left(90)
    turta.forward(size)
    turta.left(90)
    turta.forward(15)
    turta.left(90)
    turta.forward(size)
    turta.end_fill()
    #Layer3
    turta.penup()
    turta.left(90)
    turta.forward(15)
    turta.pendown()
    turta.fillcolor(third_color)
    turta.begin_fill()
    turta.forward(30)
    turta.left(90)
    turta.forward(size)
    turta.left(90)
    turta.forward(30)
    turta.left(90)
    turta.forward(size)
    turta.end_fill()
    #Layer4
    turta.penup()
    turta.left(90)
    turta.forward(30)
    turta.pendown()
    turta.fillcolor(topping_color)
    turta.begin_fill()
    turta.forward(20)
    turta.left(90)
    turta.forward(size)
    turta.left(90)
    turta.forward(20)
    turta.left(90)
    turta.forward(size)
    turta.end_fill()


    # Cherry on top of the cake 
    turta.penup()

    turta.left(90)

    turta.forward(20)

    turta.left(90)

    turta.forward(size/2-7.5) 
    #taking position for cherry

    turta.right(90)

    turta.forward(10)

    turta.fillcolor("Red")

    turta.begin_fill()

    turta.pendown()

    turta.circle(10)

    turta.penup()

    turta.right(180)

    turta.forward(10)

    turta.end_fill()

   ## frosting 
    turta.penup()

    turta.right(90)

    turta.forward(size/2+12) 

    turta.left(90)

    turta.fillcolor("Beige")

    turta.begin_fill()

    turta.pendown()

    turta.forward(5)

    turta.left(90)

    turta.forward(size+10)

    turta.left(90)

    turta.forward(5)

    turta.left(90)

    turta.forward(size+10)

    turta.end_fill()






    turta.penup()

  
   #positioning for candle
    turta.forward(20)

    turta.right(180)
    turta.forward(size/2+6)
    turta.left(90)

    turta.fillcolor(candle)

    turta.begin_fill()

    turta.pendown()

    turta.forward(40)

    turta.left(90)

    turta.forward(6)

    turta.left(90)

    turta.forward(40)

    turta.left(90)

    turta.forward(6)

    turta.end_fill()

    turta.left(90)
    turta.fillcolor("red")
    turta.begin_fill()
    turta.forward(40)
    turta.right(90)
    turta.circle(8,360)

    turta.end_fill()
    turta.penup()
    

  
# defining text for the cake 
def txt(Name_of_person): 
  
    turta.up() 
    turta.goto(50, 68) 
    turta.down() 
    turta.color('black') 
  
    # Write the specified text in  
    # specified font style and size 
    turta.write("HAPPY BIRTHDAY", Name_of_person, font=("Verdana", 10)) 
  





   
def main():
    win = turtle.Screen()
    win.bgcolor("grey")


    turta.shape("turtle")

    turta.color("white")


    table_length = int(input("Enter the length of the table (Between 150-400): "))
    table_color = (input("Enter the color of the table: "))
    size = int(input("Enter the size of the cake (150-400): "))
    base_color = (input("Enter first color:"))
    second_color = (input("enter second color:"))
    third_color = (input("enter third color:"))
    topping_color = (input("enter toppoing color:"))
    candle = (input("enter color of candle: "))
    table (table_length, table_color )
    cake(size, base_color, second_color, third_color, topping_color, candle) 
    turta.speed(1)
    Name_of_person = (input("Enter name of birthday boy/girl:"))
    txt(Name_of_person)
    turta.write(Name_of_person , font=("FANTASY", 10, "bold")) 
    turta.penup()
    turta.goto(0,0)
    input("Close the drawing canvas window in order to quit...")

   
    


  

main()


win = turtle.Screen()

win.exitonclick()