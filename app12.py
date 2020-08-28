import matplotlib.pyplot as pt
import csv

x = []
y = []

with open("example.txt",'r') as csvfile:
    plots=csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))

pt.plot(x,y,label="loaded from file")
pt.legend()
pt.xlabel("X")
pt.ylabel("Y")
pt.title("Y against X")

pt.show()