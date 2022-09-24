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

pylab.figure(num=None, figsize=(4, 2.7), facecolor='w', edgecolor='k')
#matplotlib.rcParams.update({'font.size': 10})

list_of_files = [
    ('data/instr/out-sim-xorll-bf-x-clwb', 'xlist, sim.', (0, 3)),
    ('data/instr/out-sim-xorll-bf-d-clwb', 'dlist, sim.', (0, 3)),
    ('data/instr/out-xorll-x-clwb', 'xlist, instr.', (2, 3)),
    ('data/instr/out-xorll-d-clwb', 'dlist, instr.', (2, 3)),
]

markers = ['+', 'x', '1', '2']
datalist = [(pylab.loadtxt(filename, usecols=cols), label) for filename,
            label, cols in list_of_files]

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
