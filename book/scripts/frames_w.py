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

values_f = [640, 512, 640]

fig, ax = plt.subplots(figsize=(4, 1.7))

index = np.arange(len(values_f))
bar_width = 0.5

#opacity = 0.4
#error_config = {'ecolor': '0.3'}

rects1 = ax.bar(index, values_f, bar_width,
                # error_kw=error_config
                )

# ax.set_xlabel('')
ax.set_ylabel('Bytes written\nper iteration')
#ax.set_title('Scores by group and gender')
ax.set_xticks(index)
ax.set_xticklabels(('x-x', 'x-s', 'x-y'))
# ax.legend()

fig.tight_layout()


output = sys.argv[1]
plt.savefig(output)
