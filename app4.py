import matplotlib.pyplot as pt

labels = ('Python', 'Java', 'Scala', 'C#')
sizes = [45, 30, 15, 10]
explode = (0.1, 0.0, 0.0, 0.0)
pt.pie(sizes,
       labels=labels,
       explode=explode,
       shadow= True,
       autopct='%1.f%%',
       counterclock=False,
       startangle=90)

pt.show()