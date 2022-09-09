from os import read
import matplotlib.pyplot as plt
import sys
import csv


plt.rcParams["figure.figsize"] = (30,12)
figure, ax = plt.subplots(1, 2)
#plt.rcParams["figure.figsize"] = (5,3)
ft=40
plt.rcParams.update({'font.size': ft})


pmlog = [69530, 122340, 357929]
pmlog_lat_append = [1.6, 2.7, 3]
pmlog_lat_read = [0.5, 0.53, 0.4]


record_sizes = ['5%', '50%', '95%']

ax[0].plot(pmlog, marker='s', linestyle='--', color='green', label='PMLog', markersize=ft)
ax[0].set_ylabel("Throughtput (Ops/sec)", fontsize=ft)
ax[0].set_xlabel("Write ratio", fontsize=ft)
plt.sca(ax[0])
ax1 = plt.gca()
ax1.tick_params(axis="y", labelsize=ft)
#plt.yscale("log")
plt.xticks(list(range(0, 3)))
ax1.set_xticklabels(record_sizes, fontsize=ft)


ax[1].plot(pmlog_lat_append, marker='s', linestyle='--', color='blue', label='Append latency', markersize=ft)
ax[1].plot(pmlog_lat_read, marker='s', linestyle='--', color='red', label='Read latency', markersize=ft)
ax[1].set_ylabel("Latency (ms)", fontsize=ft)
ax[1].set_xlabel("Write ratio", fontsize=ft)
plt.sca(ax[1])
ax1 = plt.gca()
ax1.tick_params(axis="y", labelsize=ft)
#plt.yscale("log")
plt.xticks(list(range(0, 3)))
ax1.set_xticklabels(record_sizes, fontsize=ft)

plt.legend(ncol = 1, loc='upper left')
plt.savefig("pmlog_3shards.pdf", bbox_inches='tight', dpi = 200)

plt.show()
