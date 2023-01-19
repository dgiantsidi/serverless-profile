import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = (100,50)
plt.rcParams.update({'font.size': 40})

# set width of bar
barWidth = 0.4
fig = plt.subplots(figsize =(12, 8))

# set height of bar
read = [0.2,      0.3,    0.3,    0.3,    0.4]
append = [0.3,	0.3,	0.8,	0.8,	0.8]

# Set position of bar on X axis
br1 = np.arange(len(read))
br2 = [x + barWidth for x in br1]

# Make the plot
plt.bar(br1, read, color ='black', width = barWidth,
        edgecolor ='black', label ='Reads')
plt.bar(br2, append, color ='white', width = barWidth, hatch = '/',
        edgecolor ='black', label ='Appends')

# Adding Xticks
plt.xlabel('Replication factor')
plt.ylabel('Latency (ms)')
plt.xticks([r + barWidth/2 for r in range(len(read))],
        ['2', '3', '4', '6', '8'])

plt.legend(ncol = 1, loc='center', bbox_to_anchor=(0.25, 0.8))

plt.savefig("replication_factor.pdf", bbox_inches='tight', dpi = 200)
