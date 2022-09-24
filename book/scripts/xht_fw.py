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

values_slist = [13.4, 36.9 / 1]
#values_elist=[12,  37 / 8]
values_nlist = [11.9, 37 / 1]

errors_slist = [0, 0/8]
#errors_elist=[0, 0/8]
errors_nlist = [0, 0/8]

fig, ax = plt.subplots(figsize=(4, 2.3))

#index = np.arange(len(values_f))
bar_width = 0.9

#opacity = 0.4
#error_config = {'ecolor': '0.3'}

rects1 = ax.bar([1, 4], values_slist, bar_width,
                yerr=errors_slist,
                # error_kw=error_config,
                label='Single-linked')

ax.text(1, values_slist[0], str(values_slist[0]), fontsize=10, verticalalignment='bottom', rotation=0,
        horizontalalignment='center')
ax.text(2, values_nlist[0], str(values_nlist[0]), fontsize=10, verticalalignment='bottom', rotation=0,
        horizontalalignment='center')

# rects2 = ax.bar([2, 6], values_elist, bar_width,
# alpha=opacity,
# color='r',
#                yerr=errors_elist,
# error_kw=error_config,
#                label='Table XOR')

rects3 = ax.bar([2, 5], values_nlist, bar_width,
                # alpha=opacity,
                # color='r',
                yerr=errors_nlist,
                # error_kw=error_config,
                label='Node XOR')


# ax.set_xlabel('')
ax.set_ylabel('Memory events per\ninsert operation')
#ax.set_title('Scores by group and gender')
ax.set_xticks([1.5, 4.5])
ax.set_xticklabels(('Bits Flipped', 'Bytes Written'))
ax.legend()

fig.tight_layout()


output = sys.argv[1]
plt.savefig(output)
