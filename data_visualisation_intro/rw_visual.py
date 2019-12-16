import matplotlib.pyplot as plt
from random_walk import RandomWalk

my_walk = RandomWalk()
my_walk.walk()

plt.figure(figsize=(12,8))

plt.scatter(my_walk.x_value,my_walk.y_value,c=my_walk.y_value,s=1)
plt.title("Random Walk")
plt.show()