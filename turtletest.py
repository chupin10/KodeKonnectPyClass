import turtle

ws = turtle.Screen()

bob = turtle.Turtle()


def draw_star():
    for i in range(5):
        # moving turtle 100 units forward
        bob.forward(100)
        # rotating turtle 144 degree right
        bob.right(144)


def draw_square(length):
    for i in range(4):
        bob.forward(length)
        bob.right(90)


length = 50
for i in range(5):
    print(length * i)
    draw_square(length * i)
input()
