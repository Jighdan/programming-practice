"""
A child is playing with a ball on the nth floor of a x height building.
He drops the ball out of the window. The ball bounces (for example), to two-thirds of it's height (a bounce of 0.66)
His mother looks out of a window 1.5 meters from the ground.
How many times will the mother see the ball pass in front of her window, incliding when it's falling and bouncing?

Three conditions must be met for a valid experiment:
    - Float parameter "h" in meters must be greater than 0
    - Float parameter "bounce" must be greater than 0 and less than 1
    - Float parameter "window" must be less than h.
"""

def bouncingBall(h, bounce, window):
    if not 0 < bounce < 1: 
        return -1
    count = 0

    while h > window:
        count += 1
        h *= bounce
        if h > window: count += 1
    return count or -1