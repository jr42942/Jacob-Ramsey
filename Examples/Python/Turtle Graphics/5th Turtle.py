import turtle
import math
t = turtle.Turtle()

s = turtle.Screen()
s.colormode(255)
x = 0
y=0
angle=90
dist = 150
increment = .95
#turtle.fillcolor((r,g,b))
r=255
g=255
b=255
while y < 50:    
    t.color((r, g, b))
    t.begin_fill()
    while x < 4:
        t.forward(dist)
        t.right(angle)
        x += 1
        
        print(r)
    t.end_fill()
    r = math.floor(r*increment)
    b = math.floor(b*increment)
    g = math.floor(g*increment)
    x = 0
    y += 1
    dist = dist*increment
turtle.Screen().exitonclick()     
    




turtle.Screen().exitonclick() 