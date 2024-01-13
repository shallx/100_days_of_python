# import colorgram
# colors = colorgram.extract('hiest.jpg', 20)

# color_palatte = []
# for color in colors:
#     new_color = []
#     for col in color.rgb:
#         new_color.append(col)
#     color_palatte.append(tuple(new_color))

# print(color_palatte)

color_graphs = [(249, 228, 17), (213, 13, 9), (196, 13, 36), (196, 70, 21), (235, 148, 39), (33, 90, 188), (228, 228, 7), (44, 212, 70), (33, 30, 152), (16, 22, 54), (67, 9, 49), (243, 40, 149), (15, 206, 222), (237, 244, 249), (67, 202, 228), (63, 21, 11), (223, 20, 112)]


from turtle import Turtle, colormode
from random import choice

t = Turtle()
colormode(255)
t.screen.screensize(600,600)
t.penup()
for y in range(10):
    for x in range(0,10):
        t.pencolor()
        t.goto(-200 + x*50, -200 + y*50)
        t.dot(20,choice(color_graphs) )


t.screen.mainloop()