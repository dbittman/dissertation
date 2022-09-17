import sys
import pylab
import os
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.use("pgf")

pylab.figure(num=None, figsize=(4, 2), facecolor='w', edgecolor='k')

twz = [761.6, 526.4, 792.6, 583.5]
twz_err = [2.8, .9, 2.6, 0.9]

linux = [725, 515.2, 781.93, 601.5]
linux_err = [1.34, .7, 1, 1.13]

linux_err = [x*2 for x in linux_err]
twz_err = [x*2 for x in twz_err]

names = ['Insert', 'Lookup', 'Insert (m)', 'Lookup (m)']

xs = np.arange(4)

#norm = mdb

#native = [x / n for (x, n) in zip(native, norm)]
#mdb = [x / n for (x, n) in zip(mdb, norm)]
#twz = [x / n for (x, n) in zip(twz, norm)]

#native_err = [x*2 / n for (x, n) in zip(native_err, norm)]
#mdb_err = [x*2 / n for (x, n) in zip(mdb_err, norm)]
#twz_err = [x*2 / n for (x, n) in zip(twz_err, norm)]

w = 0.2
#pb_native = plt.bar(xs, native, width=w, yerr=native_err)
pb_linux = plt.bar(xs, linux, width=w, yerr=linux_err)
pb_twz = plt.bar(xs+w, twz, width=w, yerr=twz_err)
plt.xticks(xs+w/2, names)
plt.ylabel('Nanoseconds')
plt.yticks(np.arange(0, 1000+1, 250))
#plt.ylim(0, 2.2)
#plt.xlabel('YCSB Workload Specification')

ax = plt.gca()
#plt.legend(bbox_to_anchor=(0.75, .5), bbox_transform=ax.transAxes)
plt.legend([pb_linux, pb_twz], ['unixkv', 'twzkv'])
# , bbox_to_anchor=(0.52, .7),
#           bbox_transform=ax.transAxes,
#           ncol=1, handletextpad=0.1, handlelength=.4, borderpad=.2)
# plt.legend([pb_native, pb_mdb, pb_twz], ['SQL-Native', 'SQL-LMDB', 'SQL-NVOS'],
#       ncol=3,handletextpad=0.1)
plt.tight_layout()


output = sys.argv[1]
pylab.savefig(output)
