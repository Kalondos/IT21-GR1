##########
# KArlos fernando jr kotter
# 15.03.2022
# UL 2
#########
import turtle
#Aken
aken = turtle.Screen()
aken.setup(300,300)
aken.bgcolor("lightblue")

#kujund
t = turtle.Turtle()
for x in range(5):
    t.forward(100)
    t.left(-144)



#kolmnurk
varv = input("Sisestage kolmnurga värv: ")
kulg = input("Sisestage võrdkülgse kolmnurga külje pikkus:")

def kolmnurk():
t = turtle.Turtle()
    for t in range(3):
        t.forward(kulg)
        t.left(120)
kolmnurk()
    




turtle.exitonclick()