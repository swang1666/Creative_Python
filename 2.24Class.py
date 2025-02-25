from turtle import *

speed(0)
color("red")
fillcolor("yellow")

begin_fill()
while True:
    forward(200)
    left(102) # change a different angle value
    if abs(pos()) < 1: # use `abs(pos()) < 1` to determine if turtle is back at it home position
        break
end_fill()

mainloop()




mainloop()