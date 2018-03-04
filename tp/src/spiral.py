absolute_distance = 0

def next_color(precision):
    global absolute_distance
    magic = absolute_distance / precision / 15  # I'm ashamed
    t.pencolor(magic, 1 - magic, magic)

def circle(size, precision, level):
    global absolute_distance
    if level == 0:
        return
    distance = 0
    for seg in range(precision * level):
        next_color(precision)
        t.forward((size - distance) / precision)
        t.right(360 / precision)
        distance += 1
        absolute_distance += 1
    circle(size - distance, precision, level - 1)

circle(1000, 50, 5)
