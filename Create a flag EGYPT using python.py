#YM2 SCHOOL CODING
import turtle

# Title on the window

pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("The  EGYPT Flag by YM2 School",
          align="center",
          font=("Arial", 24, "normal"))


Screen = turtle.Screen()
Screen.bgcolor("white")
Screen.title("Flags")
Screen.screensize(120,100)
wop = turtle.Turtle()
wop.shape("turtle")
wop.up()
wop.goto(-350,200)
wop.down()

wop.color("red")
wop.speed(20)

for i in range(70):
    wop.fd(700)
    wop.rt(90)
    wop.fd(1)
    wop.rt(90)
    wop.fd(700)
    wop.lt(90)
    wop.fd(1)
    wop.lt(90)
    
wop.color("white")
for i in range(70):
    wop.fd(700)
    wop.rt(90)
    wop.fd(1)
    wop.rt(90)
    wop.fd(700)
    wop.lt(90)
    wop.fd(1)
    wop.lt(90)
    
wop.color("black")
for i in range(70):
    wop.fd(700)
    wop.rt(90)
    wop.fd(1)
    wop.rt(90)
    wop.fd(700)
    wop.lt(90)
    wop.fd(1)
    wop.lt(90)
    
wop.fd(700)

# def write (message,pas,color,size) :
#     x,y = pas
#     wop.color(color)
#     wop.penup()
#     wop.goto(x,y)
#     wop.pendown()
#     style = ("Arial",size,"italic")
#     wop.write(message,font=style)
# write("Germany",(-200,200),"black",80)

wop.hideturtle()
turtle.mainloop()
