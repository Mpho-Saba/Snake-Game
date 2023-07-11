from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.openDataFile()
        self.color("white")

        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.updateScoreBoard()

    def openDataFile(self):
        with open("data.txt", 'r') as file:
            return int(file.read())

    def updateScoreBoard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", move=True, align="center")

    def increaseScore(self):
        self.score = self.score + 2
        self.updateScoreBoard()

    def reset(self):
        if(self.score > self.high_score):
            with open("data.txt", 'w') as file:
                file.write(self.score)
            self.high_score = self.score
        self.score = 0