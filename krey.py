#!/usr/bin/python
import sys
import numpy as np
b = np.zeros(shape=(4,4))
list_of_lists = []

for line in sys.stdin:
    new_list = [float(elem) for elem in line.split()]
    list_of_lists.append(new_list)
 
b = list_of_lists
c= np.zeros(shape=(4,5))
key = 1
for i in range(0,4):
    c[i][0] = key
    key = key+1
for k in range(0,4):
    for l in range(0,4):
         c[k][l+1] = b[k][l]




for m in range(0,4):
    for n in range(0,5):
        print "%d \t"%c[m][n],#sys.stdout.write("%.2f\t"%(np.array(c[m][n])))
    print



