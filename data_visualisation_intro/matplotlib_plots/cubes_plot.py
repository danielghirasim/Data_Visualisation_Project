import matplotlib.pyplot as plt

x_values = range(1,55)
y_values = [x*x*x for x in x_values]

plt.scatter(x_values,y_values,c=y_values, cmap = plt.cm.Blues, edgecolors = 'none', s=20)

plt.xlabel("X Value")
plt.ylabel("X Cubed")
plt.title("Cubes_Plot")

plt.axis([0, x_values[-1], 0, y_values[-1]])


plt.show()