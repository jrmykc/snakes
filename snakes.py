import turtle
import time
import random

# determines how fast the game runs 
delay = 0.05
# the user's score
score = 0

# create window
wn = turtle.Screen()
wn.setup(width=500, height=500)
wn.title("Snakes by Jeremy Koch")
wn.bgcolor("black")
wn.tracer(0) # turns off the animation

# create pen object to display score
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 200)
pen.write("Score: {}".format(score), align="center", font=("Courier", 14, "normal"))


# create the snakes head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("lime")
head.penup()
head.goto(0,0)
head.direction = "stop"

# initialize the snakes body
segments = []

# create the apple that the snake 'eats'
apple = turtle.Turtle()
apple.speed(0)
apple.shape("circle")
apple.color("red")
apple.penup()
apple.goto(random.randrange(-240, 240, 1), random.randrange(-240, 240, 1))

# snake movement with 'wasd' and arrow keys
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

# Listeners
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

# Main Gameloop
while True:
    wn.update()

    # Check collision with border
    if head.xcor() > 240 or head.xcor() < -240 or head.ycor() > 240 or head.ycor() < -240:
        pen.clear()
        pen.write("Game Over - Score = {}".format(score), align="center", font=("Courier", 14, "normal"))
        time.sleep(2) # not optimal (better: wait for user input)
        head.goto(0,0)
        head.direction = "stop"
        score = 0
        pen.clear()
        pen.write("Score: {}".format(score), align="center", font=("Courier", 14, "normal"))
        for segment in segments:
            segment.goto(1000,1000)
        segments.clear()
        apple.goto(random.randrange(-240, 240, 1), random.randrange(-240, 240, 1))

    # Check collision with body
    for segment in segments:
        if head.distance(segment) < 20:
            pen.clear()
            pen.write("Game Over - Score = {}".format(score), align="center", font=("Courier", 14, "normal"))
            time.sleep(2)
            head.goto(0,0)
            head.direction = "stop"
            score = 0
            pen.clear()
            pen.write("Score: {}".format(score), align="center", font=("Courier", 14, "normal"))
            for segment in segments:
                segment.goto(1000,1000)
            segments.clear()
            apple.goto(random.randrange(-240, 240, 1), random.randrange(-240, 240, 1))
    
    # snakes eats apple
    if head.distance(apple) < 20:
        # update score
        score += 1
        pen.clear()
        pen.write("Score: {}".format(score), align="center", font=("Courier", 14, "normal"))
        # update apple position
        apple.goto(random.randrange(-240, 240, 1), random.randrange(-240, 240, 1))

        # create new segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("green")
        new_segment.penup()
        segments.append(new_segment)

    # move end segments first in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # move segment 0 to head
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()
    
    time.sleep(delay)