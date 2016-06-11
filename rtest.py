#!/usr/bin/python
import sys
import numpy as np
from  StringIO import StringIO

a = np.zeros(shape=(3,4))
a = np.loadtxt(sys.stdin)

print a

   
