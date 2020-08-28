import matplotlib.pyplot as pt

labels = ('Python', 'Scala', 'C#', 'Java', 'PHP')
index = (1, 2, 3, 4, 5)  # provides locations on x axis
sizes = [45, 10, 15, 30, 22]

pt.bar(index, sizes,width=0.5, tick_label=labels,
       color=("red", 'orange', 'yellow', 'cyan', "magenta"))
pt.ylabel("Percentage use",fontsize=12)
pt.xlabel("Programming language",fontsize=10)
pt.title("Programming languages used in an organization")

pt.show()
