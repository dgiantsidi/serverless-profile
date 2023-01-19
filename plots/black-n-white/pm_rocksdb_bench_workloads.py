from os import read
import matplotlib.pyplot as plt
import sys
import csv
plt.rcParams["figure.figsize"] = (25,12)
#plt.rcParams["figure.figsize"] = (5,3)
plt.rcParams.update({'font.size': 40})


rocksdb_sync = [32903, 43691, 65019, 125848, 293750, 585669, 1812116]
#rocksdb = [784779, 1029009, 1470882, 2257547, 2701705, 2740057, 2924731]
pmlog = [720000, 996000, 1424172, 2470572, 3486660, 3508896, 3696720]

fig = plt.figure(figsize = (12, 8))


workloads = ['0', '25', '50', '75', '90', '95', '99']

plt.plot(rocksdb_sync, marker='o', linestyle='--', color='black', label='Boki (RocksDB)', markersize=30)
#plt.plot(rocksdb, marker='*', linestyle='--', color='r', label='rocksdb w/o persistency', markersize=20)
plt.plot(pmlog, marker='s', linestyle='--', color='black', label='FlexLog (PM)', markersize=30)

ax = plt.gca()
plt.yscale("log")
plt.xticks(list(range(0, 7)))
ax.set_xticklabels(workloads)

plt.ylabel("Ops/sec")
#plt.ylabel("Throughput (Ops/sec)")
plt.xlabel("Reads (%)")
plt.tight_layout()
#plt.legend(loc='best')
#plt.legend(ncol = 1, loc='right', bbox_to_anchor=(0.5, 1.15), mode="expand")
#plt.legend(ncol = 3, loc='upper center', bbox_to_anchor=(0.5, 1.4))
plt.savefig("pmlog_rocksdb_bench_workloads.pdf", bbox_inches='tight', dpi = 200)

#plt.show()
