import turtle

# Setup screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Sri Chakra Drawing")

# Setup turtle pen
pen = turtle.Turtle()
pen.speed(0)   # max speed

# Function to draw one triangle
def draw_triangle(size, angle):
    pen.setheading(angle)
    for _ in range(3):
        pen.forward(size)
        pen.left(120)

# Draw 9 main triangles (4 upward + 5 dow
