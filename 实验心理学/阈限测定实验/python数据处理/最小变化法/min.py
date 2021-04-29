import pandas as pd
import numpy as np
import os
data_up = [0]*30
data_low = [0]*30
pse_up = [0]*30
pse_low = [0]*30
for i in range(1,31):
    #print(i, end=': ')
    filename = str(i) + '.csv'
    df=pd.read_csv(filename,header=None,sep=',') 
    kind = df[6]
    series1 = df[11]
    series2 = df[12]
    num_up = 0
    num_low = 0
    sum_up = 0
    sum_low = 0
    for j in range(1, 41):
        if kind[j] == 'IncreaseSeries' :
            num_up = num_up + (float(series1[j]) - float(series2[j]))/2
            sum_up = sum_up + (float(series1[j]) + float(series2[j]))/2
        else:
            num_low = num_low + (float(series1[j]) - float(series2[j]))/2
            sum_low = sum_low + (float(series1[j]) + float(series2[j]))/2
    average_up = num_up / 20 #绝对阈限（增）
    data_up[i - 1] = average_up
    average_low = num_low / 20 #绝对阈限（减）
    data_low[i - 1] = average_low
    pse_up[i - 1] = sum_up / 20
    pse_low[i - 1] = sum_low /20

print('+', data_up)
print('+', pse_up)
print('-', data_low)
print('-',pse_low)
