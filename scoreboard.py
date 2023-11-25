from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.setpos(0, 280)
        self.score = 0
        with open("data.txt") as data:
            self.high_score = data.read()

    def write_score(self):
        self.clear()
        self.setpos(0, 280)
        self.color("white")
        self.write(arg=f"Your Score: {self.score}, High Score: {self.high_score}", move=True, align="center", font=('Arial', 17, 'normal'))

    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            with open("data.txt", mode='w') as data:
                data.write(str(self.high_score))
        self.score = 0
        self.setpos(0, 280)
        self.clear()
        self.write(arg=f"Your Score: {self.score}, High Score: {self.high_score}", move=True, align="center",
                   font=('Arial', 17, 'normal'))


