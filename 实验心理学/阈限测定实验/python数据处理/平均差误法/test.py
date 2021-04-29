import pandas as pd
import numpy as np
import os
data = [0]*15
for i in range(1,16):
    print(i, end=': ')
    #print(':')
    filename = str(i) + '.csv'
    df=pd.read_csv(filename,header=None,sep=',') 
    series1 = df[8]
    series2 = df[9]
    #print(series1)
    #print(series2)
    #print(series1[40])
    num = 0
    for j in range(1, 97):
        num = num + int(series1[j]) + int(series2[j])
    print(num)
    #print(int(series1[40:41]).apply(sum))
    #print(int(series1[1]) + int(series1[2]))
    #print(type(int(series1[1])))
    #result = abs(200 - )/40
    #data[i -1] = num
    #print(df)
    #print('\n')
#print(data)
#print(df.head()) 
#print(df.tail())