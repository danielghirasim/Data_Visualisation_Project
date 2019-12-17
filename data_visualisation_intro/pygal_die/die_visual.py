import pygal
from pygal_die.die import Die

# Create a 6 Sided die.
my_die = Die()

# Make some rolls and store the results in a list.

results = []
for roll_num in range(10000):
    result = my_die.roll()
    results.append(result)

# Analyze results
frequencies = []
for value in range(1, my_die.num_sides + 1):  # Added +1 because range
    frequency = results.count(value)  # Counts how many times num.sides appears in results from above
    frequencies.append(frequency)


# Visualize the results.

hist = pygal.Bar()

hist.title = (f'Results of rolling {my_die.num_sides} sided die {len(results)} times')
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')
