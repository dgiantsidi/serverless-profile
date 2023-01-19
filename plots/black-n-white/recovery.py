import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = (100, 50)
plt.rcParams.update({'font.size': 40})


# creating the dataset
data = {'100':0.2, '1K':2, '5K':13,
        '10K':45, '100K':297, '1e6':4300, "3e6":24000}

courses = list(data.keys())
values = list(data.values())

fig = plt.figure(figsize = (12, 8))

# creating the bar plot
plt.bar(courses, values, color ='gray', edgecolor = 'black',
        width = 0.4, label="Write latency")


plt.yscale("log")

plt.xlabel("records to recover")
plt.ylabel("Recovery time (ms)")
#plt.title("")
plt.savefig("recovery.pdf", bbox_inches='tight', dpi = 500)

