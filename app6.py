import matplotlib.pyplot as pt

labels = ('Python', 'Scala', 'C#', 'Java', 'PHP')
index = (1, 2, 3, 4, 5) # provides locations on x axis
sizes = [45, 10, 15, 30, 22]

pt.barh(index, sizes, tick_label=labels)
pt.ylabel("Programming languages")
pt.xlabel('Percentage use')
pt.title('Percentage use of programming languages')

pt.show()