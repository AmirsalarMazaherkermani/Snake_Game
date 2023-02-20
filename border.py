from turtle import Turtle
LOCATION_Y = [(0, 320), (0, -320)]
LOCATION_X = [(320, 0), (-320, 0)]


class Border:

    def __init__(self):
        self.borders = []
        self.screensize = None

    def screen_border(self, screensize):
        self.screensize = screensize
        for y in LOCATION_Y:
            new_b = Turtle()
            new_b.shape("square")
            new_b.penup()
            new_b.shapesize(1, self.screensize / 20 + 3)
            new_b.color("white")
            new_b.goto(y)
            self.borders.append(new_b)

        for x in LOCATION_X:
            new_b = Turtle()
            new_b.shape("square")
            new_b.penup()
            new_b.shapesize(self.screensize / 20 + 3, 1)
            new_b.color("white")
            new_b.goto(x)
            self.borders.append(new_b)
