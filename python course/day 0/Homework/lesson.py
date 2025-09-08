from turtle import*
#i want to paint a house  

#step 1 draw a square

shape("turtle")
width(10)
color("tan")

speed(100)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(70)
color("brown")

left(90)
forward(110)        

left(-90)
forward(70)

left(-90)
forward(110)
        
penup()
goto(200, 200)

right(145)
pendown()
color("yellow")

forward(170)
left(108)

forward(170)

penup()
color("blue")
goto(20, 130)

left(127)
pendown()
forward(30)

left(90)
forward(30)

left(90)
forward(30)

left(90)
forward(30)

penup()
goto(150, 130)

pendown()

left(90)
forward(30)

left(90)
forward(30)

left(90)
forward(30)

left(90)
forward(30)

exitonclick()
