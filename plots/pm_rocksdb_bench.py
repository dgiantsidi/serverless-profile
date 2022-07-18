from os import read
import matplotlib.pyplot as plt
import sys
import csv
plt.rcParams["figure.figsize"] = (25,12)
#plt.rcParams["figure.figsize"] = (5,3)
plt.rcParams.update({'font.size': 55})


rocksdb_sync = [64857, 64759, 64653, 64662, 64904, 64606, 64622, 64824]
rocksdb = [1491401, 1463455, 1482468, 1473461, 1478599, 1465882, 1464387, 1475854]
pmlog = [1414016, 1413729, 1422686, 1419716, 1462096, 1409430, 1427061, 1436916]


record_sizes = ['64', '128', '256', '512', '1024', '2048', '4096', '8192']

plt.plot(rocksdb_sync, marker='o', linestyle='--', color='b', label='rocksdb', markersize=20)
plt.plot(rocksdb, marker='*', linestyle='--', color='r', label='rocksdb w/o persistency', markersize=20)
plt.plot(pmlog, marker='s', linestyle='--', color='green', label='PMLog', markersize=20)

ax = plt.gca()
plt.yscale("log")
plt.xticks(list(range(0, 8)))
ax.set_xticklabels(record_sizes)

plt.ylabel("Throughput (Ops/sec)")
plt.xlabel("record sz (B)")
plt.tight_layout()
#plt.legend(loc='best')
#plt.legend(ncol = 1, loc='right', bbox_to_anchor=(0.5, 1.15), mode="expand")
plt.legend(ncol = 3, loc='upper center', bbox_to_anchor=(0.5, 1.4))
plt.savefig("pmlog_rocksdb_bench.pdf", bbox_inches='tight', dpi = 200)

#plt.show()
