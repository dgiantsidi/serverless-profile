import common_utils as c

# creating the dataset
data = {'100':0.2, '1K':2, '5K':13,
        '10K':45, '100K':297, '1e6':4300, "3e6":24000}

courses = list(data.keys())
values = list(data.values())

fig = c.plt.figure(figsize = (12, 8))

# creating the bar plot
c.plt.bar(courses, values, color = c.palette[3], edgecolor = 'black', hatch = '*',
        width = 0.4, label="Write latency")


c.plt.yscale("log")

c.plt.xlabel("records to recover")
c.plt.ylabel("Recovery time (ms)")
#plt.title("")
c.plt.savefig("colored_plots/recovery_colorful.pdf", bbox_inches='tight', dpi = 500)

