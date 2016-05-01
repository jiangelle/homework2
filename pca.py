# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 22:46:07 2016

@author: jurcol
"""
import matplotlib.pyplot as plt
import numpy as np

file = open("optdigits.tes.txt")
data3 = [ ]
while 1:
    line = file.readline()
    if not line:
        break
    line = line.strip('\n')
    list1 = line.split(',')
    for index, item in enumerate(list1):
        list1[index] = int(item)
    data = np.array(list1)
    if data[64]==3:
        data = data[0:64]
        data3.append(data)

pdata = np.transpose(data3)
[i,j]=pdata.shape
print i,j
for a in range(i):
    for b in range(j):
        pdata[a,b]=pdata[a,b]-np.mean(pdata[a,:])

C = 1.0/j*np.dot(pdata,np.transpose(pdata))
w,v=np.linalg.eig(C)
a=np.argsort(-w)
a=a[0:2]
P=[v[:,a[0]],v[:,a[1]]]
y = np.dot(P,pdata)
[i,j] = y.shape
print i,j

plt.plot(y[0,:],y[1,:],'.',color='green')
plt.xlabel('first principle component')
plt.ylabel('second principle component')

y1max = np.max(y[0,:])
y2max = np.max(y[1,:])
y1min = np.min(y[0,:])
y2min = np.min(y[1,:])
y1 = np.linspace(y1min, y1max, 5)
y2 = np.linspace(y2min, y2max, 5)

index = np.empty(25)

for k in range(5):
    for h in range(5):
        min1 = 100
        for m in range(j):
            dis = (y1[k]-y[0,:][m])**2 + (y2[h]-y[1,:][m])**2
            if dis < min1:
                min1 = dis 
                index[(k-1)*5+h-1] = m
                
pshow = np.empty((8,8,3))
ptshow = np.empty((40,40,3))
for a in range(25):
    for j in range(3):
        pshow[:,:,j] = pdata[:,index[a]].reshape(8,8)[:,:]
    ptshow[a/5*8 : a/5*8+8, a%5*8: a%5*8+8] = pshow
plt.imshow(ptshow)
