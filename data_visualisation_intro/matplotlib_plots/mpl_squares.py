import matplotlib.pyplot as plt

squares = [x * x for x in range(1, 6)]
input_values = [1, 2, 3, 4, 5]

plt.plot(input_values, squares, linewidth=5)

# Set chart title and label axes
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of value", fontsize=14)

# Set size of tick labels.
plt.tick_params(axis='both', labelsize=14)

plt.show()

print(input_values)
