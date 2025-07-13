# Python Crash Course, 2Ed, writtern by Eric Matthes

from random import choice

class Randomwalk:
# A class to generate random walks. #

    def __init__(self, num_points = 5000):
        # Initialize attricutes of a walk. #
        self.num_points = num_points

        # All walks start at (0,0)
        self.x_values = [0]
        self.y_values = [0]

        # determine the range possible for each steps
        self.step = [value for value in range(0,9)]

        
    def get_step(self):
        # Decide which direction to go and how far to go in that direction.
        direction = choice([1, -1])
        distance = choice(self.step)
        step = direction * distance
        return step

    def fill_walk(self):
        # Calculate all the points in the walk #
        # Keep talking steps until the walk reaches the desired length. #
        while len(self.x_values) < self.num_points:
            
            x_step = self.get_step()
            y_step = self.get_step()

            # Reject moves that go nowhere. #
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the new position. #
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)
