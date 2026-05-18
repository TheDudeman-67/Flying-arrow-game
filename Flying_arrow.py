import turtle
import random
import sounddevice as sd
import soundfile as sf
import threading
import os
import time
os.chdir(os.path.dirname(__file__))
screen=turtle.Screen()
screen.setup(width=1.0, height=1.0)
screen.getcanvas().winfo_toplevel().state("zoomed")
screen.setworldcoordinates(-500, -400, 500, 400)
screen.bgcolor("black")
screen.title("Flying arrow")

import tkinter as tk
canvas = screen.getcanvas()
root = canvas.winfo_toplevel()
root.overrideredirect(True)   # removes window frame

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
die.speed(0)
die.goto(0, 0)
g.speed(0)
a.speed(0)
b.speed(0)
c.speed(0)
d.speed(0)
t.speed(0)
g.goto(-480, -355)
high=turtle.Turtle()
high.hideturtle()
high.penup()
high.speed(0)
high.goto(0,-120)
high.color('light green')
high1=turtle.Turtle()
high1.hideturtle()
high1.penup()
high1.speed(0)
high1.goto(0,-250)
high1.color('light blue')
highdisp=turtle.Turtle()
highdisp.hideturtle()
highdisp.penup()
highdisp.speed(0)
highdisp.goto(0, 330)
highdisp.color('blue')
##
##
g.write("v1.6", font=("OCR A Extended", 20, "normal"))# version
##
##
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
highscore = 0
highdisp.write('highscore = ' + str(highscore), align='center', font=('OCR A extended', 20, 'normal'))

def highscore_new():
    global count, highscore
    if count > highscore:
        highscore = count
        high.write('New Highscore!', align="center", font=("OCR A extended", 80, "normal"))
        high1.write(str(highscore), align='center', font=('OCR A extended', 60, 'normal'))
        highdisp.clear()
        highdisp.write('highscore = ' + str(highscore), align='center', font=('OCR A extended', 20, 'normal'))
        
import time

music_stop = False
data, samplerate = sf.read("Song.wav")
def loop_music():
    global music_stop
    while True:
        if not music_stop:
            sd.play(data, samplerate)
            sd.wait()
        else:
            sd.stop()
            time.sleep(0.05)

threading.Thread(target=loop_music, daemon=True).start()

def restart():
    global game1, count, speed, dead, music_stop, death_anim, rotating
    if not dead:
        return

    game1 = False
    death_anim = False
    rotating = False
    count = 0
    speed = 6

    screen.bgcolor("black")

    die.clear()
    high.clear()
    high1.clear()
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
    music_stop = False

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

death_anim = False

def rotate():
    global rotating
    t.left(10)

    if t.ycor() <= -320:
        rotating = False
        return

    if rotating:
        screen.ontimer(rotate, 20)

def down():
    if not death_anim:
        return 
    global rotating
    x = t.xcor()
    y = t.ycor()
    if y > -320:
        t.goto(x, y - 5)
    screen.ontimer(down, 28)

def death_animation():
    global death_anim
    global rotating
    rotating = True
    t.speed(0)
    t.penup()
    if death_anim:
        if not death_anim:
            return

    if death_anim:
        rotate()
        down()

def close_window():
    global game1
    game1 = False
    screen.bye()

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
    ob.goto(random.randint(-400, 500), random.randint(-260, 260))
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
    global game1, music_stop
    global dead, count, speed
    if game1 == False:
        return
    if dead:
            global death_anim
            death_anim = True
            death_animation()
            screen.bgcolor("dark red")
            die.write("U died", align=("center"), font=("OCR A extended", 150, "normal"))
            highscore_new()
            game1 = False
            music_stop = True
            sd.stop()
            for ob in death_circles:
                ob.hideturtle()
            death_circles.clear()
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
    

screen.listen()

screen.onkeypress(up1, "space")
screen.onkeyrelease(up0, "space")
screen.onkeypress(up1, "Left")
screen.onkeyrelease(up0, "Left")
screen.onkeypress(restart, 'r')
screen.onkeypress(close_window, 'Escape')
canvas.bind("<ButtonPress-1>", lambda e: up1())
canvas.bind("<ButtonRelease-1>", lambda e: up0())

def update():
    screen.update()
    screen.ontimer(update, 16)

draw_border()
update()
loop()
screen.mainloop()