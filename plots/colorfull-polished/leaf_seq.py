import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams["figure.figsize"] = (100, 50)
plt.rcParams.update({'font.size': 40})
plt.rcParams['hatch.linewidth'] = 2.5
palette = sns.color_palette("pastel")


# creating the dataset
data = {'1':1.2, '2':2.1, '4':3.99,
        '6':5.8}

courses = list(data.keys())
values = list(data.values())

fig = plt.figure(figsize = (12, 8))

# creating the bar plot
plt.bar(courses, values, color = palette[2], edgecolor ='black', hatch='-', linewidth=2,
        width = 0.2)

plt.yticks(np.arange(0, 6.5, 1.5))
plt.xlabel("number of leaf-sequencers")
plt.ylabel("MReqs/sec")
#plt.title("")
plt.savefig("colored_plots/sequencers_colorful.pdf", bbox_inches='tight', dpi = 500)

