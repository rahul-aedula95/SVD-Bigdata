#!/usr/bin/python
import sys
import numpy as np
b = np.zeros(shape=(1000,1000)) #1
b = np.loadtxt(sys.stdin)       #n
c = np.zeros(shape=(1000,1001)) #1
key = 1                         #1
for i in xrange(0,1000):       #2(n+1)
    c[i][0] = key             #n
    key = key+1               #n

for k in xrange(0,1000):         #2(n+1)
    for l in xrange(0,1000):     #2(n)(n+1)
        c[k][l+1] = b[k][l]      #n^2


  
for m in xrange(0,1000):            #2(n+1)
    for n in xrange(0,1001):        #2(n)(n+1)
        sys.stdout.write("%.2f\t"%(np.array(c[m][n]),)) #n^2
    print                                               #n

