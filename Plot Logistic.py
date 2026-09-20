from graphics import *

def main():
    win = GraphWin("Logistic Graph", 800, 600)

    # axes
    Line(Point(50,550), Point(750,550)).draw(win)
    Line(Point(50,550), Point(50,50)).draw(win)

    p = 0.1
    r = 0.2

    for x in range(100):

        screenX = 50 + x * 7
        screenY = 550 - p * 400

        Point(screenX, screenY).draw(win)

        p = p + r * p * (1 - p)

    win.getMouse()
    win.close()

main()