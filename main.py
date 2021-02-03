import matplotlib.pyplot as plt
import numpy as np

est, xvals, yvals, = 1, np.zeros(20), np.zeros(20)
for i in range(0,20) :
  xvals[i] = i+1
  # Your code goes here
  est = 1 + 1. / ( 1 + est )
  yvals[i]=est

plt.plot( xvals, yvals, 'ko')
plt.xlabel("Iteration")
plt.ylabel("Estimate")
plt.savefig( "roottwo.png")
