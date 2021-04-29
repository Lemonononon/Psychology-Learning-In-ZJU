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
        num = num + int(series2[j])
    average = num /96
    print(average ,end=' ')
    result = 0
    for k in range(1, 97):
        result = result + abs( int(series2[k]) - average )
    print(result/96)