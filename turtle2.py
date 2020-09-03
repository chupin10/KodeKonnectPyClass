import turtle

bob = turtle.Turtle()

bob.speed(10)

for i in range(100):
    bob.forward(100)
    bob.right(30)
    bob.forward(20)
    bob.left(60)
    bob.forward(50)
    bob.right(30)

    bob.penup()
    bob.setposition(0, 0)
    bob.pendown()

    bob.right(2)

turtle.done()
