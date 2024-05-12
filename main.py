import ball
import graphics


output_width = 19
right_wall = output_width
ball_position = 1
ball_speed = 5

for time_step in range(100):
    # Show the ball's position at the current time step.
    print(graphics.show_screen(ball_position, output_width))
    ball_position = ball.move(ball_position, ball_speed, right_wall)
