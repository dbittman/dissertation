import matplotlib.pyplot as plt
import numpy as np
import sys

# X axis parameter:
xaxis = np.array([2, 8])

# Y axis parameter:
yaxis = np.array([4, 9])

plt.plot(xaxis, yaxis)
plt.savefig(sys.argv[1])
