#This the start of Part one drawing basic shapes

print("Hello World!")

"""This is the start of Lab 4, Drawing a scene with composite shapes using turtle"""
"""This is the start of installing, Importing, and Setting up Turtle """
import turtle


""" ******* PUT YOUR FUNCTIONS HERE ******* """


"""This is the function we are to use to draw a square:"""
def draw_square(t, length):
    """Draws a square with the given side length."""
    for _ in range(4):
        t.forward(length)
        t.left(90)



"""This is the function we are to use to draw a circle:"""
def draw_circle(t, radius):
    """Draws a circle with the given radius."""
    t.circle(radius)

"""This is the function we are to use to draw a any regular polygon:"""
def draw_polygon(t, sides, length):
    """Draws a regular polygon with a given number of sides and side length."""
    angle = 360 / sides
    for _ in range(sides):
        t.forward(length)
        t.left(angle)

def jump(t:turtle.Turtle, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

"""This is the start of Part 2. Creating a composite shape:"""

"""This is the function we are to use to draw a pumpkin."""
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
    base = radius // 5
    t.penup()
    t.goto(x+base//2, y + 2 * .94 * radius)
    t.pendown()
    t.fillcolor("green")
    t.begin_fill()
    t.left(90)  # Point upwards
    t.forward(radius // 2)
    t.left(90)
    t.forward(base)
    t.left(90)
    t.forward(radius // 2)
    t.left(90)
    t.forward(base)
    t.end_fill()


"""This is the function we are to use to draw the face, the eyes and mouth of the pumpkin:"""
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
    t.right(60)
    for _ in range(6):  # Create a simple zigzag mouth
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

def draw_mini_Jacky_Lantern():
    draw_pumpkin(t, 199, -265, 35)
    draw_eye(t, 181, -230, 13)
    draw_eye(t, 208, -230, 13)
    draw_mouth(t, 185, -245, 32)



""" ***** PUT YOUR FUNCTIONS HERE ****** """


#this is the turtle object
t = turtle.Turtle()
#set speed of turtle to 0 for instant
t.speed(0)
#Hid the turtle
t.hideturtle()
#screen to draw the turtle
screen = turtle.Screen()
#new screen created and background color set
screen.bgcolor("Black")
#width and height of screen set
screen.setup(width=600, height=600)
#Clear the screen
t.clear()
#Close the turtle window when clicked

t.color("white")


""" ***** PUT YOUR DRAW CALLS HERE ****** """
jump(t, -290, -280)
draw_square(t, 35)
jump(t, -275, -235)
draw_circle(t, 18)
jump(t, -285, -190)
draw_polygon(t, 6, 15)  # Hexagon
jump(t, -285, -150)
draw_polygon(t, 3, 22) #Triangle
draw_sky(t, 10)  # Draw 10 stars

draw_pumpkin(t, -160, -250, 100)
draw_eye(t, -200, -160, 35)  # Left eye
draw_eye(t, -130, -160, 35)# Right eye
draw_mouth(t, -190, -200, 85)  # Mouth

draw_sky(t, 10)  # Draw 10 stars

draw_pumpkin(t, 0, -250, 80)
draw_eye(t, -35, -170, 28)
draw_eye(t, 25, -170, 28)
draw_mouth(t, -30, -210, 65)

draw_sky(t, 10)  # Draw 10 stars
draw_pumpkin(t, 150, -250, 100)
draw_eye(t, 115, -160, 35)
draw_eye(t, 185, -160, 35)
draw_mouth(t, 110, -200, 85)

draw_sky(t, 40)# Draw the night sky


draw_mini_Jacky_Lantern() #This is my attempt at the extra credit.

""" ***** PUT YOUR DRAW CALLS HERE ******* """


turtle.exitonclick()