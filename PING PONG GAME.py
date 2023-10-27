import turtle
import os
import time
import csv


wn = turtle.Screen()
wn.title("Pong Ping_PF")
wn.bgcolor("red")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0
result=[]
final_scores=[]
header=['Player A','Player B']

# Paddle A

paddle_a = turtle.Turtle()
paddle_a.speed(5)
paddle_a.shape("square")
paddle_a.color("black")
paddle_a.shapesize(stretch_wid=9, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B

paddle_b = turtle.Turtle()
paddle_b.speed(5)
paddle_b.shape("square")
paddle_b.color("black")
paddle_b.shapesize(stretch_wid=9, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.3
ball.dy = -0.3

# Pen

pen = turtle.Turtle()
pen.speed(0)
pen.color("blue")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Function

def paddle_a_up():
    y = paddle_a.ycor()
    if y < 181:
        y += 90

    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    if y > -181:
        y -= 90
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    if y < 181:
        y += 90
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    if y > -181:
        y -= 90
    paddle_b.sety(y)

# Keyboard binding

wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
# Main game loop

for i in range(3):
    score_a=0
    score_b=0
    result.clear()
    while True:
        wn.update()

        # Move the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Border checking
        if ball.ycor() > 190:
            ball.sety(190)
            ball.dy *= -1
            os.system("afplay bounce.wav&")

        if ball.ycor() < -190:
            ball.sety(-190)
            ball.dy *= -1
            os.system("afplay bounce.wav&")

        if ball.xcor() > 355:
            ball.goto(0, 0)
            ball.dx *= -1
            score_a += 1
            if score_a > 2:
                pen.clear()
                pen.write("Player A Wins", align="center", font=("Courier", 28, "normal"))
                time.sleep(2)
                break

            pen.clear()
            pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

        if ball.xcor() < -355:
            ball.goto(0, 0)
            ball.dx *= -1
            score_b += 1
            if score_b > 2:
                pen.clear()
                pen.write("Player B Wins", align="center", font=("Courier", 28, "normal"))
                time.sleep(2)
                break


            pen.clear()
            pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))


        # Paddle and ball collisions
        if (ball.xcor() > 340 and ball.xcor() < 355) and (ball.ycor() < paddle_b.ycor() + 60 and ball.ycor() > paddle_b.ycor() -60):
            ball.setx(340)

            ball.dx *= -1
            os.system("afplay bounce.wav&")

        if (ball.xcor() < -340 and ball.xcor() > -355) and (ball.ycor() < paddle_a.ycor() + 60 and ball.ycor() > paddle_a.ycor() -60):
            ball.setx(-340)
            ball.dx *= -1
            os.system("afplay bounce.wav&")
    if i == 2:
        pen.clear()
        pen.write("Game Over", align="center", font=("Courier", 30, "normal"))
        time.sleep(4)
    if score_a > score_b:
        result.append(1)
        result.append(0)
    else:
        result.append(0)
        result.append(1)
    final_scores.append(tuple(result))
with open('result.csv', 'w',newline='') as csvfile:
    write = csv.writer(csvfile)
    write.writerow(header)
    for score__a,score__b in final_scores:
        write.writerow([score__a,score__b])
