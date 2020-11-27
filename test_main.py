import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_xvals(self) :
        fighand=plt.gca()
        figdat = fighand.get_lines()[0].get_xydata()
        this_x, this_y = zip(*figdat)
        self.assertTrue( len(this_x)==20, "The number of points in your graph is incorrect" )
        for i in range( len(this_x) ) :
            self.assertTrue( np.abs(i+1-this_x[i])<1e-7, "The x values in your graph are wrong" )
            
    def test_yvals(self) : 
        fighand=plt.gca()
        figdat = fighand.get_lines()[0].get_xydata()
        this_x, this_y = zip(*figdat)
        est = 1.
        for i in range( len(this_x) ) :
            est = 1 + 1. / ( 1 + est )
            self.assertTrue( np.abs(est-this_y[i])<1e-7, "The y values in your graph are incorrect" )
