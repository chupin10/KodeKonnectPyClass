import turtle


ws = turtle.Screen()

paddle = turtle.Turtle()
paddle.speed(1)
paddle.penup()

paddle.goto(-200, 0)
paddle.left(90)

def move_up(turt):
    turt.forward(10)

def move_down(turt):
    turt.forward(-10)

for i in range(10):
    move_up(paddle)
    move_down(paddle)

input()
