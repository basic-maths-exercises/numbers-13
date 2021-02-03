try:
    import AssCheck.plotchecks as pc
    from AssCheck.plotclass import line
except:

    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install", "AssCheck"])
    import AssCheck.plotchecks as pc
    from AssCheck.plotclass import line	

import unittest
from main import *

xvals, yvals = np.linspace(1,20,20), np.zeros(20)
est=1
for i in range(20) : 
    est = 1 + 1. / ( 1 + est )
    yvals[i]=est
line1 = line(xvals,yvals)

axislabels = ["Iteration", "Estimate"]

class UnitTests(unittest.TestCase) :
    def test_plot(self) :
        assert(pc.check_plot([line1],explabels=axislabels))
