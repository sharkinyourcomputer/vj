import unittest
import chop
import numpy as np

class ChopTest(unittest.TestCase):

  def testChop(self):
    signal = np.arange(7)
    
    output = chop.Chop(1000, signal, 3)
    
    f = ([0,1,2], [3, 4, 5], [6, 0, 0])
    
    self.assertTrue((output == f).all())
  
  
if __name__ == '__main__':
  unittest.main()	