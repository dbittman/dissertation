import sys
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import os
import pylab

matplotlib.use("pgf")
#matplotlib.rc('font',**{'family':'sans-serif','sans-serif':['Source Sans Pro']})
#matplotlib.rcParams['pdf.fonttype'] = 42
#matplotlib.rcParams['font.family'] = "sans-serif"

pylab.figure(num=None, figsize=(4, 2.7), facecolor='w', edgecolor='k')
#matplotlib.rcParams.update({'font.size': 10})

list_of_files = [
    ('data/cachesz/out-sim-xrbt2-bf-xrbt2-seq', 'No L2'),
    ('data/cachesz/out-sim-xrbt2-bf-xrbt2-seq-l2-1m', '1MB L2'),
    ('data/cachesz/out-sim-xrbt2-bf-xrbt2-seq-l2', '2MB L2'),
    ('data/cachesz/out-sim-xrbt2-bf-xrbt2-seq-l2-4m', '4MB L2'),
]

markers = ['+', 'x', '1', '2']
datalist = [(pylab.loadtxt(filename, usecols=(0, 3)), label)
            for filename, label in list_of_files]

for data, label in datalist:
    pylab.plot(data[:, 0], data[:, 1], markers[0], label=label)
    markers = markers[1:]

pylab.legend()
#pylab.title("Title of Plot")
pylab.xlabel("Number of insert operations")
pylab.ylabel("Number of bits flipped")
plt.ticklabel_format(style='sci', axis='x', scilimits=(0, 0))
plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
pylab.tight_layout()


output = sys.argv[1]
pylab.savefig(output)
