num_iteration = 2
distance = 200 / num_iteration
angles = [0, 120, -120, -120, 120, 120, 0, 120, 0]

def triforce(distance, i):
    if i > 0:
        triforce(distance / 2, i - 1)
    for i in range(num_iteration):
        for angle in angles:
            t.right(angle)
            t.forward(distance/2)
        t.penup()
        t.right(120)
        t.forward(distance)
        t.pendown()
        
triforce(distance, num_iteration)
