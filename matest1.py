#!/usr/bin/env python
import sys
import numpy as np
b = np.zeros(shape=(4,4))
b = np.loadtxt(sys.stdin)
c = np.zeros(shape=(4,5))
key = 1
for i in range(0,4):
    c[i][0] = key
    key = key+1
for k in range(0,4):
    for l in range(0,4):
         c[k][l+1] = b[k][l]



  
for m in range(0,4):
    for n in range(0,5):
        sys.stdout.write("%.2f\t"%(np.array(c[m][n]),))
    print 
