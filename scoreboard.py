from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 290)
        self.write_score()

    def write_score(self):
        """ writes the text """
        self.clear()
        self.write(f"Your score is: {self.score}", False, "center", ("Arial", 12, "normal"))

    def game_over(self):
        """ game over text """
        self.clear()
        self.goto(0, -20)
        self.write(f"GAME OVER\nFinal score: {self.score}", False, "center", ("Arial", 12, "bold"))

    def add_score(self):
        """ adds up the score """
        self.score += 1
        self.write_score()
