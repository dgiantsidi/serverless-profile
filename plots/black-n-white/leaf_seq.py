import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = (100, 50)
plt.rcParams.update({'font.size': 40})


# creating the dataset
data = {'1':1.2, '2':2.1, '4':3.99,
        '6':5.8}

courses = list(data.keys())
values = list(data.values())

fig = plt.figure(figsize = (12, 8))

# creating the bar plot
plt.bar(courses, values, color ='white', edgecolor ='black', hatch='-',
        width = 0.2)

plt.yticks(np.arange(0, 6.5, 1.5))
plt.xlabel("number of leaf-sequencers")
plt.ylabel("MReqs/sec")
#plt.title("")
plt.savefig("sequencers.pdf", bbox_inches='tight', dpi = 500)

