import turtle
import random
a = 'text'
b = 35
c = 49
##for key in range(5):
##    r = random.randint(b, c)
####    print(type(r), r)

let = int(input('Введите число'))
X = -200
turtle.penup()
turtle.goto(X, 0)

if 20 < let < 100:
    turtle.goto(0, 120)
    turtle.goto(120, 120)
    turtle.goto(120, 0)
    turtle.goto(0, 0)

elif let > 100:
    for i in range(15):
        turtle.pendown()
        X = X + 20
        turtle.goto(X, 0)
        turtle.penup()
        X = X + 20
        turtle.goto(X, 0)
    
else:
    turtle.goto(0, 120)
    turtle.goto(120, 120)
    turtle.goto(0, 0)

