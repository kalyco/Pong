import turtle

def make_paddle(coords):
	paddle = turtle.Turtle()
	paddle.speed(0)
	paddle.shape("square")
	paddle.color("white")
	paddle.shapesize(stretch_wid=5, stretch_len=1)
	paddle.penup()
	paddle.goto(coords[0], coords[1])
	return paddle

def make_ball():
	ball = turtle.Turtle()
	ball.speed(0)
	ball.shape("square")
	ball.color("white")
	ball.penup()
	ball.goto(0, 0)
	return ball