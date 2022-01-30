from turtle  import Turtle, Screen
import random


screen = Screen()
colors = ['green', 'pink', 'purple', 'orange', 'red', 'blue']
y_positions = [-120, -80, -40, 0, 40, 80, 120]
screen.setup(width = 500, height = 400)
user_input = screen.textinput(title = 'make your bet', prompt = 'which turtle will win?')
all_turtles = []

for i in range(6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.goto(-240, y_positions[i])
    new_turtle.color(colors[i])
    all_turtles.append(new_turtle)

if user_input:
    race = True
if race:
    game = True
    while game:
        for turtle in all_turtles:
            rand_distance = random.randint(0, 10)
            turtle.forward(rand_distance)
            if turtle.xcor()>210:
                game = False
                winning_color = turtle.pencolor()
                if winning_color == user_input:
                    print(f'You won! {winning_color} won the race!')
                else:
                    print(f'You lost!{winning_color} won the rce!')





# def move():
#     timmy.fd(10)
#
#
# def turn_left():
#     timmy.left(10)
#
#
# def turn_right():
#     timmy.left(10)
#
# def backwards():
#     timmy.backward(10)
#
# def clear():
#     timmy.clear()
#     timmy.reset()
#
# screen.listen()
# screen.onkey(key = 'w', fun = move)
# screen.onkey(key = 'a', fun = turn_left)
# screen.onkey(key = 'd', fun = turn_right)
# screen.onkey(key = 's', fun = backwards)
# screen.onkey(key = 'c', fun = clear)
#
screen.exitonclick()