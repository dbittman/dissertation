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

values_x = [197.8, 472.9]
errors_x = [1, 3]

values_b = [284, 565]
errors_b = [3, 3]

values_r = [218.7, 524.2]
errors_r = [2, 2]

fig, ax = plt.subplots(figsize=(4, 2.3))

index = np.arange(len(values_r))
bar_width = 0.25

#opacity = 0.4
#error_config = {'ecolor': '0.3'}

rects1 = ax.bar(index, values_x, bar_width,
                yerr=[x*2 for x in errors_x],
                # error_kw=error_config,
                label='xrbt')

rects2 = ax.bar(index + bar_width+0.02, values_b, bar_width,
                # alpha=opacity,
                # color='r',
                yerr=[x*2 for x in errors_b],
                # error_kw=error_config,
                label='xrbt-big')

rects3 = ax.bar(index + bar_width*2+0.04, values_r, bar_width,
                # alpha=opacity,
                # color='r',
                yerr=[x*2 for x in errors_r],
                # error_kw=error_config,
                label='rbt')


# ax.set_xlabel('')
ax.set_ylabel('Nanoseconds per insert')
#ax.set_title('Scores by group and gender')
ax.set_xticks(index + bar_width + 0.02)
ax.set_xticklabels(('Seq. Insert', 'Rand. Insert'))
ax.legend()

ax.annotate("$\}$",
            xy=(0.31, 0.7), xycoords='figure fraction',
            xytext=(0.410,  0.46), textcoords='figure fraction', fontsize=13,
            arrowprops=dict(arrowstyle="-", lw=0)
            )

ax.annotate("$\{$",
            xy=(0.31, 0.7), xycoords='figure fraction',
            xytext=(0.268,  0.44), textcoords='figure fraction', fontsize=17,
            arrowprops=dict(arrowstyle="-", lw=0)
            )

ax.annotate("a",
            xy=(0.31, 0.68), xycoords='figure fraction',
            xytext=(0.440,  0.461), textcoords='figure fraction', fontsize=12,
            arrowprops=dict(arrowstyle="-", lw=0)
            )

ax.annotate("b",
            xy=(0.31, 0.7), xycoords='figure fraction',
            xytext=(0.243,  0.454), textcoords='figure fraction', fontsize=12,
            arrowprops=dict(arrowstyle="-", lw=0)
            )


fig.tight_layout()


output = sys.argv[1]
plt.savefig(output)
