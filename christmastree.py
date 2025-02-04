import turtle

def draw_triangle(color, size, x, y):
    """Draws a filled triangle of a specific color and size at a given position."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(3):
        turtle.forward(size)
        turtle.left(120)
    turtle.end_fill()

def draw_star(x, y):
    """Draws a star at the given position."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("yellow")
    turtle.begin_fill()
    for _ in range(5):
        turtle.forward(30)
        turtle.right(144)
    turtle.end_fill()

def draw_christmas_tree():
    """Draws the full Christmas tree with layers, trunk, decorations, and a star."""
    turtle.speed(3)

    # Tree layers
    layer_positions = [(-50, -50), (-60, -125), (-80, -200)]
    layer_sizes = [100, 120, 160]
    colors = ["green", "forest green", "dark green"]

    for i in range(3):
        draw_triangle(colors[i], layer_sizes[i], layer_positions[i][0], layer_positions[i][1])

    # Tree trunk
    turtle.penup()
    turtle.goto(-25, -260)
    turtle.pendown()
    turtle.fillcolor("brown")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(50)
        turtle.left(90)
        turtle.forward(60)
        turtle.left(90)
    turtle.end_fill()

    # Decorations
    decoration_positions = [(0, -70), (-30, -120), (30, -130), (-10, -160)]
    turtle.penup()
    for pos in decoration_positions:
        turtle.goto(pos)
        turtle.dot(20, "red")

    # Star on top
    draw_star(-15, 40)

def main():
    """Sets up the screen and draws the festive tree."""
    turtle.setup(800, 600)
    turtle.bgcolor("gold")
    turtle.title("Festive Christmas Tree")

    draw_christmas_tree()

    # Display "Merry Christmas"
    turtle.penup()
    turtle.goto(0, -300)
    turtle.color("red")
    turtle.write("Merry Christmas!", align="center", font=("Arial", 24, "bold"))

    # Complete
    turtle.hideturtle()
    turtle.done()

main()
