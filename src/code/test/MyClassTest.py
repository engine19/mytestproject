'''
Created on Jun 4, 2018

@author: Felhasználó
'''

import unittest
from code.myclass import MyClass

class TestMyClass(unittest.TestCase):
    def testFuncA(self):
        mc = MyClass()
        result = mc.funcA(paramA=2)
        self.assertEqual(result, 3)
        
    def testFuncB(self):
        mc = MyClass()
        result = mc.funcB(paramA=2)
        self.assertEqual(result, 3)