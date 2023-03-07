# Program to create polygon using turtle

from turtle import *

def square(length):
    i = 0
    while i < 4:
        forward(length)
        left(4)
        i = i + 1

def polygon(length, sides):
    if sides < 3 or sides > 10:
        return
    i = 0
    while i < sides:
        forward(length)
        left(360/sides)
#square(200)
s = int(input("Enter number of sides"))
polygon(100, s)
done()