# Author: Dante Bianco
# Date: October 30, 2019
# Description: The code for creating the sierpinski triangle A4


import turtle

# Scotty Dub's Skeleton code for setting up the turtle
def turtle_setup(canv_width, canv_height):
    """ Set up the canvas and a turtle for coloring pixels. Return a turtle
        object in hidden state with its pen up. The canvas has size canv_width
        by canv_height, with a coordinate system where (0,0) is in the bottom
        left corner, and automatic re-drawing of the canvas is disabled so that
        turtle.update() must be called to update the drawing.
    """
    # create a turtle to color pixels with
    t = turtle.Turtle()

    # set the screen size, coordinate system, and color mode:
    screen = t.getscreen()
    screen.setup(canv_width, canv_height)
    screen.setworldcoordinates(0, 0, canv_width, canv_height)
    turtle.colormode(255) # specify how colors are set: we'll use 0-255

    t.up() # lift the pen
    t.hideturtle() # hide the turtle triangle
    screen.tracer(0, 0) # turn off redrawing after each movement

    return t


# Scotty Dub's midpoint skeleton code
def midpoint(a, b):
    """ Return the midpoint between points a = (ax, ay) and b = (bx, by) """
    ax, ay = a
    bx, by = b
    mx = (ax + bx) / 2
    my = (ay + by) / 2
    return mx, my


# Function definition for a random point
def random_point(canv_width, canv_height):
    """Generates a random point within the canvas for the turtle to draw
        that takes the canv_width and canv_height arguments   
    """
    import random
    px = random.randint(0, canv_width)
    py = random.randint(0, canv_height)
    point = px, py
    return point


# Function definition for a random corner
def random_corner():
    """Generates the 3 corners used to create the triangles given the canv_width
        and canv_height arguments
    """
    corner_one = ((canv_width / 2), canv_height)
    corner_two = (0, 0)
    corner_three = (canv_width, 0)
    
    import random
    random_corner = random.randint(1, 3)
    if random_corner == 1:
        return corner_one
    elif random_corner == 2:
        return corner_two
    else:
        return corner_three


# A function that calculates the distance between the bottom-left corner of the canvas(origin)
# to the top-right corner of the canvas
def distance(x, y):
    """Calculates the the distance between two random non-negative points,
        as given by x and y.
        This function was purely for test purposes within sierpinski_test.py.
    """
    
    import math
    # the maximum distance from one corner of the canvas to another
    # think of it as a diagonal line that cuts the canvas
    max_dist = math.sqrt((x ** 2) + (y ** 2))
    
    return max_dist


# Function for choosing the color
def choose_color(m):
    """The function that chooses the color for a certain point.
        Makes use of the variable "m" within the for loop below, uses "p" as the x value
        for the distances from each corner to that midpoint and does the same but with "c"
        for the y value.
        Returns the value of "color" which is a tuple of three integers that give a certain
        point a color value.
    """
    x = m[0]
    y = m[1]
    
    import math
    # the maximum distance from one corner of the canvas to another
    # think of it as a diagonal line that cuts the canvas
    max_dist = math.sqrt((canv_width ** 2) + (canv_height ** 2))
    
    # Distance from each respective corner to the midpoint of the opposite side
    dist_from_c1 = int(math.sqrt((((canv_width / 2) - x) ** 2) + ((canv_height - y) ** 2)))
    dist_from_c2 = int(math.sqrt(((0 - x) ** 2) + ((0 - y) ** 2)))
    dist_from_c3 = int(math.sqrt(((canv_width - x) ** 2) + ((0 - y) ** 2)))
    
    # The color value as the dots fade away from their respective corner
    color_c1 = int(255 - ((dist_from_c1 / max_dist) * 255))
    color_c2 = int(255 - ((dist_from_c2 / max_dist) * 255))
    color_c3 = int(255 - ((dist_from_c3 / max_dist) * 255))
    
    color = (color_c1, color_c2, color_c3)
    
    return color

 

#Take the choose color function and color that pixel
def color_pixel(t, point, color):
    """ Colors the pixel each time the pen goes down while creating the triangle.
        Takes the turtle "t", the value of "point" that was returned
        from random_point, and the value of "color" as returned from choose_color.
    """
    t.colormode(255)
    t.color(color)
    t.penup()
    t.hideturtle()
    t.goto(point)
    t.pendown()
    t.dot(2, color)
    t.penup()     
    
    
# Write your main program here.
def main_function():
    """The main function that creates the chaos game and runs it
    """
    # Start by calling the turtle_setup function.
    turtle_setup(canv_width, canv_height)
    
    # Chaos game
    # Let p be a random point in the window
    p = random_point(canv_width, canv_height)
    for i in range(10000):
        # removal of the first 10 points drawn
        if i < 10:
            c = random_corner()
            m = midpoint(p, c)
            color = choose_color(m)
            p = m
        else:
            # c = a random corner of the triangle
            c = random_corner()
            # m = the midpoint between p and c
            m = midpoint(p, c)
            # choose a color for m
            color = choose_color(m)
            # color the pixel at m
            color_pixel(turtle, m, choose_color(m))
            p = m
            if i % 2000 == 0:
                turtle.update()


# part of Scotty Dub's skeleton code, runs the main function
# allows for program arguments to be inputted
if __name__ == "__main__":    
    import sys
    
    # width and height are given as command line arguments:
    canv_width = int(sys.argv[1])
    canv_height = int(sys.argv[2])
    
    # a call to the main function
    main_function()
