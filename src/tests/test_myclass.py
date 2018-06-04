'''
Created on Jun 4, 2018

@author: Felhasználó
'''
import sys
import os

sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'code'))

from myclass import MyClass

class TestMyClass(object):
    def testA(self):
        mc = MyClass()
        print("{0}".format(mc))
        assert mc.PropA != 1
        
    def testB(self):
        mc = MyClass()
        mc.setPropA(1)
        print("{0}".format(mc))
        assert mc.PropA == 1