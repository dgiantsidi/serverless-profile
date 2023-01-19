from os import read
import matplotlib.pyplot as plt
import sys
import csv
plt.rcParams["figure.figsize"] = (24,12)
#plt.rcParams["figure.figsize"] = (5,3)
plt.rcParams.update({'font.size': 60})


log_append_threads = []
fileio_append_threads = []
syscall_append_threads = []

lat_log_append_threads = [521, 517, 521, 618, 760, 958, 1109, 1280]
lat_fileio_append_threads = [67398, 70640, 68179, 67023, 67526
, 73099, 72839, 79144]
lat_syscall_append_threads = [4035, 4093, 4276, 4484, 4326, 4247, 5184, 5010]

#log_read_variable_chunk_sizes = [2155068.352788, 2121916.03535, 1819599.322446, 1715541.406289, 1663653.645731, 1501938.227251, 739958.214101, 697341.714764]
#fileio_read_variable_chunk_sizes = [12476.069464, 12399.103873, 12390.960738, 12410.154022, 11770.378402, 11785.329196, 9852.603058, 8965.898321]
#syscall_log_read_variable_chunk_sizes = [389730.718717, 389072.721427, 387820.96053, 384858.098336, 378628.507738, 363125.029456, 295212.444144, 282444.564598]

lat_log_read_variable_chunk_sizes = [479, 486, 564, 597, 616, 680, 1366, 1449]
lat_fileio_read_variable_chunk_sizes = [80168, 80665, 80718, 80594, 84974, 84866, 101511, 111548]
lat_syscall_log_read_variable_chunk_sizes = [2580, 2585, 2593, 2613,2656, 2768, 3402, 3555]

value_sizes = ['64', '128', '256', '512', '1024', '2048', '4096', '8192']

plt.plot(lat_log_read_variable_chunk_sizes, marker='o', linestyle='--', color='navy', label='pmem_read', markersize=30)
plt.plot(lat_fileio_read_variable_chunk_sizes, marker='*', linestyle='--', color='maroon', label='fileio_read', markersize=30)
plt.plot(lat_syscall_log_read_variable_chunk_sizes, marker='s', linestyle='--', color='green', label='read_syscall', markersize=30)

plt.plot(lat_log_append_threads, marker='X', linestyle='--', color='navy', label='pmem_write', markersize=30)
plt.plot(lat_fileio_append_threads, marker='^', linestyle='--', color='maroon', label='fileio_write', markersize=30)
plt.plot(lat_syscall_append_threads, marker='>', linestyle='--', color='green', label='write_syscall', markersize=30)

ax = plt.gca()
plt.yscale("log")
plt.xticks(list(range(0, 8)))
ax.set_xticklabels(value_sizes)

plt.ylabel("Latency ($nsec)$")
plt.xlabel("block sz (B)")
plt.tight_layout()
#plt.legend(loc='best')
#plt.legend(ncol = 1, loc='right', bbox_to_anchor=(0.5, 1.15), mode="expand")
plt.legend(ncol = 3, loc='upper center', bbox_to_anchor=(0.5, 1.4))
plt.savefig("storage.pdf", bbox_inches='tight', dpi = 500)

#plt.show()
