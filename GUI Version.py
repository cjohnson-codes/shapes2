from graphics import *

def inside(p, p1, p2):
    return p1.getX() <= p.getX() <= p2.getX() and \
           p1.getY() <= p.getY() <= p2.getY()


def main():

    win = GraphWin("Logistic Grapher", 900, 600)

    # axes
    Line(Point(50,550), Point(750,550)).draw(win)
    Line(Point(50,550), Point(50,50)).draw(win)

    Text(Point(830,100), "Initial P").draw(win)
    pEntry = Entry(Point(830,130), 10)
    pEntry.setText("0.1")
    pEntry.draw(win)

    Text(Point(830,180), "Growth Rate").draw(win)
    rEntry = Entry(Point(830,210), 10)
    rEntry.setText("0.2")
    rEntry.draw(win)

    buttonRect = Rectangle(Point(780,300), Point(880,350))
    buttonRect.draw(win)

    buttonText = Text(Point(830,325), "Graph")
    buttonText.draw(win)

    while True:

        click = win.getMouse()

        if inside(click,
                  Point(780,300),
                  Point(880,350)):

            if buttonText.getText() == "Graph":

                p = float(pEntry.getText())
                r = float(rEntry.getText())

                oldPoint = None

                for x in range(100):

                    screenX = 50 + x * 7
                    screenY = 550 - p * 400

                    currentPoint = Point(screenX, screenY)

                    if oldPoint is not None:
                        Line(oldPoint, currentPoint).draw(win)

                    oldPoint = currentPoint

                    p = p + r * p * (1 - p)

                buttonText.setText("Exit")

            else:
                break

    win.close()

main()