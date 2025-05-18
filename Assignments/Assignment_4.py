import turtle
import colorsys


screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Geometric Spiral Art")


pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)
pen.hideturtle()


hue = 0
num_shapes = 100  
size = 200       
angle = 15       

for i in range(num_shapes):
    
    color = colorsys.hsv_to_rgb(hue, 1, 1)
    pen.pencolor(color)

    
    for _ in range(4):
        pen.forward(size)
        pen.right(90)

    
    pen.circle(size / 2)

    
    pen.right(angle)
    size -= 2
    hue += 1 / num_shapes  


screen.exitonclick()
