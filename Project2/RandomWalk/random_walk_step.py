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

        # Set moving range further
        self.x_range = [value for value in range(0,9)]
        self.y_range = [value for value in range(0,9)]

    def fill_walk(self):
        # Calculate all the points in the walk #
        
        # Keep talking steps until the walk reaches the desired length. #
        while len(self.x_values) < self.num_points:
            
            # Decide which direction to go and how far to go in that direction.
            x_direction = choice([1,  0])           # set x to [1,0], i.e. no moving left
            x_distance = choice(self.x_range)
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice(self.y_range)
            y_step = y_direction * y_distance

            # Reject moves that ho nowhere. #
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the new position. #
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)
