# Python Crash Course, 2Ed, writtern by Eric Matthes

import matplotlib.pyplot as plt

# generate data
x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

# build up a plotting platform
plt.style.use('seaborn')
fig, ax = plt.subplots()

# stryling individual plot
ax.scatter(x_values, y_values, c = y_values, cmap = plt.cm.Blues, s=10)

# set the line width
#ax.plot(x_values, y_values, linewidth = 3)

# set chart title and axes
ax.set_title("Cubic Numbers", fontsize = 24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Cubic of Value", fontsize = 14)

# set the range for each axis
ax.axis([0, 5050, 0, max(y_values)*1.1])

# set size of tick labels
ax.tick_params(axis='both', labelsize = 14)

# show the plot
plt.show()

# save the plot into pic file
#plt.savefig("squares_plot.png", format="png", bbox_inches='tight')
