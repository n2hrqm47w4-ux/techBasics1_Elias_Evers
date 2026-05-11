from turtle import *
import random

#link for inspo
#https://katharina-werk.org/engelkarten/
# --> vergesslicher Engel (Paul Klee)

#setup
width = 500
height = 650
tracer(1, 5)
bgcolor('#fcfaf5') #paper color
color('#4b3621')   #ink
pensize(2)
hideturtle()

#background
speed(0)
for x in range(-250, 251, 60):
    for y in range(-320, 321, 60):
        if random.random() > 0.75:
            penup()
            goto(x + random.randint(-20, 20), y + random.randint(-20, 20))
            pendown()
            dot(1, "gray")

def draw_klee_line(points):
    wobble = [-1.5, 0, 1.5]
    penup()
    goto(points[0])
    pendown()
    for p in points[1:]:
        target_x = p[0] + random.choice(wobble)
        target_y = p[1] + random.choice(wobble)
        goto(target_x, target_y)


#head
head_coords = [(0, 100), (50, 130), (60, 200), (30, 260), (-30, 260), (-60, 200), (-50, 130), (0, 100)]
draw_klee_line(head_coords)

#wings
left_wing = [(-65, 140), (-200, 300), (-180, -200), (-70, -140)]
right_wing = [(65, 140), (200, 300), (180, -200), (70, -140)]
draw_klee_line(left_wing)
draw_klee_line(right_wing)

# body
chest = [(-65, 140), (10, -120), (65, 140)]
draw_klee_line(chest)

#left arm
left_arm = [(-65, 140), (-150, -30), (-20, -230)]
draw_klee_line(left_arm)

#right arm
right_arm = [(65, 140), (80, -50), (20, -230)]
draw_klee_line(right_arm)

#hands
penup()
goto(-25, -230)
for i in range(4):
    pendown()
    setheading(90)
    forward(25)
    penup()
    goto(xcor() + 12, -230)

#eyes
for start_x in [-35, 15]:
    penup()
    goto(start_x, 210)
    setheading(-60)
    pendown()
    circle(15, 120)

#mouth
penup()
goto(-12, 165)
setheading(-10)
pendown()
circle(40, 25)

done()
