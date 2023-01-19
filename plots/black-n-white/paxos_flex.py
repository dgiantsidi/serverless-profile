import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = (100,50)
plt.rcParams.update({'font.size': 40})

# set width of bar
barWidth = 0.05
fig = plt.subplots(figsize =(12, 8))

# set height of bar
flexlog = [270.000]
flexlog_relaxed = [300.000]
paxos = [109.572]

# Set position of bar on X axis
br1 = np.arange(len(flexlog))
br2 = [x + barWidth+0.1 for x in br1]
br3 = [x + barWidth+0.1 for x in br2]

# Make the plot
plt.bar(br1, flexlog, color ='gray', width = barWidth,
        edgecolor ='black', label ='FlexLog')
plt.bar(br2, flexlog_relaxed, color ='white', width = barWidth, hatch = '/',
        edgecolor ='black', label ='FlexLog (partial ord.)')
plt.bar(br3, paxos, color ='black', width = barWidth, hatch = '/',
        edgecolor ='black', label ='Paxos')

# Adding Xticks
plt.xlabel('FlexLog vs Paxos')
plt.ylabel('KOps/sec')
plt.xticks([r + barWidth/2 for r in range(len(flexlog))],
        ['', '', '', '', ''])

plt.legend(ncol = 2, loc='center', bbox_to_anchor=(0.4, 1.2))

plt.savefig("ordering.pdf", bbox_inches='tight', dpi = 200)
