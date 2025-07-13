# Python Crash Course, 2Ed, writtern by Eric Matthes

import matplotlib.pyplot as plt

# generate data
squares = []
input_values = []
for i in range(1,11):
    input_values.append(i)
    squares.append(i*i)

# build up a plotting platform
plt.style.use('seaborn')
fig, ax = plt.subplots()

# set the line width
ax.plot(input_values, squares, linewidth = 3)

# set chart title and axes
ax.set_title("Square Numbers", fontsize = 24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Square of Value", fontsize = 14)

# set size of tick labels
ax.tick_params(axis='both', labelsize = 14)

# show the plot
plt.show()
