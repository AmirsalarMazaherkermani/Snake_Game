from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.85, 0.85)
        self.color("yellow")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """ makes a dot as a feed in a random place """
        x_location = random.randint(-280, 280)
        y_location = random.randint(-280, 280)
        self.goto(x_location, y_location)
