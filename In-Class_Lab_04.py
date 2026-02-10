print("hello world. . . ")

#"it is just a friendly thing to do, for loops, and the i
# isnt being used, change it to an underscore."


#"This is a core concept of science and programing,
# taking big problems and making them smaller."  "

#triple quites are best used for multiline comments


#def polyline(n, length, angle):


#sometimes there are very long doc strings, "If you are stuck
# in a multi hour long flight you are going to want to see all that
# information"

#Try not to forget the previous weeks lectures/material/knowledge
#all these build on each other and along eachother.
#LEcture ended ish @ 2:54 pm


#THIS IS THE START OF LAB 4
#DRAWING A SCENE WITH COMPOSITE SHAPES USING TURTLE

#"can computers do actual random? No, because the computer
# deos what you tell them"
#"explanation on cloud flares execution of random-ness, a
# leet haxor might be able to figure it out, but no one has yet."

#look through this code and see what you can understand
#make sure oyuthon interpreter is 3.13 with tk, because turtle
# uses it.

#for the dimensions of windth and height, what units does it use?
# Python uses pixels
# , other libraries use different units

#within pycharm, highlighting and right clicking brings in
# useful options, rind usages bring you to where they are being used,
# and go to Declaration or usages, brings you to where a
# the highlighted function is being defines, go to
# implementation also bring you

#what is scope?

#[] square brackets can contain lists of items.

#"I just want you to see some material early."
#if you are interested in rpogrmaming, learning about aoject oriented
# and functional oriented pradymn can be helpful
#lambda is an anonymous function, that returns a function pointer.

#we are going to do an entrire week of lambda's around week 8.

#function nesting calls, this happens alot, how to check to see
# what does
#it do? (in the IDE) (right click go to implementation)


#if you asked to desipher soemone elses code start top down, if you
# are trying to figure out how to make something start bottumup,
# then generalize and refactor



import turtle
import math
import random


my_turtle = turtle.Turtle()

def draw_polyline(n, length, angle):  # This is really generalized and flexible now.
    """Draws line segments with the given length and angle between them.

    n: integer number of line segments
    length: length of the line segments
    angle: angle between segments (in degrees)
    """
    for i in range(n):
        my_turtle.forward(length)
        my_turtle.left(angle)


def draw_polygon(n, length):
    angle = 360.0 / n
    # Now this is more generalized as it uses polyline, but still fixes the length and angle for regular polygons.
    draw_polyline(n, length, angle)

def draw_arc(radius, angle):  # Similar to circle, but can do fractional circles.
    arc_length = 2 * math.pi * radius * angle / 360  # Here we calculate how much of the arc of a circle to draw.
    n = 30  # We fix the segments to 30 still, but this is 30 segments per arc, so smaller arcs will appear smoother.
    length = arc_length / n
    step_angle = angle / n  # Since we are covering a fraction of the arc of a circle, we need smaller angles too.
    draw_polyline(n, length, step_angle)  # And now we approximate the arc with polyline.


def draw_square(length):
    draw_polygon(12, length)


#indentation function name headers scope(local variable)



#function name is draw underscore square
#, it uses one parameter named length, it calls one function
# named draw underscore polygon, it has been given two variables
# an n of 12 and length


#looking for explanation, an internal conversation of what you are
# looking at, how does code work



#Part Two: Creating Composite Shapes
#Pumkin

#debugging is normal and often, in lass denugging
# completed by trevor.

#in general you want to not use global parameters.






def draw_pumpkin(t, x, y, radius):
    """Draws a pumpkin (orange circle) at the given (x, y) location with a green stem."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("orange")
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

    # Drawing the stem
    t.penup()
    t.goto(0, 0 + 2 * .94 * radius)
    t.pendown()
    t.fillcolor("green")
    t.begin_fill()
    t.left(90)  # Point upwards
    t.forward(radius // 2)
    t.left(90)
    t.forward(radius // 5)
    t.left(90)
    t.forward(radius // 2)
    t.left(90)
    t.forward(radius // 5)
    t.end_fill()

#how would i draw a pumkin right noe?
#missing t object, find it
# #

import turtle


# Create a turtle object
t = turtle.Turtle()

# Hide the turtle and set speed
t.speed(10)  # 1 is slow, 10 is fast, 0 is instant
t.hideturtle()

# Create a window to draw in
# Create a new turtle screen and set its background color
screen = turtle.Screen()
screen.bgcolor("darkblue")
# Set the width and height of the screen
screen.setup(width=600, height=600)
# Clear the screen
t.clear()

"""PUT YOUR DRAW CALLS TO FUNCTIONS HERE"""

# Close the turtle graphics window when clicked

# Example of drawing a jack-o-lantern with eyes and a mouth

turtle.exitonclick()

#(first run incorrect, (intentional) why did the
# stem not draw correctly?
#

#drawing the stem torubleshooting
#t.penup()
#t.goto(0, 0+ 2*.99*radius)
#t.pendown()

#incomplete

from shape_factory import draw_polygon

def draw_eye(t, x, y, size):
    """Draws one triangular eye at the given (x, y) position."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()
    draw_polygon(t, 3, size)
    t.end_fill()

def draw_mouth(t, x, y, width):
    """Draws a jagged mouth using a series of connected lines."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()

    for _ in range(5):  # Create a simple zigzag mouth
        t.forward(width // 5)
        t.left(120)
        t.forward(width // 5)
        t.right(120)
    t.end_fill()
    t.left(60)


def draw_star(t, x, y, size):
    """Draws a star at the given (x, y) position."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("white")
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144)  # 144 degrees is the angle to form a star
    t.end_fill()


import random

def draw_sky(t, num_stars):
    """Draws a starry sky with the given number of stars."""
    for _ in range(num_stars):
        x = random.randint(-300, 300)
        y = random.randint(0, 300)
        size = random.randint(10, 30)
        draw_star(t, x, y, size)

#draw_pumpkin(0, 0,  0, -100, 100)  # Draw the pumpkin
#draw_eye(t, -40, 0, 30)  # Left eye
#draw_eye(t, 40, 0, 30)   # Right eye
#draw_mouth(t, -50, -50, 100)  # Mouth

draw_sky(t, 20)  # Draw 20 stars

#this is oging to take buckets of focused practice to get it
# to stick




# Draw three jack-o-lanterns
draw_pumpkin(t, -150, -250, 100)
draw_eye(t, -190, -160, 30)  # Left eye
draw_eye(t, -110, -60, 30)  # Right eye
draw_mouth(t, -190, -200, 80)  # Mouth

draw_pumpkin(t, 0, -250, 80)
draw_eye(t, -20, -170, 25)
draw_eye(t, 20, -710, 25)
draw_mouth(t, -30, -210, 60)

draw_pumpkin(t, 150, -250, 100)
draw_eye(t, 110, -160, 30)
draw_eye(t, 190, -160, 30)
draw_mouth(t, 110, -200, 80)

# Draw the night sky
draw_sky(t, 50)

#extra credit make a jack o lantern encapsulated function


#extra credit challenge  make a jack o lantern encapsulated function


#hint, radius/ratio





















