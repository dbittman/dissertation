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


pylab.figure(num=None, figsize=(4, 2.4), facecolor='w', edgecolor='k')
#matplotlib.rcParams.update({'font.size': 10})

list_of_files = [
    ('data/out-sim-mal-bf-24-l2', '24 bytes'),
    ('data/out-sim-mal-bf-40-l2', '40 bytes'),
    ('data/out-sim-mal-bf-48-l2', '48 bytes')]

datalist = [(pylab.loadtxt(filename, usecols=(0, 3)), label)
            for filename, label in list_of_files]

markers = ['+', 'x', '1']

for data, label in datalist:
    pylab.plot(data[:, 0], data[:, 1], markers[0], label=label)
    markers = markers[1:]

pylab.legend()
#pylab.title("Title of Plot")
pylab.xlabel("Number of calls to malloc()")
pylab.ylabel("Number of bits flipped")
plt.ticklabel_format(style='sci', axis='x', scilimits=(0, 0))
plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
pylab.tight_layout()

output = sys.argv[1]
pylab.savefig(output)
