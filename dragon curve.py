import turtle
'''
1 = 90 degree
-1 = -90 degree

1
1 1 -1
1 1 -1 1 1 -1 -1
'''

def dragon_curve(turtle1, order, length, angle):  # draw dragon curve function
    direction = [1]
    # preparation for turning direction
    for curve in range(order):
        reverse_direction = direction[::-1]
        direction.append(1)
        for num in reverse_direction:
            direction.append(num * -1)

    # drawing the curve
    for turns in direction:
        turtle1.forward(length)
        turtle1.left(turns * angle)


# input for personalization
iteration = int(input('how many iteration: '))
length = float(input('how long is the segment: '))
angle = float(input('What is the turning angle for the curve you want: '))
pen_color = input('what color for the curve: ').lower()
background_color = input('what background color: ').lower()
work = input('how you want your curve done (instant/slow): ').lower()

# create turtle (pointer)
dragon = turtle.Turtle()
dragon.hideturtle()
dragon.speed(0)
dragon.color(pen_color)

# create screen
screen = turtle.Screen()
screen.title('Dragon Curve')
screen.bgcolor(background_color)

if work == 'instant':
    turtle.tracer(0, 0)
    dragon_curve(dragon, iteration, length, angle)
    turtle.update()
else:
    dragon_curve(dragon, iteration, length, angle)

turtle.exitonclick()
