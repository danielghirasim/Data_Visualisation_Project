import matplotlib.pyplot as plt
from random_walk.random_walk import RandomWalk


# Keep making new walks, as long as the program is active.

def make_walk():
    while True:
        my_walk = RandomWalk(30000)
        my_walk.walk()

        # Make a list of our number_points from class
        point_numbers =list(range(my_walk.number_points))
        # Make the figure 12 by 8 inches or cm idfk
        plt.figure(dpi = 128, figsize=(10, 6))
        # c = the thing we color, cmap = Color map
        plt.plot(my_walk.x_value, my_walk.y_value)
        plt.title("Random Walk")
        # Remove the axes.
        plt.axes().get_xaxis().set_visible(False)
        plt.axes().get_yaxis().set_visible(False)

        plt.show()

make_walk()