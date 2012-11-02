import turtle

turtle.colormode(255)
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
    #turtle.shape("turtle") # I'm a turtle
    color = 1
    for turn_left in path:
        turtle.forward(1)
        if turn_left:
            turtle.left(90)
        else:
            turtle.right(90)
        turtle.pencolor(color & 0xFF,
                        (color >> 8) & 0xFF,
                        (color >> 16) & 0xFF)
        color = color + 1

gogo_turtle(dragon_path(20))
