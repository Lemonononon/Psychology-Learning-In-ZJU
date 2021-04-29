import pandas as pd
import numpy as np
import numpy as np
from scipy.optimize import leastsq

Xi = np.array([185, 191, 197, 203, 209, 215])
Yi = np.array([0.02, 0.04, 0.12, 0.36, 0.8, 0.88])

def fun(p,x): #回归模型函数
    k,b = p
    return k*x+b

def error(p,x,y): #误差
    return fun(p,x)-y

p0 = np.array([1,3])
para = leastsq(error,p0,args=(Xi,Yi))
k,b = para[0]
print('y1 = '+str(round(k,2)) + 'x1 +' + str(round(b,2)))