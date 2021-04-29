import pandas as pd
import numpy as np
import numpy as np
from scipy.optimize import leastsq

num = np.zeros((30, 6), dtype=float)
num_shorter = np.zeros((30, 6), dtype=float)
number = [185, 191, 197, 203, 209, 215]

for i in range(1,31):
    #print(i, end=': ')
    filename = str(i) + '.csv'
    df=pd.read_csv(filename,header=None,sep=',') 
    kind = df[8]
    series1 = df[9]
    series2 = df[10]

    for j in range(1, 301):
        if kind[j] == '185':
            if series2[j] == 'Longer':
                num[i - 1][0] += 1
            else:   num_shorter[i - 1][0] += 1
        elif kind[j] == '191':
            if series2[j] == 'Longer':
                num[i - 1][1] += 1
            else:   num_shorter[i - 1][1] += 1
        elif kind[j] == '197':
            if series2[j] == 'Longer':
                num[i - 1][2] += 1
            else:   num_shorter[i - 1][2] += 1
        elif kind[j] == '203':
            if series2[j] == 'Longer':
                num[i - 1][3] += 1
            else:   num_shorter[i - 1][3] += 1
        elif kind[j] == '209':
            if series2[j] == 'Longer':
                num[i - 1][4] += 1
            else:   num_shorter[i - 1][4] += 1
        else:
            if series2[j] == 'Longer':
                num[i - 1][5] += 1
            else:   num_shorter[i - 1][5] += 1

for k in range(0, 30):
    for l in range(0, 6):
        num[k][l] /= (num[k][l] + num_shorter[k][l])*1.0
        num_shorter[k][l] =  1 - num[k][l]
# print('longer:',num, '\n','shorter:', num_shorter)

#最小二乘法

for m in range(0, 30):
    print(m + 1, end = ':')
    Xi = np.array([185, 191, 197, 203, 209, 215])
    Yi = np.array(num[m])
    Yi_shorter = np.array(num_shorter[m])
    def fun(p,x): #回归模型函数
        k,b = p
        return k*x+b

    def error(p,x,y): #误差
        return fun(p,x)-y

    p0 = np.array([1,3])
    para1 = leastsq(error,p0,args=(Xi,Yi))
    para2 = leastsq(error,p0,args=(Xi,Yi_shorter))
    k1, b1 = para1[0]
    k2, b2 = para2[0]
    x = (0.75 - b1) / k1
    y = (0.75 - b2) / k2
    # print('k1 = ', k1, 'b1 = ', b1)
    # print('k2 = ', k2, 'b2 = ', b2)
    print('esp = ', (x + y) / 2, 'chabie = ', (x - y) / 2)
    #y = kx + b
    #x = (y - b) / k