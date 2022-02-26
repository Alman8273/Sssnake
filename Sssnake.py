#snake game
#importing libraries
import turtle #draw on screen w keyboard (like turtle sim on ROS)
import random
import time

#creating turtle screen
screen = turtle.Screen()
screen.cv._rootwindow.resizable(False, False)
screen.title('Sssnanke')
screen.setup(width = 700, height = 700)
screen.tracer(0)
#turtle.bgpic("back.jpg")
turtle.bgcolor('#33964e')

turtle.speed(5)
turtle.pensize(4)
turtle.penup()
turtle.goto(-310,250)
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

#score
score = 0
delay = 0.1

#snake
Turtle = turtle.Turtle()
Turtle.speed(0)
Turtle.shape('turtle') #head #tutle icon
Turtle.color("yellow") #head
Turtle.penup()
Turtle.goto(0,0)
Turtle.direction = 'stop'

#food
fruit = turtle.Turtle()
fruit.speed(0)
fruit.shape('circle')
fruit.color('red')
fruit.penup()
fruit.goto(30,30)

tailOld=[]

#scoring
scoring = turtle.Turtle()
scoring.speed(0)
scoring.color("black")
scoring.penup()
scoring.hideturtle()
scoring.goto(0,300)
scoring.write("Score: ",align="center",font=("Times",24,"bold"))


#how to move
def snake_go_up():
    if Turtle.direction != "down":
        Turtle.direction = "up"
                
def snake_go_down():
    if Turtle.direction != "up":
        Turtle.direction = "down"
        
def snake_go_left():
    if Turtle.direction != "right":
        Turtle.direction = "left"
   
def snake_go_right():
    if Turtle.direction != "left":
        Turtle.direction = "right"
        
        # #set heading
        # snake.setheading(0)
        # snake.setheading(90)
        # snake.setheading(180)
        # snake.setheading(270)
        
def snake_move():
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

# Keyboard keys
screen.listen()
screen.onkeypress(snake_go_up, "Up")
screen.onkeypress(snake_go_down, "Down")
screen.onkeypress(snake_go_left, "Left")
screen.onkeypress(snake_go_right, "Right")

#main 
while True:
        screen.update()
            #hit fruit
        if Turtle.distance(fruit)< 20:
                x = random.randint(-290,270)
                y = random.randint(-240,240)
                fruit.goto(x,y)
                scoring.clear()
                score+=1
                scoring.write("Score:{}".format(score),align="center",font=("Times",24,"bold"))
                delay-=0.001
                
                #create taill
                tailAdd = turtle.Turtle()
                tailAdd.speed(0)
                tailAdd.shape('square')
                tailAdd.color('black')
                tailAdd.penup()
                tailOld.append(tailAdd)
            #adding tail ^^^^        
        for index in range(len(tailOld)-1,0,-1):
                a = tailOld[index-1].xcor()
                b = tailOld[index-1].ycor()

                tailOld[index].goto(a,b)
                                     
        if len(tailOld)>0:
                a= Turtle.xcor()
                b = Turtle.ycor()
                tailOld[0].goto(a,b)
        snake_move()

        #hit wall  
        if Turtle.xcor()>280 or Turtle.xcor()< -300 or Turtle.ycor()>240 or Turtle.ycor()<-240:
                time.sleep(1)
                screen.clear()
                screen.bgcolor('turquoise')
                scoring.goto(0,0)
                scoring.write("   GAME OVER \n      Your Score  \n\t{}".format(score),align="center",font=("Times",70,"bold"))


        ## snake collision
        for food in tailOld:
                if food.distance(Turtle) < 20:
                        time.sleep(1)
                        screen.clear()
                        screen.bgcolor('turquoise')
                        scoring.goto(0,0)
                        scoring.write("    GAME OVER \n Your Score is {}".format(score),align="center",font=("Courier",30,"bold"))


                
        time.sleep(delay)

turtle.Terminator()
