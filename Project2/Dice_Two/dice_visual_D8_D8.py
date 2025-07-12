from die import Die
from plotly import offline
from plotly.graph_objs import Bar, Layout

# Create two D6s.
die1 = Die(8)
die2 = Die(8)

# Make some rolls, and store results in a list.
results = []
for roll_num in range(1000):
    result = die1.roll() + die2.roll()
    results.append(result)

# Analyse the results
frequencies = []
max_result = die1.num_sides + die2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results
x_value = list(range(2, max_result+1))
data = [Bar(x=x_value, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick' : 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling two D8 dice 1000 times', xaxis = x_axis_config, yaxis = y_axis_config)
offline.plot({'data': data, 'layout' : my_layout}, filename = 'd8_d8.html')
