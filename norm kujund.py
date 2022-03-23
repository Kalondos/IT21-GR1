import turtle
from turtle import *


t = turtle.Turtle()
#teeb nelinurga valma
for i in range(2):
    t.forward(150)
    t.left(90)
    t.forward(50)
    t.left(90)

#ei taju aga ilma selleta ei t66ta
t.forward(150)
t.left(-45)
t.forward(50)
t.left(270)
t.forward(150)
t.left(-90)
t.forward(50)
t.left(-90)
t.forward(150)
t.left(-90)
t.forward(50)

#l2ristab ekraanile 6 korda kujundit, ainult 2gedamalt
for i in range(6):
    t.left(45)
    t.forward(50)
    t.left(-90)
    t.forward(150)
    t.left(-90)
    t.forward(50)
    t.left(-90)
    t.forward(150)
    t.left(-90)
    t.forward(50)


turtle.exitonclick()