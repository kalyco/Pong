# From @TokyoEdTech tutorial
import turtle
from builders import make_paddle, make_ball
from movement import paddle_down, paddle_up

win = turtle.Screen()
win.title = ("Pong by @kalyco")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

paddle_a = make_paddle([-350, 0])
paddle_b= make_paddle([350, 0])
ball = make_ball()

def paddle_a_up():
	paddle_up(paddle_a)

def paddle_a_down():
	paddle_down(paddle_a)

def paddle_b_up():
	paddle_up(paddle_b)

def paddle_b_down():
	paddle_down(paddle_b)

# Keyboard binding
win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
	win.update()
