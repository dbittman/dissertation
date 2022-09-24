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
#matplotlib.rcParams.update({'font.size': 9})

values_s = [37.2, 8, 4.7]
errors_s = [1, 0.1, 0.3]

#values_e = [16.7, 3.8, 155, 55.6]
#errors_e = [5, 2, 5, 2]

values_n = [37.05, 8.5, 5]
errors_n = [0.4, 0.3, 0.1]

fig, ax = plt.subplots(figsize=(4, 1.8))

index = np.arange(len(values_s))
bar_width = 0.4

#opacity = 0.4
#error_config = {'ecolor': '0.3'}

rects1 = ax.bar(index, values_s, bar_width,
                yerr=[x for x in errors_s],
                # error_kw=error_config,
                label='Single-linked')

# rects2 = ax.bar(index + bar_width, values_e, bar_width,
# alpha=opacity,
# color='r',
#               yerr=[x for x in errors_e],
# error_kw=error_config,
#              label='Table XOR')

rects3 = ax.bar(index + bar_width + 0.02, values_n, bar_width,
                # alpha=opacity,
                # color='r',
                yerr=[x for x in errors_n],
                # error_kw=error_config,
                label='Node XOR')


# ax.set_xlabel('')
ax.set_ylabel('Nanoseconds\nper operation')
#ax.set_title('Scores by group and gender')
ax.set_xticks(index + bar_width/2 + 0.01)
ax.set_xticklabels(('Insert', 'Lookup', 'Delete'))
ax.legend()

fig.tight_layout()

output = sys.argv[1]
plt.savefig(output)
