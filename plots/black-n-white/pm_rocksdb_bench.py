from os import read
import matplotlib.pyplot as plt
import sys
import csv
plt.rcParams["figure.figsize"] = (25,12)
#plt.rcParams["figure.figsize"] = (5,3)
plt.rcParams.update({'font.size': 40})


#rocksdb_sync = [64857, 64759, 64653, 64662, 64904, 64606, 64622, 64824]
#rocksdb = [1491401, 1463455, 1482468, 1473461, 1478599, 1465882, 1464387, 1475854]
#pmlog = [1414016, 1413729, 1422686, 1419716, 1462096, 1409430, 1427061, 1436916]
rocksdb_sync = [64857, 64759, 64662, 64904, 64606, 64622, 64824]
pmlog = [1414016, 1413729, 1419716, 1462096, 1409430, 1427061, 1436916]

fig = plt.figure(figsize = (12, 8))

record_sizes = ['64', '128', '512', '1K', '2K', '4K', '8K']

plt.plot(rocksdb_sync, marker='o', linestyle='--', color='black', label='Boki (RocksDB)', markersize=30)
#plt.plot(rocksdb, marker='*', linestyle='--', color='r', label='rocksdb w/o persistency', markersize=20)
plt.plot(pmlog, marker='s', linestyle='--', color='black', label='FlexLog (PM)', markersize=30)

ax = plt.gca()
plt.yscale("log")
plt.xticks(list(range(0, len(record_sizes))))
ax.set_xticklabels(record_sizes)

#plt.ylabel("Throughput (Ops/sec)")
plt.ylabel("Ops/sec")
plt.xlabel("record sz (B)")
plt.tight_layout()
#plt.legend(loc='best')
#plt.legend(ncol = 1, loc='right', bbox_to_anchor=(0.5, 1.15), mode="expand")
plt.legend(ncol = 1, loc='upper center', bbox_to_anchor=(0.5, 0.8))
plt.savefig("pmlog_rocksdb_bench.pdf", bbox_inches='tight', dpi = 500)

#plt.show()
