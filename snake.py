import turtle as t

SPEED = 20


class Snake:

    def __init__(self):
        self.pos = None
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """ creates a snake with three segments """
        for n in range(0, 3):
            self.pos = (n * -20, 0)
            self.add_segment(self.pos)

    def add_segment(self, position):
        """ adds segments """
        new_segment = t.Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        """ extends the snake by one segment to the end """
        self.add_segment(self.segments[-1].position())

    def move(self):
        """ moves the snake forward with a specific speed """
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(SPEED)

    def up(self):
        if self.head.heading() == 90 or self.head.heading() == 270:
            pass
        else:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() == 90 or self.head.heading() == 270:
            pass
        else:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() == 0 or self.head.heading() == 180:
            pass
        else:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() == 0 or self.head.heading() == 180:
            pass
        else:
            self.head.setheading(0)
