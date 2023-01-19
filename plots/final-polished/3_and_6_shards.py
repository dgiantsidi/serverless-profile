from os import read
import numpy as np
import matplotlib.pyplot as plt
import sys
import csv
plt.rcParams["figure.figsize"] = (24,12)
#plt.rcParams["figure.figsize"] = (5,3)
plt.rcParams.update({'font.size': 60})


Three_shards_append_lat = [0.42, 0.42, 0.48, 0.62, 0.80, 1.25]
Three_shards_append_tps = [80, 400, 600, 1080, 1300, 1500]
Three_shards_read_lat = [0.12, 0.15, 0.20, 0.33, 0.52, 1]
Three_shards_read_tps = [72, 400, 600, 1080, 1300, 1500]

Six_shards_append_lat = [0.60, 0.63, 0.70, 0.82, 1.1, 1.50, 1.80]
Six_shards_append_tps = [72, 550, 830, 1400, 1900, 2600, 2900]
Six_shards_read_lat = [0.10, 0.12, 0.15, 0.22, 0.32, 0.54, 0.75]
Six_shards_read_tps = [72, 550, 830, 1400, 1900, 2600, 2900]



plt.plot(Three_shards_append_tps, Three_shards_append_lat, marker='o', linestyle='--', color='navy', label='Append (3 shards)', markersize=30)
plt.plot(Three_shards_read_tps, Three_shards_read_lat, marker='>', linestyle='--', color='navy', label='Read (3 shards)', markersize=30)
plt.plot(Six_shards_read_tps, Six_shards_read_lat, marker='>', linestyle='--', color='green', label='Read (6 shards)', markersize=30)
plt.plot(Six_shards_append_tps, Six_shards_append_lat, marker='o', linestyle='--', color='green', label='Append (6 shards)', markersize=30)
#plt.plot(lat_fileio_read_variable_chunk_sizes, marker='*', linestyle='--', color='maroon', label='fileio_read', markersize=30)
#plt.plot(lat_syscall_log_read_variable_chunk_sizes, marker='s', linestyle='--', color='green', label='read_syscall', markersize=30)
#plt.plot(lat_log_append_threads, marker='X', linestyle='--', color='navy', label='pmem_write', markersize=30)

plt.yticks(np.arange(0, 2, 0.25))


ax = plt.gca()
#plt.yscale("log")
#plt.xticks(list(range(0, 8)))
#ax.set_xticklabels(value_sizes)

plt.ylabel("Latency (ms)")
plt.xlabel("Throughput (KOps/sec)")
plt.tight_layout()
#plt.legend(loc='best')
#plt.legend(ncol = 1, loc='right', bbox_to_anchor=(0.5, 1.15), mode="expand")
plt.legend(ncol = 2, loc='upper center', bbox_to_anchor=(0.5, 1.4))
plt.savefig("append_read.pdf", bbox_inches='tight', dpi = 500)

#plt.show()
