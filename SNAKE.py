from turtle import Screen, Turtle

    
def go():  
    snake.forward(1)
    screen.ontimer(go, 5)

def left():
    screen.onkeypress(left, 'Left')  # disable handler inside handler
    snake.circle(1, 8)
    screen.onkeypress(left, 'Left')  # reenable handler

def right():
    screen.onkeypress(right, 'Right')
    snake.circle(1, -8)
    screen.onkeypress(right, 'Right')    

screen = Screen()
screen.title("Turn with Left and Right buttons your keyboard. Click on screen to EXIT.")
screen.bgcolor('black')

snake = Turtle()
snake.color('purple')
snake.shape('circle')
snake.shapesize(0.25)
snake.pensize(5)
snake.speed(0)


screen.onkeypress(left, 'Left')
screen.onkeypress(right, 'Right')


go()

screen.listen()
screen.exitonclick()
