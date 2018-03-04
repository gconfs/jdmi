''' To be used in the TP's website '''

def triangle(size):
    t.pendown()
    t.forward(size)
    t.right(120)
    t.forward(size)
    t.right(120)
    t.forward(size)
    t.right(120)
    t.penup()

def sierpinsky(size, level):
    if level == 0:
        triangle(size)
    else:
        size /= 2
        # bottom-left triangle
        sierpinsky(size, level - 1)
        # top triangle
        t.right(60)
        t.forward(size)
        t.left(60)
        sierpinsky(size, level - 1)
        # bottom-right triangle
        t.left(60)
        t.forward(size)
        t.right(60)
        sierpinsky(size, level - 1)
        # return to origin
        t.forward(-size)

sierpinsky(200, 4)

