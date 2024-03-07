from turtle import Turtle

START_POSITION  = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
class Snake:

    def __init__(self):
        self.segment = []
        for position in START_POSITION:
            new_snake = Turtle()
            new_snake.shape("square")
            new_snake.shapesize(stretch_wid=0.9, stretch_len=0.9)
            if len(self.segment) == 0:
                new_snake.color("white")
            else:
                new_snake.color("white")
            new_snake.penup()
            new_snake.goto(position)
            self.segment.append(new_snake)
        self.head = self.segment[0]

    def reset(self):
        for segment in self.segment[3::]:
            segment.goto(1000, 1000)

        del self.segment[3::]

        self.head.goto(START_POSITION[0])
        self.segment[1].goto(START_POSITION[1])
        self.segment[2].goto(START_POSITION[2])
    def add_snake_segment(self):
        new_snake = Turtle()
        new_snake.shape("square")
        new_snake.shapesize(stretch_wid=0.9, stretch_len=0.9)
        new_snake.color("white")
        new_snake.penup()
        new_snake.goto(self.segment[-1].pos())
        self.segment.append(new_snake)

    def move(self):
        for num in range(len(self.segment) - 2, -1, -1):
            self.segment[num + 1].goto(self.segment[num].position())
        self.head.forward(MOVE_DISTANCE)

        if self.head.xcor() > 300:
            self.head.setx(-300)
        if self.head.xcor() < -300:
            self.head.setx(300)

        if self.head.ycor() > 300:
            self.head.sety(-300)
        if self.head.ycor() < -300:
            self.head.sety(300)

    def getheading(self):
        return self.head.heading()

    def setheading(self, snake_run_nums):
        self.head.setheading(snake_run_nums)

    def up(self):
        if self.getheading() != 270:
            self.setheading(90)
    def down(self):
        if self.getheading() != 90:
            self.setheading(270)

    def left(self):
        if self.getheading() != 0:
            self.setheading(180)

    def right(self):
        if self.getheading() != 180:
            self.setheading(0)