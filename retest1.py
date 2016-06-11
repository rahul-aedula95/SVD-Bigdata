#!/usr/bin/python
import sys
import numpy as np
from subprocess import call
from StringIO import StringIO
a = np.zeros(shape=(1000,1001))
a = np.loadtxt(sys.stdin)
x = np.zeros(shape=(1000,1000))#,dtype=complex)
y = np.zeros(shape=(1000,1000))#,dtype=complex)
z = np.zeros(shape=(1000,1000))#,dtype=complex)
f = np.zeros(shape=(1000,1000))#,dtype=complex)
for i in range(0,1000):
    for j in range(0,1000):

        x[i][j]=a[i][j+1]

np.set_printoptions(threshold=np.nan)
np.set_printoptions(suppress=True)
#np.set_printoptions(linewidth=1000)
u,s,v = np.linalg.svd(x)
for m in range(0,1000):
    for n in range(0,1000):
        if(m==n):
          y[m][n]=s[m]

k = np.dot(u,y)
z = np.dot(x,np.transpose(v))
f = np.dot(np.linalg.inv(u),z)

print y
print
print k
print
print z
print 
print f

