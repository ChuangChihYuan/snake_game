from turtle import Turtle
import os

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.ht()
        self.penup()
        self.goto(0, 265)
        self.score = 0
        self.highscore = 0

        if os.path.exists("test.txt") == True:
            self.file = open("test.txt", mode="r")
            self.test_text = self.file.read()
            print(self.test_text)
            self.file.close()
            self.highscore = int(self.test_text)
        else:
            self.file = open("test.txt", mode="w+")
            self.file.write(f"{self.highscore}")
            self.file.close()

            self.file = open("test.txt", mode="r")
            self.test_text = self.file.read()
            print(self.test_text)
            self.file.close()



        self.refresh()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER", align="center", font=('Arial', 30, 'normal'))

    def add_score(self):
        self.score += 1
        self.refresh()

    def refresh(self):
        self.clear()
        self.goto(0, 265)
        self.write(arg=f"SCORE : {self.score} , HIGH SCORE : {self.highscore}", align="center", font=('Arial', 20, 'normal'))

    def highscore_update(self):
        if self.score > self.highscore:
            self.highscore = self.score

            self.file = open("test.txt", mode="w+")
            self.file.write(f"{self.highscore}")
            self.file.close()

            self.file = open("test.txt", mode="r")
            self.test_text = self.file.read()
            print(self.test_text)
            self.file.close()

            self.refresh()
