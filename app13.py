import matplotlib.pyplot as pt
import numpy as np


x,y = np.loadtxt("example.txt", delimiter=",", unpack=True)

pt.plot(x,y, label="unpacked using np.")

pt.legend()
pt.xlabel("X")
pt.ylabel("Y")
pt.title("Y against X")

pt.show()