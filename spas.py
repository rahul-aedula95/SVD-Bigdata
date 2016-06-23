#!/usr/bin/python
import sys
import numpy as np
list_of_lists = []

a = np.zeros(shape=(4,5))
for line in sys.stdin:
    new_list = [float(elem) for elem in line.split()]
    list_of_lists.append(new_list)

a = list_of_lists

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

