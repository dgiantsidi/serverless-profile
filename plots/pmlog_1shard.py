from os import read
import matplotlib.pyplot as plt
import sys
import csv


plt.rcParams["figure.figsize"] = (24, 12)
figure, ax = plt.subplots(1, 2)
#plt.rcParams["figure.figsize"] = (5,3)
ft=60
plt.rcParams.update({'font.size': ft})
marker_ft=45

pmlog = [69.530, 122.340, 357.929]
pmlog_lat_append = [3, 2.7, 1.6]
pmlog_lat_read = [0.4, 0.53, 0.5]


record_sizes = ['5', '50', '95']

ax[0].plot(pmlog, marker='s', linestyle='--', color='black', label='PMLog', markersize=marker_ft)
ax[0].set_ylabel("KOps/sec", fontsize=ft)
#ax[0].set_ylabel("Throughtput (KOps/sec)", fontsize=ft)
ax[0].set_xlabel("Reads (%)", fontsize=ft)
plt.sca(ax[0])
ax1 = plt.gca()
ax1.tick_params(axis="y", labelsize=ft)
#plt.yscale("log")
plt.xticks(list(range(0, 3)))
ax1.set_xticklabels(record_sizes, fontsize=ft)


ax[1].plot(pmlog_lat_append, marker='o', linestyle='--', color='black', label='Append', markersize=marker_ft)
ax[1].plot(pmlog_lat_read, marker='>', linestyle='--', color='black', label='Read', markersize=marker_ft)
ax[1].set_ylabel("Latency (ms)", fontsize=ft)
ax[1].set_xlabel("Reads (%)", fontsize=ft)
plt.sca(ax[1])
ax1 = plt.gca()
ax1.tick_params(axis="y", labelsize=ft)
#plt.yscale("log")
plt.xticks(list(range(0, 3)))
ax1.set_xticklabels(record_sizes, fontsize=ft)

plt.legend(ncol = 1, loc='center left', bbox_to_anchor=(-0.04, 0.5))
#plt.legend(ncol = 1, loc='center left', bbox_to_anchor=(-0.2, 1.2))
plt.savefig("pmlog_3shards.pdf", bbox_inches='tight', dpi = 200)

#plt.show()
