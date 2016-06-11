#!/usr/bin/python
import sys
import numpy as np

b = np.zeros(shape=(2,2))
#with open('test.txt','r') as f:  
b = np.loadtxt(sys.stdin)

print "{0}".format(b)
