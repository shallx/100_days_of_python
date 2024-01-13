import colorgram
colors = colorgram.extract('hiest.jpg', 20)

color_palatte = []
for color in colors:
    new_color = []
    for col in color.rgb:
        new_color.append(col)
    color_palatte.append(tuple(new_color))

print(color_palatte)