import sys
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import os

matplotlib.use("pgf")
#matplotlib.rc('font',**{'family':'sans-serif','sans-serif':['Source Sans Pro']})
#matplotlib.rcParams['pdf.fonttype'] = 42
#matplotlib.rcParams['font.family'] = "sans-serif"

plt.figure(num=None, figsize=(4, 2), facecolor='w', edgecolor='k')
#matplotlib.rcParams.update({'font.size': 10})

values_f = [9.8, 2.75]
errors_f = [0.6, 0.2]

values_w = [14.1, 14.1]
errors_w = [0.8, 0.8]

values_r = [15.7, 15.7]
errors_r = [0.1, 0.1]

fig, ax = plt.subplots(figsize=(4, 2.2))

index = np.arange(len(values_r))
bar_width = 0.25

#opacity = 0.4
#error_config = {'ecolor': '0.3'}

values_d = [9.8, 14.1, 15.7]
values_x = [2.75, 14.1, 15.7]
errs_d = [0.6, .8, .1]
errs_x = [0.2, .8, .1]

rects1 = ax.bar([1, 4, 7], values_d, yerr=errs_d, label='Doubly')

rects2 = ax.bar([2, 5, 8], values_x, yerr=errs_x, label='XOR')


# rects1 = ax.bar(index, values_f, bar_width,
#                yerr=errors_f,
# error_kw=error_config,
#                label='Bits flipped')

# rects2 = ax.bar(index + bar_width, values_w, bar_width,
# alpha=opacity,
# color='r',
#                yerr=errors_w,
# error_kw=error_config,
#                label='Bytes written')

# rects3 = ax.bar(index + bar_width*2, values_r, bar_width,
# alpha=opacity,
# color='r',
#                yerr=errors_r,
# error_kw=error_config,
#                label='Bytes read')


# ax.set_xlabel('')
ax.set_ylabel('Memory events\nper operation')
#ax.set_title('Scores by group and gender')
ax.set_xticks([1.5, 4.5, 7.5])
ax.set_xticklabels(('Bits Flipped', 'Bytes Written', 'Bytes Read'))
ax.legend()

fig.tight_layout()


output = sys.argv[1]
plt.savefig(output)
