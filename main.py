import turtle
import math
import time

# Screen setup
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("sky blue")
screen.title("Basic Palm Tree Animation")

# Define colors
TREE_BROWN = "#8B4513"
LEAF_GREEN = "forest green"

# Create turtle objects for the trunk and leaves
trunk = turtle.Turtle()
leaves = turtle.Turtle()

# Trunk settings
trunk.color(TREE_BROWN)
trunk.width(20)
trunk.hideturtle()
trunk.speed(0)

# Leaves settings
leaves.color(LEAF_GREEN)
leaves.width(3)
leaves.hideturtle()
leaves.speed(0)

# Function to draw the trunk
def draw_trunk():
    trunk.penup()
    trunk.goto(0, -200)
    trunk.pendown()
    trunk.setheading(90)
    trunk.forward(150)

# Function to draw a single leaf
def draw_leaf(angle):
    leaves.penup()
    leaves.goto(0, -50)
    leaves.setheading(angle)
    leaves.pendown()
    leaves.forward(100)

# Draw static parts of the tree (the trunk and initial leaves)
draw_trunk()

# Function to animate the leaves swaying
def animate_leaves():
    sway_angle = 20  # Maximum sway angle
    direction = 1    # 1 for right, -1 for left

    while True:
        leaves.clear()  # Clear previous leaf positions

        # Draw leaves with a small sway effect
        for angle in range(-30, 40, 20):  # Leaf angles
            draw_leaf(angle + direction * sway_angle)

        # Change direction after each cycle
        direction *= -1

        # Small delay for smoother animation
        time.sleep(0.5)

# Run the animation
animate_leaves()

# Keep the window open
turtle.done()
