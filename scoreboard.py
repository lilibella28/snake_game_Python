from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 24, 'normal')
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, 270)
        self.color('white')
        self.penup()
        self.score = 0
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font=FONT)

    def score_board(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()


    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align=ALIGNMENT, font=FONT)