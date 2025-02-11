from turtle import Screen, Turtle
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

# Turtle for displaying "PAUSED" and "GAME OVER" messages
message_turtle = Turtle()
message_turtle.color("white")
message_turtle.hideturtle()

# Function to toggle pause state
def toggle_pause():
    global paused
    paused = not paused
    if paused:
        message_turtle.clear()
        message_turtle.write(
            "PAUSED", align="center", font=("Arial", 24, "normal")
        )
    else:
        message_turtle.clear()

# Function to display game over message
def game_over_screen():
    message_turtle.clear()
    message_turtle.write(
        "GAME OVER\nPress 'R' to Restart", align="center", font=("Arial", 24, "bold")
    )

# Function to restart the game
def restart_game():
    global game_is_on, paused
    message_turtle.clear()
    snake.reset()
    scoreboard.reset()
    food.refresh()
    paused = False  # Ensure the game isn't paused after restarting
    game_loop()  # Start the game again

# Key bindings
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(toggle_pause, "p")  # Bind the "P" key to pause/resume
screen.onkey(restart_game, "r")  # Bind the "R" key to restart the game

# Main game loop function
def game_loop():
    global game_is_on
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
                game_over_screen()
                game_is_on = False  # End the game loop

            # Detect collision with tail
            for segment in snake.segments:
                if segment == snake.head:
                    pass
                elif snake.head.distance(segment) < 10:
                    game_over_screen()
                    game_is_on = False  # End the game loop

# Start the game for the first time
game_loop()
screen.exitonclick()
