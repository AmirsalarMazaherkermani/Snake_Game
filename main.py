import turtle as t
import time
import snake
import food
import scoreboard
import border

screen_size = 600
screen = t.Screen()
screen.screensize(screen_size, screen_size)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

snake = snake.Snake()
food = food.Food()
score = scoreboard.Score()
border = border.Border()
border.screen_border(screen_size)

screen.listen()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.15)
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")
    snake.move()

    if snake.head.distance(food) < 18:
        food.refresh()
        score.add_score()
        snake.extend()

    if snake.head.xcor() > screen_size / 2 or snake.head.xcor() < -screen_size / 2 or \
            snake.head.ycor() > screen_size / 2 or snake.head.ycor() < -screen_size / 2:
        score.game_over()
        game_is_on = False

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()


screen.exitonclick()
