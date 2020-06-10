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

class BouncingBall():
    def __init__(self, building_height):
        self.building_height = building_height
        self.ball_bounce = 0.66
        self.window = 1.5
        self.bounce_times = 1

    def conditions_passed(self):
        condition_1 = self.building_height > 0
        condition_2 = 0 > self.ball_bounce < 1
        condition_3 = self.window < self.building_height
        if (condition_1 | condition_2 | condition_3) == False:
            return False
        else:
            return True

    def bounce_ball(self, bouncy):
        if (bouncy > self.window):
            self.bounce_times += 2
            bounced = bouncy * self.ball_bounce
            return self.bounce_ball(bounced)
        else:
            pass
    
    def start(self):
        if self.conditions_passed() == True:
            bounce_formula = self.building_height * self.ball_bounce
            self.bounce_ball(bounce_formula)
            return self.bounce_times
        else:
            return -1


###################
# Other Solutions #
###################

def bouncingBall(h, bounce, window):
    if not 0 < bounce < 1: 
        return -1
    count = 0

    while h > window:
        count += 1
        h *= bounce
        if h > window: count += 1
    return count or -1