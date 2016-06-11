#!/usr/bin/python
import sys
import numpy as np
from subprocess import call
from StringIO import StringIO
a = np.zeros(shape=(1000,1001))                   #1
a = np.loadtxt(sys.stdin)                         #n
x = np.zeros(shape=(1000,1000))#,dtype=complex)    1
y = np.zeros(shape=(1000,1000))#,dtype=complex)    1
u = np.zeros(shape=(1000,1000),dtype=complex)     #1  
v = np.zeros(shape=(1000,1000),dtype=complex)     #1
for i in xrange(0,1000):                          #2(n+1)
    for j in xrange(0,1000):                      #2n(n+1)

        x[i][j]=a[i][j+1]                         #n^2

np.set_printoptions(threshold=np.nan)
np.set_printoptions(suppress=True)
u,s,v = np.linalg.svd(x)                           #A(n)
for m in xrange(0,1000):                           #2(n+1)
    for n in xrange(0,1000):                       #2(n)(n+1)
        if(m==n):                                  #2(n^2)
          y[m][n]=s[m]


print u                                            #3
print 
print y
print
print v
                  
