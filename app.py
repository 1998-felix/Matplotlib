from matplotlib import pyplot

y_data = [0, 2, 6, 14, 30, 43, 75]
x_data = [0, 1, 2, 3, 4, 5, 6]

pyplot.ylabel("Speed", fontsize=12)
pyplot.xlabel("Time", fontsize=12)

pyplot.title("Speed v Time")

pyplot.plot(x_data, y_data, 'bx-')
pyplot.show()
