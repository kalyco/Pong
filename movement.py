import turtle

def paddle_up(paddle):
	y = paddle.ycor()
	if (y <= 240):
		y += 20
		paddle.sety(y)


def paddle_down(paddle):
	y = paddle.ycor()
	if (y >= -220):
		y -= 20
		paddle.sety(y)