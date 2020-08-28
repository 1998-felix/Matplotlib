import matplotlib.pyplot as pt

teama_results = (60, 75, 56, 62, 58)
teamb_results = (55, 68, 80, 73, 55)

BAR_WIDTH = 0.35

index_a = [1, 2, 3, 4, 5]
index_b = [i+BAR_WIDTH for i in index_a]

ticks = [i+BAR_WIDTH /2 for i in index_a]
tick_labels = ('Lab 1', 'Lab 2', 'Lab 3', 'Lab 4', 'Lab 5')

pt.bar(index_a,teama_results,color="green",width=BAR_WIDTH,
       label ='Team A')
pt.bar(index_b,teamb_results,color="blue",width=BAR_WIDTH,
       label ='Team B')

pt.ylabel("Results")
pt.xlabel('labs')
pt.title("Results v Labs")
pt.legend()
pt.xticks(ticks,tick_labels)
pt.show()
