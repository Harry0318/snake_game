from turtle import Turtle

FONT = ("Arial", 14, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high_score.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write_score()
        self.hideturtle()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score} High score:{self.high_score}", align="center", font=FONT)

    def increase_score(self):
        self.score += 1
        self.write_score()

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt",mode="w") as data:
                data.write(f"{self.high_score}")
        self.score=0
        self.write_score()


    #def game_over(self):
    #    self.goto(0,0)
    #    self.write(f"GAME OVER  ", align="center", font=FONT)


