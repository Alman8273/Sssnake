# turtle-time
import turtle  # draw on screen w keyboard (like turtle sim on ROS)
import random
import time

# creating turtle screen
screen = turtle.Screen()
screen.cv._rootwindow.resizable(False, False)
screen.title('Turlte-Time')
screen.setup(width=700, height=690)
screen.tracer(0)
# turtle.bgpic("back.jpg")
turtle.bgcolor('#33964e')

turtle.speed(5)
turtle.pensize(4)
turtle.penup()
turtle.goto(-310, 250)
turtle.pendown()
turtle.color('black')
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.penup()
turtle.hideturtle()

# score
score = 0
delay = 0.1

# snake
Turtle = turtle.Turtle()
Turtle.speed(0)
Turtle.shape('turtle')  # head #tutle icon
Turtle.color("yellow")  # head
Turtle.penup()
Turtle.goto(0, 0)
Turtle.direction = 'stop'

# food
fruit = turtle.Turtle()
fruit.speed(0)
fruit.shape('circle')
fruit.color('red')
fruit.penup()
fruit.goto(30, 30)

tailOld = []

# scoring
scoring = turtle.Turtle()
# instruc = turtle.Turtle
scoring.speed(0)
scoring.color("black")
scoring.penup()
scoring.hideturtle()
scoring.goto(0, 300)
scoring.write("Score: ", align="center", font=("Times", 35, "bold"))
# instruc = turtle.write('ddddddddddddd').place(x=0,y=0)
turtle.goto(0, 255)
turtle.color('orange')
turtle.write("Help Franklin get his children!",
             align='center', font=('Times', 25, 'bold'))


# how to move (heads)
def turtleup():
    if Turtle.direction != "down":
        Turtle.direction = "up"


def turtledown():
    if Turtle.direction != "up":
        Turtle.direction = "down"


def turtleleft():
    if Turtle.direction != "right":
        Turtle.direction = "left"


def turtleright():
    if Turtle.direction != "left":
        Turtle.direction = "right"

# #how to move (tail)
# def tailup():
#     if tailAdd.direction != "down":
#         Turtle.direction = "up"

# def taildown():
#     if tailAdd.direction != "up":
#         tailAdd.direction = "down"

# def tailleft():
#     if tailAdd.direction != "right":
#         tailAdd.direction = "left"

# def tailright():
#     if tailAdd.direction != "left":
#         tailAdd.direction = "right"

# tilts (head)


def turtle_move():
    if Turtle.direction == "up":
        y = Turtle.ycor()
        Turtle.sety(y + 20)
        Turtle.setheading(90)

    if Turtle.direction == "down":
        y = Turtle.ycor()
        Turtle.sety(y - 20)
        Turtle.setheading(270)

    if Turtle.direction == "left":
        x = Turtle.xcor()
        Turtle.setx(x - 20)
        Turtle.setheading(180)

    if Turtle.direction == "right":
        x = Turtle.xcor()
        Turtle.setx(x + 20)
        Turtle.setheading(0)

# tilts (tail)
# def tail_move():
#     if tailAdd.direction == "up":
#         y = Turtle.ycor()
#         tailAdd.sety(y + 20)
#         tailAdd.setheading(90)

    # if Turtle.direction == "down":
    #     y = Turtle.ycor()
    #     Turtle.sety(y - 20)
    #     Turtle.setheading(270)

    # if Turtle.direction == "left":
    #     x = Turtle.xcor()
    #     Turtle.setx(x - 20)
    #     Turtle.setheading(180)

    # if Turtle.direction == "right":
    #     x = Turtle.xcor()
    #     Turtle.setx(x + 20)
    #     Turtle.setheading(0)


# Keyboard keys
screen.listen()
screen.onkeypress(turtleup, "Up")
screen.onkeypress(turtledown, "Down")
screen.onkeypress(turtleleft, "Left")
screen.onkeypress(turtleright, "Right")

# main
while True:
        screen.update()
            # hit fruit
        if Turtle.distance(fruit) < 20:
                x = random.randint(-290, 270)
                y = random.randint(-240, 240)
                fruit.goto(x, y)
                scoring.clear()
                score += 1
                scoring.write("Score:{}".format(score),
                              align="center", font=("Times", 24, "bold"))
                delay -= 0.001

                # create taill
                tailAdd = turtle.Turtle()
                tailAdd.speed(0)
                tailAdd.shape('turtle')
                tailAdd.color('yellow')
                tailAdd.penup()
                tailOld.append(tailAdd)
            # adding tail ^^^^
        for index in range(len(tailOld)-1, 0, -1):
                a = tailOld[index-1].xcor()
                b = tailOld[index-1].ycor()

                tailOld[index].goto(a, b)

        if len(tailOld) > 0:
                a = Turtle.xcor()
                b = Turtle.ycor()
                tailOld[0].goto(a, b)
        turtle_move()

        # hit wall
        if Turtle.xcor() > 280 or Turtle.xcor() < -300 or Turtle.ycor() > 240 or Turtle.ycor() < -240:
                time.sleep(1)
                screen.clear()
                screen.bgcolor('#472526')
                scoring.goto(0, 0)
                scoring.color('#ffffff')
                scoring.write(" GAME OVER \n    Your Score\n            {}".format(score), align="center", font=("Times", 50, "bold"))

        # collision
        for food in tailOld:
            if food.distance(Turtle) < 20:
                     time.sleep(1)
                     screen.clear()
                     screen.bgcolor('#472526')
                     scoring.goto(0,0)
                     scoring.color('#ffffff')
                     scoring.write(" GAME OVER \n    Your Score\n            {}".format(score),align="center",font=("Times",50,"bold"))


                
        time.sleep(delay)

turtle.Terminator() #kill turtle sim
