import turtle
from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import random
import time
import gc
import os
import psutil
import sys

FOOD_NUMS = 3

# 顯示當前 python 程式佔用的記憶體大小
def show_memory_info(hint):
    pid = os.getpid()
    p = psutil.Process(pid)

    info = p.memory_full_info()
    memory = info.uss / 1024. / 1024
    print('{} memory used: {} MB'.format(hint, memory))

gc.enable()

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkeypress(fun=snake.up, key="w")
screen.onkeypress(fun=snake.down, key="s")
screen.onkeypress(fun=snake.left, key="a")
screen.onkeypress(fun=snake.right, key="d")

scoreboard = Scoreboard()

foods = []
for food_num in range(FOOD_NUMS):
    new_food = Food()
    foods.append(new_food)

is_game_on = True

while is_game_on:
    snake.move()
    time.sleep(0.1)
    screen.update()

    for i in range(len(foods)):
        if snake.head.distance(foods[i]) < 15:
            foods[i].refresh()
            snake.add_snake_segment()
            scoreboard.add_score()

    for segment in snake.segment[1::]:
        if snake.head.distance(segment) < 5 :
            print(snake.segment[0].position())
            print(snake.segment[1].position())
            print(snake.segment[2].position())
            scoreboard.highscore_update()
            scoreboard.game_over()
            screen.update()
            time.sleep(1)
            scoreboard.score = 0
            scoreboard.refresh()
            snake.reset()
            screen.update()


            #is_game_on = False


    

screen.exitonclick()
