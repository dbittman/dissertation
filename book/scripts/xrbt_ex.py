import sys
import pylab
import os
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.use("pgf")
#matplotlib.rc('font',**{'family':'sans-serif','sans-serif':['Source Sans Pro']})
#matplotlib.rcParams['pdf.fonttype'] = 42
#matplotlib.rcParams['font.family'] = "sans-serif"

pylab.figure(num=None, figsize=(4, 2), facecolor='w', edgecolor='k')
#matplotlib.rcParams.update({'font.size': 10})

list_of_files = [
    ('data/cachesz/out-sim-xrbt2-bf-xrbt2-seq', 'Data structure inserts')
]

datalist = [(pylab.loadtxt(filename, usecols=(0, 3)), label)
            for filename, label in list_of_files]

markers = ['+', 'x', '1', '2']
for data, label in datalist:
    pylab.plot(data[:, 0], data[:, 1], markers[0], label=label)
    markers = markers[1:]

pylab.legend()
#pylab.title("Title of Plot")
pylab.xlabel("Iteration count")
pylab.ylabel("Number of\nbits flipped")
plt.ticklabel_format(style='sci', axis='x', scilimits=(0, 0))
plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
pylab.tight_layout()


output = sys.argv[1]
pylab.savefig(output)
