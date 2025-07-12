import matplotlib.pyplot as plt

from random_walk import Randomwalk

# Keep making new walks, as long as the program is active.

while True:

    # Make a random walk

    rw = Randomwalk(50_000)
    rw.fill_walk()

    # Plot the points in the walk

    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(16,9))
    point_numbers = range(rw.num_points)
    ax.plot(rw.x_values, rw.y_values, linewidth = 1)

    # Emphasize the first and the last points
    
    ax.scatter(0,0, c='green', s=100, edgecolors='none', zorder=2)
    ax.scatter(rw.x_values[-1],rw.y_values[-1], c='red', s=100, edgecolors='none',zorder=2)

    # Remove the axes

    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y / n) >> ").lower()
    if keep_running == 'n':
        break
