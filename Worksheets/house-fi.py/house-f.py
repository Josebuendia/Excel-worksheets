import turtle

myPic = turtle.Turtle()
myPic.pencolor("red")
myPic.pensize(3)

#the building outine

length = 200
x = 0
y = 0

myPic.penup()
myPic.setposition(x - 100, y - 100)
myPic.pendown()
myPic.forward(length)
myPic.left(90)
myPic.forward(length)
myPic.left(90)
myPic.forward(length)
myPic.left(90)
myPic.forward(length)
myPic.left(90)

#the roof

myPic.pencolor("black")
myPic.penup()
myPic.forward(length)
myPic.left(90)
myPic.forward(length)
myPic.pendown()
myPic.pensize(3)
myPic.left(45)
myPic.forward(length)
myPic.left(112)
myPic.forward(length-45)

#the door

x = x + 100
y = y + 100

myPic.penup()
myPic.right(157)
##myPic.setposition(x-70,y-200)
myPic.setposition(20,-100)
myPic.pendown()
myPic.forward(100)
myPic.left(90)
myPic.forward(50)
myPic.left(90)
myPic.forward(100)
myPic.left(90)
myPic.forward(50)
myPic.left(90)
myPic.pendown()

#the circular window

x = x + 200
y = y + 200


myPic.penup()
myPic.pencolor("red")
myPic.pensize(3)
myPic.setposition(70,50)
myPic.pendown()
myPic.circle(25,360,8)

#the rectangle window

myPic.penup()
myPic.right(180)
myPic.setposition(-65,70)
myPic.pendown()
myPic.forward(45)
myPic.left(90)
myPic.forward(35)
myPic.left(90)
myPic.forward(45)
myPic.left(90)
myPic.forward(35)
myPic.left(90)
myPic.pendown()

#the grass


myPic.penup()
myPic.pencolor("green")
myPic.setposition(-100,-100)
myPic.pendown()
myPic.right(90)
myPic.forward(100)

myPic.penup()
myPic.pencolor("green")
myPic.setposition(100,-100)
myPic.pendown()
myPic.left(180)
myPic.forward(100)



#the chiminey

myPic.penup()
myPic.pencolor("black")
myPic.setposition(100,100)
myPic.left(90)
myPic.pendown()
myPic.forward(45)
myPic.left(90)
myPic.forward(35)
myPic.left(90)
myPic.forward(45)
myPic.left(90)
myPic.forward(35)
myPic.left(90)
myPic.pendown()

#grass 2

myPic.penup()
myPic.pencolor("green")
myPic.setposition(-100,-100)
myPic.pendown()
myPic.right(90)
myPic.forward(100)

myPic.penup()
myPic.pencolor("green")
myPic.setposition(100,-100)
myPic.pendown()
myPic.left(180)
myPic.forward(100)

#grass 3

myPic.penup()
myPic.pencolor("green")
myPic.setposition(-100,-100)
myPic.pendown()
myPic.left(90)
myPic.forward(100)

myPic.penup()
myPic.pencolor("green")
myPic.setposition(100,-100)
myPic.pendown()
myPic.right(360)
myPic.forward(100)

turtle.done()






