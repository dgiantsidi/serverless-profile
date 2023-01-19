from os import read
import matplotlib.pyplot as plt
import sys
import csv
import numpy as np


plt.rcParams["figure.figsize"] = (24, 12)
figure, ax = plt.subplots(1, 2, gridspec_kw={'width_ratios': [1, 1]})
plt.subplots_adjust(wspace=0.35)
#plt.rcParams["figure.figsize"] = (5,3)
ft=60
plt.rcParams.update({'font.size': ft})
marker_ft=45
barWidth = 0.025

flexilog = [232, 210, 136]
boki = [1105, 800, 600]



workloads = ['10', '15', '50']

ax[0].plot(boki, marker='o', linestyle='--', color='black', label='Boki', markersize=marker_ft)
ax[0].plot(flexilog, marker='s', linestyle='--', color='black', label='FlexLog', markersize=marker_ft)
ax[0].set_ylabel("Latency (usec)", fontsize=ft)
#ax[0].set_ylabel("Throughtput (KOps/sec)", fontsize=ft)
ax[0].set_xlabel("Reads (%)", fontsize=ft)
plt.sca(ax[0])
ax1 = plt.gca()
ax1.tick_params(axis="y", labelsize=ft)
#plt.yscale("log")
plt.xticks(list(range(0, 3)))
ax1.set_xticklabels(workloads, fontsize=ft)
plt.legend(ncol = 1, loc='center left', bbox_to_anchor=(-0.04, 0.36), frameon=True)
plt.rcParams["figure.figsize"] = (5,3)

# set height of bar
flexlog = [270.000]
flexlog_relaxed = [300.000]
paxos = [109.572]

# Set position of bar on X axis
br1 = np.arange(len(flexlog))
br2 = [x + barWidth+0.01 for x in br1]
br3 = [x + barWidth+0.01 for x in br2]

# Make the plot
ax[1].bar(br1, flexlog, color ='gray', width = barWidth, edgecolor ='black', label ='FlexLog')
ax[1].bar(br2, flexlog_relaxed, color ='white', width = barWidth, hatch = '/', edgecolor ='black', label ='FlexLog-P')
ax[1].bar(br3, paxos, color ='black', width = barWidth, hatch = '/', edgecolor ='black', label ='Paxos')

 # Adding Xticks
#ax[1].xlabel('FlexLog vs Paxos')
#ax[1].ylabel('KOps/sec')
#ax[1].xticks([r + barWidth/2 for r in range(len(flexlog))], ['', '', '', '', ''])
ax[1].set_ylabel("kOps/sec", fontsize=ft)



plt.sca(ax[1])
ax1 = plt.gca()
ax1.tick_params(axis="y", labelsize=ft)
plt.xticks(list(range(0, 1)))
#ax1.set_xticklabels(record_sizes, fontsize=ft)

plt.legend(ncol = 1, loc='upper left', bbox_to_anchor=(1, 1))
plt.savefig("ordering.pdf", bbox_inches='tight', dpi = 200)

#plt.show()
