import matplotlib.pyplot as pt

labels = ('Python', 'Scala', 'C#', 'Java', 'PHP')
index = (1, 2, 3, 4, 5)
web_usage = [20, 2, 5, 10, 14]
data_science_usage = [15, 8, 5, 15, 2]
games_usage = [10, 1, 5, 5, 4]

pt.bar(index,web_usage,tick_label=labels,
       color='green',width=0.5,label='web')
pt.bar(index,data_science_usage,tick_label=labels,
       color='blue',width=0.5,bottom=web_usage,label="data science")

web_and_games_usage= list(web_usage[i]+data_science_usage[i]\
                          for i in range(0, len(web_usage)))
pt.bar(index, games_usage, tick_label=labels,
       label='games',width = 0.5, bottom=web_and_games_usage)

pt.ylabel('Percentage use')
pt.xlabel("Programming languages")
pt.title("Programming languages by use")
pt.legend()

pt.show()