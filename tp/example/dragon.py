import turtle
import colorsys

# left = True
# right = False
def dragon_path(iteration):
    path = []
    for i in range(iteration):
        reverse_path = list(path)
        reverse_path.reverse()
        path.append(True)
        path.extend([not i for i in reverse_path])
    return path

def gogo_turtle(path):
    turtle.speed(0) # super turtle mode
    turtle.hideturtle()
    i = 0
    #turtle.shape("turtle") # I'm a turtle
    for i, turn_left in enumerate(path):
        turtle.pencolor(colorsys.hls_to_rgb(float(i) / float(len(path)), .5, .5))
        turtle.forward(1)
        if turn_left:
            turtle.left(90)
        else:
            turtle.right(90)

gogo_turtle(dragon_path(15))
import time
time.sleep(10000)
