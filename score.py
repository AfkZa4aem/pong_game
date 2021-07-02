from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 40, "normal")


class Score(Turtle):

    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.ht()
        self.goto(position)
        self.current_score = 0
        self.show_score()

    def show_score(self):
        self.write(f"{self.current_score}", align=ALIGNMENT, font=FONT)

    def add_point(self):
        self.clear()
        self.current_score += 1
        self.show_score()
