import matplotlib.pyplot as plt
import numpy as np

est, xvals, yvals, = 1, np.zeros(20), np.zeros(20)
for i in range(0,20) :
  xvals[i] = i+1
  # Your code goes here

plt.plot( xvals, yvals, 'ko')
plt.savefig( "roottwo.png")
