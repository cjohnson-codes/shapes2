from graphics import *
from math import *

def main():
    n = int(input("Number of sides: "))
    radius = float(input("Radius: "))

    win = GraphWin("Rotated Polygon", 500, 500)

    centerX = 250
    centerY = 250

    vertices = []

    angle_between = 360 / n

    rotation = radians(-90 + angle_between / 2)

    for i in range(n):
        angle = radians(i * angle_between) + rotation

        x = centerX + radius * cos(angle)
        y = centerY - radius * sin(angle)

        vertices.append(Point(x, y))

    poly = Polygon(vertices)
    poly.draw(win)

    win.getMouse()
    win.close()

main()