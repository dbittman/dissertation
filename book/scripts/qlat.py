import sys
import pylab
import os
import matplotlib.pyplot as plt
import numpy as np
import matplotlib

matplotlib.use("Agg")
pylab.figure(num=None, figsize=(4, 2.5), facecolor='w', edgecolor='k')


names = ['Sort', 'Mean', 'Median', 'Index', 'Find', 'Probe']

#twz_ruc =    (.042, 99.23, 2050.5, 1940.1, 156.2, 2258.9, .15)
#native_ruc = (27.7, 206.5, 4466.9, 3825.5, 307.6, 3105.3, .06)
#mdb_ruc =    (.043, 189.2, 2217.8, 3608.3, 287.8, 2866.7, .07)

#twz_err = (.001, .2,    45.3, 1.6, .2, 4.4, .01)
#native_err = (.07, .15, 32.6, 10, .1, .65, .01)
#mdb_err = (.001, .1, 1, 10.7, 1, 3, .01)

#mdb = [0.065670 , 5856.014095 , 314.366819 , 4007.802466 , 4155.913525 , 449.297651 , 0.113003 ]
#mdb_err=[0.001436 , 23.173517 , 0.496720 , 5.201794 , 8.845737 , 0.481272 , 0.0016 ]

# count: .061 += .002
mdb = [4015.430501, 192.012491, 2047, 3022.943726, 333.425700, 0.098701]
mdb_err = [5.510097, 1.498429,  2.4, 5.404812, 0.220377, 0.002094]

#latency-performance, w/ DAX, single-threaded
#native = [15.695760 , 43 , 287.413062 , 6535.560693 , 4598.821371 , 422.156337 , 0.082464 ]
#native_err = [0.096526 , 11.725063 , 0.523766 , 9.788924 , 12.334635 , 1.276220 , 0.00120 ]

# count: 8.74 += .1
native = [4340.612321, 179.220398, 4748.247314,
          3224.966195, 309.237732, 0.067506]
native_err = [9.931174, 0.283012, 7.779372, 3.908915, 0.474357, 0.000604]


# native[0]=0
# native_err[0]=0

# count: .03 += .00082
pmdk = [3610.13, 631.196869, 9749, 8533.4, 742.307330, 0.058303]
pmdk_err = [6.7, 9.860969, 83.6, 140, 10.297450, 0.000708]

# count: .013 += .001
twz = [3196.9, 190.8, 2287.1, 3362.4, 302.22, 0.053]
twz_err = [4.6, 1.3, 7.4, 5.8, 1.2, .0013]
#twz     = [.0156, 2515.714828, 149.350966, 2310.075862, 4082.87, 227.72, .046]
#twz_err = [0.0004, 5.6, 2.6, 1.23, 11.1, 1.14, .0012]


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
plt.xticks(xs+w*1.5, names, rotation=0)
#plt.gcf().subplots_adjust(left=0.15, bottom=0.21)

plt.ylabel('Query Latency (normalized)')
#plt.xlabel('Query Name')
plt.ylim(0, 5)
#plt.text(.15, 1.8, str(round(native[0], 2)))
#plt.text(6.15, 4.65, str(round(native_ruc[6], 2)))
plt.yticks(np.arange(0, 5, 1))
ax = plt.gca()
plt.xlabel('Query Operation')
plt.legend([pb_native, pb_mdb, pb_pmdk, pb_twz], ['SQL-Native', 'SQL-LMDB', 'SQL-PMDK',
                                                  'SQL-Twizzler'],
           ncol=2, handletextpad=0.1, handlelength=.4, borderpad=.2)
plt.tight_layout()

#plt.legend(bbox_to_anchor=(4, 3, 3, 3), bbox_transform=ax.transAxes)


output = sys.argv[1]
pylab.savefig(output)
