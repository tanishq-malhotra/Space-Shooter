import turtle
import math
import random
import time

#set up screen
wn=turtle.Screen()
wn.bgcolor("black")
wn.bgpic("bg.gif")
wn.title("Space Runner")
wn.tracer(2)
#import the images
turtle.register_shape("enemy.gif")

#draw border
b=turtle.Turtle()
b.color("white")
b.penup()
b.speed(0)
b.setposition(-300,-300)
b.pendown()
b.pensize(4)
for x in range(4):
    b.forward(600)
    b.left(90)
b.hideturtle()

#create player
player=turtle.Turtle()
player.color("Blue")
player.shape("triangle")
player.penup()
player.speed(0)

#create enemy
maxobjects=10
object=[]
for i in range(maxobjects):
    object.append(turtle.Turtle())
    object[i].color("red")
    object[i].shape("enemy.gif")
    object[i].penup()
    object[i].speed(0)
    object[i].setposition(random.randint(-280,280),random.randint(-280,280))

#set speed
speed = 0

#game stopper
count=0
stop=turtle.Turtle()
stop.color("white")
stop.penup()
stop.speed(0)
stop.setposition(-50,0)
stop.hideturtle()
flag = 0

#score
score=0
s = turtle.Turtle()
s.color("white")
s.penup()
s.speed(0)
s.setposition(-290,310)
ss= "Score: {}".format(score)
s.write(ss,False,align="left",font=("Arial",12,"normal"))
s.hideturtle()

#define functions
def turn_left():
    player.left(30)

def turn_right():
    player.right(30)

def speed_up():
    global speed
    if speed < 2.4:
        speed+=0.8

def speed_down():
    global speed
    if speed > 2.4:
        speed-=0.8

def collosion_check(player,ob):
    d = math.sqrt( math.pow(player.xcor() - ob.xcor(),2) + math.pow(player.ycor() - ob.ycor(),2))
    if d < 20:
        return True
    else:
        return False

#set keyboard inputs
turtle.listen()
turtle.onkey(turn_left,"Left")
turtle.onkey(turn_right,"Right")
turtle.onkey(speed_up,"Up")
turtle.onkey(speed_down,"Down")

#main loop
while True:
    player.forward(speed)
    #Boundary check
    x =player.xcor()
    y=player.ycor()
    if x > 290 or x < -290:
        player.left(180)
    elif y > 290 or y < -290:
        player.right(180)
    #move objects
    for i in range(maxobjects):
        object[i].forward(2)
        if object[i].xcor() > 290 or object[i].xcor() < -290:
            object[i].left(180)
        elif object[i].ycor() > 290 or object[i].ycor() < -290:
            object[i].right(180)
        # collosion check
        if collosion_check(player,object[i]):
            object[i].setposition(1000,1000)
            score+=1
            count+=1
            ss= "Score: {}".format(score)
            s.clear()
            s.write(ss,False,align="left",font=("Arial",12,"normal"))

        #used to stop the game after all 10 enemies are killed
        if count == 10:
            stop.showturtle()
            stopstring="GAME OVER"
            stop.write(stopstring, False , align="center" , font=("Arial",50,"bold"))
            time.sleep(2)
            flag = 1
            break
    if flag:
        break
