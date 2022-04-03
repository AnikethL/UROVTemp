import sys 
import numpy as np 
from numpy.linalg import inv

x = np.matrix([[1,2],[3,4]])
y = np.matrix([[3,4],[5,6]])
xinv = inv(x)
w = np.dot(y,xinv)
winv=inv(w)
stored = {}
#stored[y] = y
idx = 0 

while (np.allclose(y,w) == False):  
    idx +=1 
    w = (np.dot(y,winv))
    print(w)
    if not hash(str(y)) in stored:
        stored[hash(str(y))] = w
    if idx == 100:
        print(stored)
        break
    y = w

'''
from logging import info
import sys 
import numpy as np 
from numpy.linalg import inv

# add x,y(key) and w(value) to dictionary
# 2nd project take x and y, find w, use that w as the y value... do this input number of times

x = np.matrix([[1,2], [3,4]])
y = np.matrix([[3,4], [5,6]])
xinv = inv(x)

w = (np.dot(y,xinv))

print(w)


for i in range (n):
    for i in range(n):
        


'''