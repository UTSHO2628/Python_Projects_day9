# Happy Christmas 
from turtle import *
import random

# Set up the screen
bgcolor("black")
pencolor("white")
pensize(2)

# Function to draw a triangle (tree layer)
def draw_triangle(size, color):
    fillcolor(color)
    begin_fill()
    for _ in range(3):
        forward(size)
        left(120)
    end_fill()

# Function to draw the Christmas tree
def draw_tree():
    colors = ["green", "dark green", "forest green"]
    y_offset = 0
    for i in range(3):
        penup()
        goto(-50, -y_offset)
        pendown()
        draw_triangle(100 - i * 20, colors[i % len(colors)])
        y_offset += 50

# Function to draw a star
def draw_star(size):
    pencolor("yellow")
    fillcolor("yellow")
    begin_fill()
    for _ in range(5):
        forward(size)
        right(144)
    end_fill()

# Function to draw ornaments
def draw_ornaments():
    colors = ["red", "gold", "blue", "silver"]
    for _ in range(10):
        penup()
        x = random.randint(-50, 50)
        y = random.randint(-120, 30)
        goto(x, y)
        pendown()
        pencolor(random.choice(colors))
        dot(10)

# Draw the star on top of the tree
penup()
goto(-10, 90)
pendown()
draw_star(30)

# Draw the Christmas tree
draw_tree()

# Add ornaments
draw_ornaments()

# Write "Merry Christmas"
penup()
goto(-180, -200)
pendown()
pencolor("white")
style = ("Courier", 30, "bold")
write("Merry Christmas!", font=style, move=True)

# Add some snowflakes
def draw_snowflake(size):
    for _ in range(6):
        forward(size)
        backward(size)
        right(60)

penup()
for _ in range(20):
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    goto(x, y)
    pendown()
    draw_snowflake(random.randint(5, 15))
    penup()

hideturtle()
done()
