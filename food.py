from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.shapesize(stretch_wid=0.5, stretch_len =0.5)
        self.penup()
        self.refresh()

    def refresh(self):
        self.goto(random.randint(-280, 280), random.randint(-280, 280))

    def del_all(self):
        self.reset()
        self.shapesize(stretch_wid=0.1, stretch_len=0.1)
        self.ht()
        self.clear()
        #del self.turtlesize
        #del self.refresh