'''
Created on 24/10/2015

@author: brad

'''
# core python imports
import unittest

# library imports

# project imports
from pybaseproj import calculator

# constants


class CalculatorTest(unittest.TestCase):

    def testAdding(self):
        a = 2
        b = 9
        expected = a + b
        self.assertEqual(expected, calculator.Calculator().add(a, b))
    

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    
