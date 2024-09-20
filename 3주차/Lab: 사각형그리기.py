import turtle

t = turtle.Turtle()
t.shape("turtle")

def square(length):
    t.down()
    for i in range(4):
        t.fd(length)
        t.lt(90)
    t.up()
    
square(100)
t.fd(120)
square(100)
t.fd(120)
square(100)

turtle.mainloop()
turtle.bye()