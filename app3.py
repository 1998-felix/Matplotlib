import numpy as np
import matplotlib.pyplot as pt

x = (5, 5.5, 6, 6.5, 7, 8, 9, 10)
y = (120, 115, 100, 112, 80, 85, 69, 65)

pt.scatter(x=x, y=y, c='cyan', label="Random Plots")

z = np.polyfit(x, y, 1)
p = np.poly1d(z)

pt.plot(x, p(x), 'r,-')
pt.ylabel("y values", fontsize=12)
pt.xlabel('x values', fontsize=12)
pt.title("y against x")
pt.legend()

pt.show()
