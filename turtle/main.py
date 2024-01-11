import turtle

turtle.bgcolor('black')
t = turtle.Turtle()
colors = ['red', 'dark red']
t.speed(0)

for number in range(300):
    t.forward(number+5)
    t.right(79)
    t.pencolor(colors[number%2])
turtle.done()