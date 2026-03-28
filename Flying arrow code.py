import turtle
import random
screen=turtle.Screen()
screen.setup(width=1.0, height=1.0)
screen.getcanvas().winfo_toplevel().state("zoomed")
screen.setworldcoordinates(-500, -400, 500, 400)
screen.bgcolor("black")

speed = 6

t=turtle.Turtle()
a=turtle.Turtle()
b=turtle.Turtle()
c=turtle.Turtle()
d=turtle.Turtle()
g=turtle.Turtle()
die=turtle.Turtle()
g.hideturtle()
d.hideturtle()
a.hideturtle()
b.hideturtle()
c.hideturtle()
die.hideturtle()
die.color("orange")
a.width(4)
b.width(4)
a.color("red")
b.color("red")
c.color("blue")
t.color("turquoise")
g.color("green")
d.color('blue')
die.penup()
c.penup()
d.penup()
g.penup()
die.speed()
die.goto(0, 0)
g.speed(0)
a.speed(0)
b.speed(0)
c.speed(0)
d.speed(0)
t.speed(0)
g.goto(-480, -355)
##
##
g.write("v1.3", font=("OCR A Extended", 20, "normal"))# version
##
##
count = 0
c.goto(360, 330)
d.goto(-480, 330)

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
game1 = True
count = 0

def restart():
    global game1, count, speed, dead
    
    if not dead:
        return

    game1 = False
    count = 0
    speed = 6

    die.clear()
    t.hideturtle()
    t.penup()
    t.clear()
    t.goto(-500, 0)
    t.pendown()
    t.showturtle()
    screen.update()
    
    for ob in death_circles:
        ob.hideturtle()
    death_circles.clear()
    
    t.up = False
    dead = False
    game1 = True

    screen.ontimer(loop, 16)

    


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
    c.write('score = ' + str(count), font=("OCR A Extended", 20, "normal"))

def spawn_circle():
    ob=turtle.Turtle()
    ob.shape("square")
    ob.setheading(52)
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
    global game1
    global dead, count, speed
    if game1 == False:
        return
    if dead:
            die.write("U died", align=("center"), font=("OCR A extended", 150, "normal"))
            game1 = False
    counter()
    if dead:
        return
    x, y = t.pos()
    d.clear()
    d.write('speed = ' + str(speed), font=("OCR A Extended", 20, "normal"))
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
        speed = round(speed + 0.2, 1)
        t.pendown()
        spawn_circle()
    if nextposy < -320:
        dead = True
    if nextposy > 320:
        dead = True
    if collision():
        dead = True
    if game1:
        screen.ontimer(loop, 16)
    screen.update()

screen.listen()

screen.onkeypress(up1, "space")
screen.onkeyrelease(up0, "space")
screen.onkeypress(up1, "Left")
screen.onkeyrelease(up0, "Left")
screen.onkeypress(restart, 'r')
canvas = screen.getcanvas()
canvas.bind("<ButtonPress-1>", lambda e: up1())
canvas.bind("<ButtonRelease-1>", lambda e: up0())




draw_border()
loop()
screen.mainloop()
