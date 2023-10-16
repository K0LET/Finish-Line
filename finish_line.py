import turtle


width = 220
stepX = 10
dirX1 = -1
dirX2 = 1
dirX3 = -1
x1 = 0
y1 = 0
x2 = 0
y2 = 50
x3 = 0
y3 = 100
level = 1
play = 1
score_a = 0
score_b = 0
tigerfail = 0
dragonfail =0
wn = turtle.Screen()

#addshape
wn.addshape('fire.gif')
wn.addshape('tiger.gif')
wn.addshape('dragon.gif')
wn.addshape('bomb.gif')

# Main program
def startGame():
    global x1,x2,y1,y2,x3,y3,score_a,score_b,level,dragonfail,tigerfail
    yoav_logo()
    while (level < 4) and (tigerfail == 0) and (dragonfail == 0):

        Ball1Direction()
        if level > 0:
            x1 = x1 + dirX1 * 2 * level
        ball1.goto(x1, y1)

        Ball2Direction()
        if level >1:
            x2 = x2 + dirX2 * 4 * level
        ball2.goto(x2, y2)

        Ball3Direction()
        if level > 2:
            x3 = x3 + dirX3 * 8 * level
        ball3.goto(x3, y3)

        if Tiger.ycor() > 200:
            Tiger.goto(-150, -190)
            Dragon.goto(150, -190)
            score_a += 1
            level += 1
            pen.clear()
            pen.write("Tiger: {}  Dragon: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

        if Dragon.ycor() > 200:
            Tiger.goto(-150, -190)
            Dragon.goto(150, -190)
            score_b += 1
            level += 1
            pen.clear()
            pen.write("Tiger: {}  Dragon: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

        if Tiger.distance(ball1) < 20:
            ball1.shape("fire.gif")
            tigerfail = 1

        if Tiger.distance(ball2) < 20:
            ball2.shape("fire.gif")
            tigerfail = 1

        if Tiger.distance(ball3) < 20:
            ball3.shape("fire.gif")
            tigerfail = 1

        if Dragon.distance(ball1) < 20:
            ball1.shape("fire.gif")
            dragonfail = 1

        if Dragon.distance(ball2) < 20:
            ball2.shape("fire.gif")
            dragonfail = 1

        if Dragon.distance(ball3) < 20:
            ball3.shape("fire.gif")
            dragonfail = 1


#  Ball1Direction
def Ball1Direction():
    global dirX1
    if ball1.xcor() > 220:
        dirX1 = -1
    elif ball1.xcor() < -220:
        dirX1 = 1

#  Ball2Direction
def Ball2Direction():
    global dirX2
    if ball2.xcor() > 220:
        dirX2 = -1
    elif ball2.xcor() < -220:
        dirX2 = 1

#  Ball3Direction
def Ball3Direction():
    global dirX3
    if ball3.xcor() > 220:
        dirX3 = -1
    elif ball3.xcor() < -220:
        dirX3 = 1


def yoav_logo():
    t = turtle.Turtle()
    t.penup()
    t.goto(-45, 220)
    t.pendown()
    t.color("blue")
    t.write("y", font=("David", 25,))

    t.penup()
    t.goto(-15, 220)
    t.color("green")
    t.write("o", font=("David", 25,))

    t.goto(15, 220)
    t.color("blue")
    t.write("a", font=("David", 25,))

    t.goto(45, 220)
    t.color("green")
    t.write("v", font=("David", 25,))
    t.goto(0, 205)
    t.color("black")
    t.write("FINISH",align="center", font=("David", 12,))

#  t.goto(500,500)
    t.goto(-260,200)
    t.color("black")
    t.pensize(5)
    t.pendown()
    t.goto(260,200)
# Tiger
wn = turtle.Screen()
Tiger = turtle.Turtle()
Tiger.speed(0)
Tiger.shape("tiger.gif")
Tiger.color("blue")
Tiger.shapesize(1)
Tiger.penup()
Tiger.goto(-150, -190)

#  Dragon
wn = turtle.Screen()
Dragon = turtle.Turtle()
Dragon.speed(0)
Dragon.shape("dragon.gif")
Dragon.color("red")
Dragon.shapesize(1)
Dragon.penup()
Dragon.goto(150, -190)

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, -240)
pen.write("Tiger: 0  Dragon: 0", align="center", font=("Courier", 24, "normal"))

# Function
def Tiger_up():
	y = Tiger.ycor()
	y += 20
	Tiger.sety(y)
def Tiger_down():
	y = Tiger.ycor()
	y -= 20
	Tiger.sety(y)


def Dragon_up():
    y = Dragon.ycor()
    y += 20
    Dragon.sety(y)


def Dragon_down():
	y = Dragon.ycor()
	y -= 20
	Dragon.sety(y)

# Keyboard binding
wn.listen()
wn.onkey(Tiger_up, "w")
wn.onkey(Tiger_down, "s")
wn.onkey(Dragon_up, "Up")
wn.onkey(Dragon_down, "Down")

#border
wm = turtle.Screen()
wm.setup(width=500, height=500)
wm.title("Finish Line")
wm.bgcolor("white")

#ball1
wn = turtle.Screen()
ball1 = turtle.Turtle()
ball1.shape("bomb.gif")
ball1.color("black")
ball1.turtlesize(1)
ball1.penup()
ball1.setposition(x1 , y1)
ball1.speed(1)

#ball2
wn = turtle.Screen()
ball2 = turtle.Turtle()
ball2.shape("bomb.gif")
ball2.color("black")
ball2.turtlesize(1)
ball2.penup()
ball2.setposition(x2, y2)
ball2.speed(1)

#ball3
wn = turtle.Screen()
ball3 = turtle.Turtle()
ball3.shape("bomb.gif")
ball3.color("black")
ball3.turtlesize(1)
ball3.penup()
ball3.setposition(x3, y3)
ball3.speed(1)

#finish
startGame()
finish = turtle.Turtle()
finish.speed(0)
finish.color("red")
finish.penup()
finish.hideturtle()
finish.goto(0, 0)
finish.write("Game Over!!!", align="center", font=("Cooper Black", 24, "normal"))
finish.goto(0, -50)
if tigerfail == 1:
    finish.color("green")
    finish.write("Dragon Win", align="center", font=("Cooper Black", 24, "normal"))
elif dragonfail == 1:
    finish.color("#e48324")
    finish.write("Tiger Win", align="center", font=("Cooper Black", 24, "normal"))
elif score_a>score_b:
    finish.color("#e48324")
    finish.write("Tiger Win", align="center", font=("Cooper Black", 24, "normal"))
else:
    finish.color("green")
    finish.write("Dragon Win", align="center", font=("Cooper Black", 24, "normal"))

turtle.mainloop()#addshape
wn.addshape('E:/gif/fire.gif')
wn.addshape('E:/gif/tiger.gif')
wn.addshape('E:/gif/dragon.gif')
wn.addshape('E:/gif/bomb.gif')