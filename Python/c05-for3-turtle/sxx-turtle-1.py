
import turtle

t = turtle.Pen()

for x in range(100): # 0 ~ 99
    t.forward(x) # 전진
    t.left(90)   # 회전(90도)

turtle.done()
