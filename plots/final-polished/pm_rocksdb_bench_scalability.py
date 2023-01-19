from os import read
import matplotlib.pyplot as plt
import sys
import csv
plt.rcParams["figure.figsize"] = (25,12)
#plt.rcParams["figure.figsize"] = (5,3)
plt.rcParams.update({'font.size': 60})


rocksdb_sync = [10760, 14702, 27224, 38448, 46449, 55487, 65064]
#rocksdb = [387723, 389579, 686046, 914532, 1128106, 1309887, 1479264]
pmlog = [178454, 334535, 611917, 883374, 1088547, 1265343, 1396754]


threads_nb = ['1', '2', '4', '6', '8', '10', '12']

plt.plot(rocksdb_sync, marker='o', linestyle='--', color='b', label='Boki (RocksDB)', markersize=30)
#plt.plot(rocksdb, marker='*', linestyle='--', color='r', label='rocksdb w/o persistency', markersize=20)
plt.plot(pmlog, marker='s', linestyle='--', color='green', label='FlexLog (PM)', markersize=30)

ax = plt.gca()
plt.yscale("log")
plt.xticks(list(range(0, 7)))
ax.set_xticklabels(threads_nb)

plt.ylabel("Throughput (Ops/sec)")
plt.xlabel("number of threads")
plt.tight_layout()
#plt.legend(loc='best')
#plt.legend(ncol = 1, loc='right', bbox_to_anchor=(0.5, 1.15), mode="expand")
plt.legend(ncol = 3, loc='upper center', bbox_to_anchor=(0.5, 1.4))
plt.savefig("pmlog_rocksdb_bench_scalability.pdf", bbox_inches='tight', dpi = 200)

#plt.show()
