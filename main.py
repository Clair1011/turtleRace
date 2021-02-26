from turtle import Turtle, Screen
import random


screen = Screen()

screen.setup(width=500, height=400)
user_bat = screen.textinput(title="Make your bat", prompt="Which turtle will win the race? Enter a color: ")
color = ["red", "purple", "blue", "black", "orange", "pink"]
y_position = [-110, -60, -10, 40, 90, 140]

is_race_on = False

all_turtle = []
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.speed(1)
    new_turtle.color(color[turtle_index])
    new_turtle.goto(x=-220, y=y_position[turtle_index])
    all_turtle.append(new_turtle)

if user_bat:
    is_race_on = True

while is_race_on:

    for turtle in all_turtle:
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bat:
                print(f"You've won! The {winning_color} is the winner.")
            else:
                print(f"You've lose! The {winning_color} is the winner.")

screen.exitonclick()