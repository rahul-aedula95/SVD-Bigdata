#!/usr/bin/python
import sys
import numpy as np
c = np.zeros(shape=(2,2))
c = np.loadtxt(sys.stdin)
d=[0.0,0.0]

for i in range(0,1):
    d[i]=np.linalg.eigvals(c)
    print d[i]

