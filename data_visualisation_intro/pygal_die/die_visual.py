import pygal
from pygal_die.die import Die


# Create two a 6 Sided die.
die1 = Die(8)
die2 = Die(8)

# Make some rolls and store the results in a list.

results = []
for roll_num in range(10000):
    result = die1.roll() + die2.roll()
    results.append(result)

# Analyze results
max_results = die1.num_sides + die2.num_sides
frequencies = []
for value in range(2, max_results + 1):  # Added +1 because range
    frequency = results.count(value)  # Counts how many times num.sides appears in results from above
    frequencies.append(frequency)

# Visualize the results.

hist = pygal.Bar()
max_outcome = list([die1.num_sides + die2.num_sides])
neat = []
for x in range(2, max_results + 1):
    formatted_x = f"{x}"
    neat.append(formatted_x)
print(neat)
hist.title = (f'Results of rolling {die1.num_sides} sided die and a {die2.num_sides} die {len(results)} times')
hist.x_labels = neat
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('D6 + D6', frequencies)
hist.render_to_file('die_visual.svg')

