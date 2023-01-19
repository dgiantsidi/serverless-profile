from os import read
import matplotlib.pyplot as plt
import sys
import csv
plt.rcParams["figure.figsize"] = (25,12)
#plt.rcParams["figure.figsize"] = (5,3)
plt.rcParams.update({'font.size': 60})


flexilog = [232, 210, 136]
boki = [1105, 800, 600]


workloads = ['10', '15', '50']

plt.plot(boki, marker='o', linestyle='--', color='b', label='Boki (Paxos)', markersize=30)
plt.plot(flexilog, marker='s', linestyle='--', color='green', label='FlexLog (ordering)', markersize=30)

ax = plt.gca()
#plt.yscale("log")
plt.xticks(list(range(0, 3)))
ax.set_xticklabels(workloads)

plt.ylabel("Latency (usec)")
plt.xlabel("Reads (%)")
plt.tight_layout()
#plt.legend(loc='best')
#plt.legend(ncol = 1, loc='right', bbox_to_anchor=(0.5, 1.15), mode="expand")
plt.legend(ncol = 2, loc='upper center', bbox_to_anchor=(0.5, 1.4))
plt.savefig("ordering_bench_workloads.pdf", bbox_inches='tight', dpi = 200)

#plt.show()
