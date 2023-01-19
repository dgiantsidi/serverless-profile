from os import read
import matplotlib.pyplot as plt
import sys
import csv
import seaborn as sns
plt.rcParams['hatch.linewidth'] = 2.5
palette = sns.color_palette("pastel")




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

ax[0].plot(pmlog, marker='s', linestyle='--', linewidth=4, color='k', markerfacecolor=palette[2], label='PMLog', markersize=marker_ft,  markeredgecolor='black', markeredgewidth=4)
ax[0].set_ylabel("KOps/sec", fontsize=ft)
#ax[0].set_ylabel("Throughtput (KOps/sec)", fontsize=ft)
ax[0].set_xlabel("Reads (%)", fontsize=ft)
plt.sca(ax[0])
ax1 = plt.gca()
ax1.tick_params(axis="y", labelsize=ft)
#plt.yscale("log")
plt.xticks(list(range(0, 3)))
ax1.set_xticklabels(record_sizes, fontsize=ft)


ax[1].plot(pmlog_lat_append, marker='o', linestyle='--', linewidth=4, color='k', markerfacecolor= palette[5], label='Append', markersize=marker_ft,  markeredgecolor='black', markeredgewidth=4)
ax[1].plot(pmlog_lat_read, marker='>', linestyle='--', linewidth=4, color='k', markerfacecolor=palette[0], label='Read', markersize=marker_ft,  markeredgecolor='black', markeredgewidth=4)
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
plt.savefig("colored_plots/pmlog_3shards_colorful.pdf", bbox_inches='tight', dpi = 200)

#plt.show()
