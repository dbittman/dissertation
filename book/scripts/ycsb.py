import sys
import pylab
import os
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.use("pgf")

pylab.figure(num=None, figsize=(4, 2.5), facecolor='w', edgecolor='k')

names = ('A', 'B', 'C', 'D', 'E', 'F')
#twz_ruc = (45.1, 57.9, 61.2, 56.4, 3, 33.65)
#native_ruc = (18.4, 22.5, 23.3, 22, 1.9, 13.3)
#mdb_ruc = (33.4, 33.9, 34.2, 32.5, 2.6, 22.52)

#native_err = (.1, .1, .1, .1, .01, .1)
#native_ruc = (17.3, 22.2, 23.1, 21.7, 1.9, 12.7)
#mdb_err = (.3, .1, .1, .1, .01, .1)
#mdb_ruc = (33, 33.98, 34.3, 32.5, 2.57, 22.25)

#twz_err = (.2, .2, .15, .15, .01, .13)
#twz_ruc = (45.6, 59.49, 63.12, 57.45, 3.05, 33.78)

# normal, latency-performance (no turbo), DAX enabled
#mdb = [16.96, 21.5, 22.3, 20.26, 1.77, 12.37]
#mdb_err = [.04, .02, .014, .02, .003, .026]
mdb = [23.58, 33.4, 35.3, 31.1, 2.26, 18]
mdb_err = [.1, .1, .2, .1, .01, .1]

# normal, latency-performance (no turbo), DAX enabled
native = [15.6, 28.7, 32.5, 26.5, 2.16, 11.86]
native_err = [1, .2, .1, .75, .004, .12]

pmdk = [21.2, 28.9, 30.4, 21.2, 1.79, 16.03]
pmdk_err = [.2, .1, .1, .13, .003, .1]

twz = [45.1, 42.8, 42.7, 39.5, 2.58, 30.21]
twz_err = [0.1, 0.1, 0.1, 0.1, 0.001, .1]


xs = np.arange(6)

norm = mdb

native = [x / n for (x, n) in zip(native, norm)]
mdb = [x / n for (x, n) in zip(mdb, norm)]
twz = [x / n for (x, n) in zip(twz, norm)]
pmdk = [x / n for (x, n) in zip(pmdk, norm)]

native_err = [x*2 / n for (x, n) in zip(native_err, norm)]
mdb_err = [x*2 / n for (x, n) in zip(mdb_err, norm)]
twz_err = [x*2 / n for (x, n) in zip(twz_err, norm)]
pmdk_err = [x*2 / n for (x, n) in zip(pmdk_err, norm)]

w = 0.2
pb_native = plt.bar(xs, native, width=w, yerr=native_err)
pb_mdb = plt.bar(xs+w, mdb, width=w, yerr=mdb_err)
pb_pmdk = plt.bar(xs+w*2, pmdk, width=w, yerr=pmdk_err)
pb_twz = plt.bar(xs+w*3, twz, width=w, yerr=twz_err)
plt.xticks(xs+w*1.5, names)
plt.ylabel('Transaction Rate (normalized)')
plt.ylim(0, 2.2)
plt.xlabel('YCSB Workload Specification')

plt.legend([pb_native, pb_mdb, pb_pmdk, pb_twz], ['SQL-Native', 'SQL-LMDB', 'SQL-PMDK',
                                                  'SQL-Twizzler'],
           ncol=2, handletextpad=0.1, handlelength=.4, borderpad=.2)
# plt.legend([pb_native, pb_mdb, pb_twz], ['SQL-Native', 'SQL-LMDB', 'SQL-NVOS'],
#       ncol=3,handletextpad=0.1)
plt.tight_layout()

#ax = plt.gca()
#plt.legend(bbox_to_anchor=(0.75, .5), bbox_transform=ax.transAxes)


output = sys.argv[1]
pylab.savefig(output)
