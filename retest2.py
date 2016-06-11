#!/usr/bin/env python
import sys
import numpy as np
from subprocess import call
from StringIO import StringIO
a = np.zeros(shape=(4,5))
a = np.loadtxt(sys.stdin)
x = np.zeros(shape=(4,4))#,dtype=complex)
y = np.zeros(shape=(4,4))#,dtype=complex)
z = np.zeros(shape=(4,4),dtype=complex)
m = np.zeros(shape=(4,4),dtype=complex)
for i in range(0,4):
    for j in range(0,4):

        x[i][j]=a[i][j+1]

np.set_printoptions(threshold=np.nan)
np.set_printoptions(suppress=True)
#np.set_printoptions(linewidth=4)
u,s,v = np.linalg.svd(x)
for m in range(0,4):
    for n in range(0,4):
        if(m==n):
          y[m][n]=s[m]


#print u
#print 
print y
'''print

print y1
print
print np.transpose(v)
print

 
k = np.dot(u,y1)
print k
print 
print x
print 
print 
print
z = np.dot(x,np.transpose(v))
f = np.dot(np.linalg.inv(u),z)
print z
print 

print
print f
'''

