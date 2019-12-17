from random import choice

"""A class that defines a random walk."""


class RandomWalk():

    def __init__(self, number_points=5000):
        self.number_points = number_points

        # X and Y always starts with 0 since the point needs to start from 0,0
        self.x_value = [0]
        self.y_value = [0]

    def walk(self):
        while len(self.x_value) < self.number_points:
            x_step = self.get_steps_x()
            y_step = self.get_steps_y()
            next_x = self.x_value[-1] + x_step
            next_y = self.y_value[-1] + y_step

            self.x_value.append(next_x)
            self.y_value.append(next_y)

    def get_steps_x(self):
        x_direction = choice([x for x in range(-100, 100)])
        x_distance = choice([x for x in range(1, 100)])
        x_step = x_direction * x_distance
        return x_step

    def get_steps_y(self):
        y_direction = choice([x for x in range(-100, 100)])
        y_distance = choice([x for x in range(1, 100)])
        y_step = y_direction * y_distance
        return y_step