'''
Created on Jun 4, 2018

@author: User
'''

class MyClass(object):
    PropA = -1
    
    def __init__(self, a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def setPropA(self, _propA):
        self.PropA = _propA
    

myclass = MyClass(1,2,3)
print(myclass.PropA)