from random import choice

"""A class that defines a random walk."""


class RandomWalk():

    def __init__(self, number_points=20000):
        self.number_points = number_points

        # X and Y always starts with 0 since the point needs to start from 0,0
        self.x_value = [0]
        self.y_value = [0]

    def walk(self):
        while len(self.x_value) < self.number_points:
            x_direction = choice([-1, 1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([-1, 1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            next_x = self.x_value[-1] + x_step
            next_y = self.y_value[-1] + y_step

            self.x_value.append(next_x)
            self.y_value.append(next_y)
