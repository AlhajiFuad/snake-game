from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Set up screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# Initialize game components
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Variable to manage pause state
paused = False

# Function to toggle pause state
def toggle_pause():
    global paused
    paused = not paused

# Key bindings
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(toggle_pause, "p")  # Bind the "P" key to pause/resume

# Main game loop
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    # Execute game logic only if not paused
    if not paused:
        snake.move()

        # Detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        # Detect collision with wall
        if (
            snake.head.xcor() > 280 or snake.head.xcor() < -280 or
            snake.head.ycor() > 280 or snake.head.ycor() < -280
        ):
            scoreboard.reset()
            snake.reset()

        # Detect collision with tail
        for segment in snake.segments:
            if segment == snake.head:
                pass
            elif snake.head.distance(segment) < 10:
                scoreboard.reset()
                snake.reset()

screen.exitonclick()
