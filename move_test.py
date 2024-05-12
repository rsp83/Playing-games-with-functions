def maybe_bounce(position, speed, right_wall):
  """Returns the ball's new position after one time step.
     The ball moves in a straight line at the given speed, bouncing off the right wall.
  """
  new_position = position + speed
  # Check if the ball goes past the right wall
  if new_position > right_wall:
    # Bounce the ball by setting the new position to the right wall
    new_position = right_wall
    # Reverse direction and lose speed with maybe_bounce
    speed = maybe_bounce(position, speed)
  return new_position