import turtle
import time
import random

delay = 0.05
score = 0
# read and save highscore from textfile
with open("snake_highscore.txt", "r") as highscore_data:
    data = highscore_data.read()
    highscore = int(data)

# Create Window
wn = turtle.Screen()
wn.setup(width=500, height=500)
wn.title("Snakes by Jeremy")
wn.bgcolor("black")
wn.tracer(0)

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 200)
pen.write("Score: 0 Highscore: {}".format(highscore), align="center", font=("Courier", 14, "normal"))

# Snakehead
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("lime")
head.penup()
head.goto(0,0)
head.direction = "stop"

# Snakebody
segments = []

# Apple
apple = turtle.Turtle()
apple.speed(0)
apple.shape("circle")
apple.color("red")
apple.penup()
apple.goto(random.randrange(-240, 240, 1), random.randrange(-240, 240, 1))

# Snake Movement
def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)

    if head.direction == "down":
        head.sety(head.ycor() - 20)

    if head.direction == "right":
        head.setx(head.xcor() + 20)

    if head.direction == "left":
        head.setx(head.xcor() - 20)

    if head.direction == "stop":
        pass

def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"    

# Listen
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# Main Gameloop
while True:
    wn.update()

    # Check collision with border
    if head.xcor() > 240 or head.xcor() < -240 or head.ycor() > 240 or head.ycor() < -240:
        pen.clear()
        if score > highscore:
            highscore = score
            pen.write("Game Over - NEW HIGHSCORE! = {}".format(highscore), align="center", font=("Courier", 14, "normal"))
            # Write new highscore in textfile
            f = open("snake_highscore.txt", "w")
            f.write(str(highscore))
        else:
            pen.write("Game Over - Score = {}".format(score), align="center", font=("Courier", 14, "normal"))
        time.sleep(2)
        head.goto(0,0)
        head.direction = "stop"
        score = 0
        pen.clear()
        pen.write("Score: {} Highscore: {}".format(score, highscore), align="center", font=("Courier", 14, "normal"))
        for segment in segments:
            segment.goto(1000,1000)
        segments.clear()

    # Check collision with body
    for segment in segments:
        if head.distance(segment) < 20:
            pen.clear()
            if score > highscore:
                highscore = score
                pen.write("Game Over - NEW HIGHSCORE! = {}".format(highscore), align="center", font=("Courier", 14, "normal"))
                # write new highscore in textfile
                f = open("snake_highscore.txt", "w")
                f.write(str(highscore))
            else:
                pen.write("Game Over - Score = {}".format(score), align="center", font=("Courier", 14, "normal"))
            time.sleep(2)
            head.goto(0,0)
            head.direction = "stop"
            score = 0
            pen.clear()
            pen.write("Score: {} Highscore: {}".format(score, highscore), align="center", font=("Courier", 14, "normal"))
            for segment in segments:
                segment.goto(1000,1000)
            segments.clear()
    
    # Collision with apple
    if head.distance(apple) < 20:
        # Update score
        score += 1
        pen.clear()
        pen.write("Score: {} Highscore {}".format(score, highscore), align="center", font=("Courier", 14, "normal"))
        # Update apple position
        apple.goto(random.randrange(-240, 240, 1), random.randrange(-240, 240, 1))

        # Create new segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("green")
        new_segment.penup()
        segments.append(new_segment)

    # Move end segments first in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to head
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()

    time.sleep(delay)