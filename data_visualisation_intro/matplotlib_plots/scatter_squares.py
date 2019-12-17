import matplotlib.pyplot as plt
from random import randint

x_values = list(range(1, 1001))
y_values = [x * x for x in x_values]

# Here we are using the scatter type chart
# We add X,Y values , color for y_values , colormap and size

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolors='none', s=10)

# Set chart title and labels axes

plt.xlabel("Square numbers", fontsize=24)
plt.ylabel("Value", fontsize=24)
plt.title("Square of Value", fontsize=24)

# Set size of ticklabels
plt.tick_params(axis='both', which='major', labelsize=14)

# Set the range for each axis
plt.axis([0, 1100, 0, 1100000])
plt.savefig('squares_plot.png', bbox_inches='tight')  # must be before plt.show
plt.show()
