'''
Created on Jun 4, 2018

@author: User
'''

from src.code.myclass import MyClass

class TestMyClass2(object):
    def testA(self):
        mc = MyClass()
        print("{0}".format(mc))
        assert mc.PropA != 1
        
    def testB(self):
        mc = MyClass()
        mc.setPropA(1)
        print("{0}".format(mc))
        assert mc.PropA == 1
        
    def testC(self):
        mc = MyClass()
        mc.setPropA(3)
        print("{0}".format(mc))
        assert mc.PropA == 3