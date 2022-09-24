import sys
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import os
matplotlib.use("pgf")

#matplotlib.rc('font',**{'family':'sans-serif','sans-serif':['Source Sans Pro']})
#matplotlib.rcParams['pdf.fonttype'] = 42
#matplotlib.rcParams['font.family'] = "sans-serif"
plt.figure(num=None, figsize=(4, 3), facecolor='w', edgecolor='k')
#matplotlib.rcParams.update({'font.size': 10})

values_xrbt = [23.2, 29.7, 58.5, 188.6]
values_xrbt_big = [21.7, 28.0, 77.6, 193.7]
values_rbt = [41.7, 41.1, 77.7, 193.7]

errors_xrbt = [.2, .4, .1, 3]
errors_xrbt_big = [.2, .4, .1, 2]
errors_rbt = [.3, .5, .1, 2]

fig, ax = plt.subplots(figsize=(4, 2.5))

#index = np.arange(len(values_f))
bar_width = 0.9

#opacity = 0.4
#error_config = {'ecolor': '0.3'}


def do_the_thing(x, v, e):
    if v > 150:
        ax.text(x, v - 65, str(v) + " ± " + str(e), fontsize=10, verticalalignment='bottom', rotation=90,
                horizontalalignment='center', color='white')
    else:
        ax.text(x, v + 2, str(v) + " ± " + str(e), fontsize=10, verticalalignment='bottom', rotation=90,
                horizontalalignment='center')


for x, v, e in zip([1, 5, 10, 14], values_xrbt, errors_xrbt):
    do_the_thing(x, v, e)
for x, v, e in zip([2, 6, 11, 15], values_xrbt_big, errors_xrbt_big):
    do_the_thing(x, v, e)
for x, v, e in zip([3, 7, 12, 16], values_rbt, errors_rbt):
    do_the_thing(x, v, e)


rects1 = ax.bar([1, 5, 10, 14], values_xrbt, bar_width,
                yerr=errors_xrbt,
                # error_kw=error_config,
                label='xrbt')

rects2 = ax.bar([2, 6, 11, 15], values_xrbt_big, bar_width,
                # alpha=opacity,
                # color='r',
                yerr=errors_xrbt_big,
                # error_kw=error_config,
                label='xrbt-big')

rects3 = ax.bar([3, 7, 12, 16], values_rbt, bar_width,
                # alpha=opacity,
                # color='r',
                yerr=errors_rbt,
                # error_kw=error_config,
                label='rbt')


# ax.set_xlabel('')
ax.set_ylabel('Memory events per insert')
#ax.set_title('Scores by group and gender')

xticks = [4, 13]
xticks_minor = [2, 6, 11, 15]
xlbls_m = ['Seq.', 'Rand.', 'Seq.', 'Rand.']
xlbls = ['Bits Flipped', 'Bytes Written']
# xlbls = [ 'background', '5 year statistical summary', 'future build',
#         'maximum day', '90th percentile day', 'average day' ]

ax.set_xticks(xticks)
ax.set_xticks(xticks_minor, minor=True)
ax.set_xticklabels(xlbls)
ax.set_xticklabels(xlbls_m, minor=True)
#ax.tick_params( axis='x', which='minor', direction='out', length=30 )
ax.tick_params(axis='x', which='major', pad=12)

#ax.set_xticks([2, 4, 6, 11, 13, 15])
#ax.set_xticklabels(('Seq.', 'Bits Flipped', 'Rand.', 'Seq.', 'Bytes Written', 'Rand.'))
ax.legend()

fig.tight_layout()


output = sys.argv[1]
plt.savefig(output)
