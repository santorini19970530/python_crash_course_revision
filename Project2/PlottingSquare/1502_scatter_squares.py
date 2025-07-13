# Python Crash Course, 2Ed, writtern by Eric Matthes

import matplotlib.pyplot as plt

# generate data
x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

# build up a plotting platform
plt.style.use('seaborn')
fig, ax = plt.subplots()

# stryling individual plot
# color tone can only be RGB format (decimal), e.g. (32/360,55/360,138/360)
# or use a colormap (a series of colors in a gradient that moves from a starting to an ending color)
ax.scatter(x_values, y_values, c = y_values, cmap = plt.cm.Blues, s=10)

# set the line width
#ax.plot(x_values, y_values, linewidth = 3)

# set chart title and axes
ax.set_title("Square Numbers", fontsize = 24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Square of Value", fontsize = 14)

# set the range for each axis
ax.axis([0, 1100, 0, 1100000])

# set size of tick labels
ax.tick_params(axis='both', labelsize = 14)

# show the plot
#plt.show()

# save the plot into pic file
plt.savefig("squares_plot.png", format="png", bbox_inches='tight')
