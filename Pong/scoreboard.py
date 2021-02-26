from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Times New Roman", 30, "bold")
SCORE_LOCATIONS = [(-50, 250), (50, 250)]


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.seth(270)
        self.pensize(5)
        self.make_center_line()
        self.player_one_score = 0
        self.player_two_score = 0
        self.setup_scoreboard()


    def make_center_line(self):
        self.goto(0, 300)
        for i in range(0, 10):
            self.forward(30)
            self.pendown()
            self.forward(30)
            self.penup()

    def setup_scoreboard(self):
        self.goto(SCORE_LOCATIONS[0])
        self.write(f"{self.player_one_score}", font=FONT, align=ALIGNMENT)
        self.goto(SCORE_LOCATIONS[1])
        self.write(f"{self.player_two_score}", font=FONT, align=ALIGNMENT)

    def increase_score(self, player):
        if player == 1:
            self.player_one_score += 1
        else:
            self.player_two_score += 1
        self.clear()
        self.make_center_line()
        self.setup_scoreboard()

    def display_winner(self, winner):
        self.goto(0, 0)
        if winner == 1:
            self.write("Player One Win!!!", font=FONT, align=ALIGNMENT)
        else:
            self.write("Player Two Win!!!", font=FONT, align=ALIGNMENT)


