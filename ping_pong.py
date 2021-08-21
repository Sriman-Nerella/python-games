import turtle
import winsound
import time

man=turtle.Screen()
man.title("Sriman's Ping Pong game")
man.bgcolor("white")
man.setup(width=800,height=600)
man.tracer(0)

#left side paddle
lp=turtle.Turtle()
lp.speed(0)
lp.shape("square")
lp.color("Black")
lp.shapesize(stretch_len=1,stretch_wid=5)
lp.penup()
lp.goto(-350, 0)

#right side paddle

rp=turtle.Turtle()
rp.speed(0)
rp.shape("square")
rp.color("Black")
rp.shapesize(stretch_len=1,stretch_wid=5)
rp.penup()
rp.goto(350,0)

#Ball

ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("Black")
ball.penup()
ball.goto(0,0)
ball.dx =1
ball.dy =1

#Score
A_score=0
B_score=0

#Pen
pen=turtle.Turtle()
pen.speed(0)
pen.color("red")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player 1 :0 Player 2 :0",align="center",font=("courier",22,"normal"))

# paddles moving functions

def Lpup() :
    y=lp.ycor()
    y+=20
    lp.sety(y)
    if y>260:
        lp.sety(260)
    
def Lpdown() :
    y=lp.ycor()
    y-=20
    lp.sety(y)
    if y<-260:
        lp.sety(-260)
    
def Rpup() :
    y=rp.ycor()
    y+=20
    rp.sety(y)
    if y>260:
        rp.sety(260)
    
def Rpdown() :
    y=rp.ycor()
    y-=20
    rp.sety(y)
    if y<-260:
        rp.sety(-260)

#keyboard listening

man.listen()
man.onkeypress(Lpup,"w") 
man.onkeypress(Lpdown,"s")
man.onkeypress(Rpup,"Up")
man.onkeypress(Rpdown,"Down")   

while True :
    man.update()
    time.sleep(.000000001)
    #Ball movements
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    if ball.ycor() >290 :
        ball.sety(290)
        ball.dy *=-1 
        winsound.PlaySound("bounc.wav", winsound.SND_ASYNC)
    if ball.ycor() <-290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounc.wav", winsound.SND_ASYNC)
    if ball.xcor() >390 :
        ball.goto(0,0)
        ball.dx *= -1
        A_score+=1
        pen.clear()
        pen.write("Player 1 :{} Player 2 :{}".format(A_score,B_score),align="center",font=("courier",22,"normal"))
        
    if ball.xcor()<-390 :
        ball.goto(0,0)
        ball.dx *=-1
        B_score+=1
        pen.clear()
        pen.write("Player 1 :{} Player 2 :{}".format(A_score,B_score),align="center",font=("courier",22,"normal"))

    #Collisions
    if (ball.xcor()>340 and ball.xcor() <350) and (ball.ycor()<rp.ycor()+40 and ball.ycor()>rp.ycor() -40) :
        ball.setx(340)
        ball.dx *=-1
        winsound.PlaySound("bounc.wav", winsound.SND_ASYNC)
        
    if (ball.xcor()<-340 and ball.xcor()>-350) and (ball.ycor()<lp.ycor()+40 and ball.ycor()>lp.ycor() -40) :
        ball.setx(-340)
        ball.dx *=-1    
        winsound.PlaySound("bounc.wav", winsound.SND_ASYNC)
    
    
