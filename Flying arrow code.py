import turtle
import random
screen=turtle.Screen()
screen.setup(width=1.0, height=1.0)
screen.getcanvas().winfo_toplevel().state("zoomed")
screen.setworldcoordinates(-500, -400, 500, 400)
screen.bgcolor("black")
game_running = False

speed = 6

t=turtle.Turtle()
a=turtle.Turtle()
b=turtle.Turtle()
c=turtle.Turtle()
a.hideturtle()
b.hideturtle()
c.hideturtle()
a.width(4)
b.width(4)
a.color("red")
b.color("red")
c.color("blue")
t.color("turquoise")
c.penup()

count = 0
c.goto(460, 330)

death_circles = []

t.width(2)
t.turtlesize(2)

t.hideturtle()
screen.tracer(0)
t.penup()
t.goto(-500, 0)
t.pendown()
t.showturtle()
screen.update()
t.up = False
dead = False
count = 0

def draw_border():
    a.penup()
    b.penup()
    a.goto(-500, -320)
    b.goto(-500, 320)
    a.pendown()
    b.pendown()
    a.goto(500, -320)
    b.goto(500, 320)

def counter():
    c.clear()
    c.write(str(count), font=("OCR A Extended", 20, "normal"))

def spawn_circle():
    ob=turtle.Turtle()
    ob.shape("square")
    ob.setheading(51.5)
    ob.color("red")
    ob.turtlesize(4)
    ob.penup()
    ob.goto(random.randint(-400, 500), random.randint(-320, 310))
    death_circles.append(ob)

def up1():
    t.up = True
def up0():
    t.up = False
def collision():
    for ob in death_circles:
        if t.distance(ob) < 38:
            return True
    return False

def loop():
    counter()
    global dead, count, speed
    if dead:
        return
    x, y = t.pos()
    if t.up:
        t.setheading(50)
    else:
        t.setheading(310)
    t.forward(speed)
    nextposy = t.ycor()
    if x > 490:
        t.clear()
        global count
        count += 1
        t.penup()
        t.goto(-500, y)
        if count % 5 == 0:
            speed += 2
        t.pendown()
        spawn_circle()
    if nextposy < -320:
        dead = True
        t.write("U died",font=("OCR A extended", 20, "normal"))
    if nextposy > 320:
        dead = True
        t.write("U died",font=("OCR A extended", 20, "normal"))
    if collision():
        t.write("U died",font=("OCR A extended", 20, "normal"))
        dead = True
        return
        

    screen.ontimer(loop, 16)
    screen.update()

screen.listen()

screen.onkeypress(up1, "space")
screen.onkeyrelease(up0, "space")
screen.onkeypress(up1, "Left")
screen.onkeyrelease(up0, "Left")
canvas = screen.getcanvas()
canvas.bind("<ButtonPress-1>", lambda e: up1())
canvas.bind("<ButtonRelease-1>", lambda e: up0())




draw_border()
loop()
screen.mainloop()
