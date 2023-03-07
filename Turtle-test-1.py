from turtle import *

counter = 0
sides = 8
while counter < 10:
    forward(90)
    left(360/sides)
    counter = counter + 1
    circle(100)

done()
