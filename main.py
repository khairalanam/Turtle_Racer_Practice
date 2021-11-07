import turtle
import time
import random

WIDTH, HEIGHT = 500, 500
COLORS = ['red', 'green', 'blue', 'orange', 'yellow',
          'black', 'purple', 'pink', 'cyan', 'brown']


def get_number_of_racers():
    racers = 0
    while True:
        racers = input("Enter the number of racers (2-10): ")

        if racers.isdigit():
            racers = int(racers)
        else:
            print("Invalid Input! Please try again!")
            continue

        if 2 <= racers <= 10:
            return racers
        else:
            print("Number not in range! Please try again!")


def create_turtles(colors):
    turtles = []
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos()
        racer.pendown()
        turtles.append(racer)


def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Muck Turtle Race")


racers = get_number_of_racers()
init_turtle()

random.shuffle(COLORS)
colors = COLORS[:racers]
create_turtles(colors)
