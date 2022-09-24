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

plt.figure(num=None, figsize=(4, 3), facecolor='w', edgecolor='k')
#matplotlib.rcParams.update({'font.size': 10})

values_f = [24, 22, 90.6]
errors_f = [0.01, 0.01, 2]

fig, ax = plt.subplots(figsize=(4, 1.7))

index = np.arange(len(values_f))
bar_width = 0.5

#opacity = 0.4
#error_config = {'ecolor': '0.3'}

rects1 = ax.bar(index, values_f, bar_width,
                yerr=errors_f,
                # error_kw=error_config
                )
plt.ylim(top=105)
plt.yticks([0, 20, 40, 60, 80, 100])

ax.text(0, 25, str(24), color='black', fontweight='normal', fontsize=10,
        horizontalalignment='center')
ax.text(1, 23, str(22), color='black', fontweight='normal', fontsize=10,
        horizontalalignment='center')
ax.text(2, 93, str(90.6), color='black', fontweight='normal', fontsize=10,
        horizontalalignment='center')

# ax.set_xlabel('')
ax.set_ylabel('Bits flipped\nper iteration')
#ax.set_title('Scores by group and gender')
ax.set_xticks(index)
ax.set_xticklabels(('x-x', 'x-s', 'x-y'))
# ax.legend()

fig.tight_layout()


output = sys.argv[1]
plt.savefig(output)
