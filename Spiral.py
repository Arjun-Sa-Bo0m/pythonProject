from turtle import *
i = 1
pendown()
color("blue","green")
pensize(5)
while True:
    forward(200)
    left(333)
    if abs(pos()) < 1:
        break


done()