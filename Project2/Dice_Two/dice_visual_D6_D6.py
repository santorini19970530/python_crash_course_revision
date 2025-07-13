# Python Crash Course, 2Ed, writtern by Eric Matthes

from die import Die
from plotly import offline
from plotly.graph_objs import Bar, Layout

# Create two D6s.
die1 = Die()
die2 = Die()

# Make some rolls, and store results in a list.
results = [die1.roll()+die2.roll() for result in range(1000)]

# Analyse the results
max_result = die1.num_sides + die2.num_sides
frequencies = [results.count(frequency) for frequency in range(2, max_result+1)]

# Visualize the results
x_value = list(range(2, max_result+1))
data = [Bar(x=x_value, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick' : 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling two D6 dice 1000 times', xaxis = x_axis_config, yaxis = y_axis_config)
offline.plot({'data': data, 'layout' : my_layout}, filename = 'd6_d6.html')
