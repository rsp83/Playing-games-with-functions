"""Simulates a ball's movement and collision with the edges of a screen."""

def move(position, speed, right_wall):
  """Returns the ball's new position after one time step.
     The ball moves in a straight line at the given speed, bouncing off the right wall.
  """
  new_position = position + speed
  if new_position > right_wall:
    # Bounce the ball by setting the new position to the right wall
    new_position = right_wall
    # Update speed with maybe_bounce
    speed = maybe_bounce(position, speed)
  return new_position

def maybe_bounce(position, speed, right_wall):
  """Returns the ball's new speed, which bounces off the right wall and slows down.
     This function is modified to avoid an infinite loop.
  """
  # Check if the ball is at or past the right wall
  if position >= right_wall:
    # Reverse direction and lose a bit of speed.
    speed = speed * -0.75
  return speed