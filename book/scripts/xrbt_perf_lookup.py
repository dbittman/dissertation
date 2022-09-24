import sys
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

values_x = [116.2, 441]
errors_x = [1, 3]

values_b = [152.3, 517]
errors_b = [2, 3]

values_r = [115.3, 482.6]
errors_r = [1, 2]

fig, ax = plt.subplots(figsize=(4, 2.3))

index = np.arange(len(values_r))
bar_width = 0.25

#opacity = 0.4
#error_config = {'ecolor': '0.3'}

rects1 = ax.bar(index, values_x, bar_width,
                yerr=[x*2 for x in errors_x],
                # error_kw=error_config,
                label='xrbt')

rects2 = ax.bar(index + bar_width + 0.02, values_b, bar_width,
                # alpha=opacity,
                # color='r',
                yerr=[x*2 for x in errors_b],
                # error_kw=error_config,
                label='xrbt-big')

rects3 = ax.bar(index + bar_width*2 + 0.04, values_r, bar_width,
                # alpha=opacity,
                # color='r',
                yerr=[x*2 for x in errors_r],
                # error_kw=error_config,
                label='rbt')


# ax.set_xlabel('')
ax.set_ylabel('Nanoseconds per lookup')
#ax.set_title('Scores by group and gender')
ax.set_xticks(index + bar_width + 0.02)
ax.set_xticklabels(('Seq. Lookup', 'Rand. Lookup'))
ax.legend()

fig.tight_layout()


output = sys.argv[1]
plt.savefig(output)
