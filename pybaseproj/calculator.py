'''
Created on 24/10/2015

@author: brad

'''
# core python imports
import datetime

# library imports

# project imports

# constants
NUMBER_1 = 2
NUMBER_2 = 3


class Calculator(object):

    def add(self, a, b):
        return a + b
    

if __name__ == "__main__":
    print Calculator().add(NUMBER_1, NUMBER_2)
    
