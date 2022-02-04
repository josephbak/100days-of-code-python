import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

# color_list = [(131, 166, 205), (222, 148, 106), (31, 42, 61), (199, 134, 147), (165, 59, 48), (140, 184, 162)]

color_list = [(131, 166, 205), (31, 42, 61), (199, 134, 147), (165, 59, 48), (140, 184, 162)]

def random_color():
    rc = random.choice(color_list)
    return rc

tim.speed("fastest")

def draw_one_dotted_line():
    for i in range(10):
        #tim.pendown()
        # tim.fillcolor(random_color())
        # tim.begin_fill()
        # tim.circle(10)
        # tim.end_fill()
        tim.dot(20, random_color())
        #tim.penup()
        tim.forward(50)


def move_to_beginnig():
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)

tim.ht()
tim.penup()
tim.setheading(225)
tim.forward(250)
tim.setheading(0)

for _ in range(10):
    draw_one_dotted_line()
    move_to_beginnig()



screen = t.Screen()
screen.exitonclick()