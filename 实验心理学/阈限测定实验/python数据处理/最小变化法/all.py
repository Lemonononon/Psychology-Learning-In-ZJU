import pandas as pd
import numpy as np
import os
data_up = [0]*30
data_low = [0]*30
sum_up = 0
sum_low = 0
pse_up = 0
pse_low = 0
for i in range(1,31):
    #print(i, end=': ')
    filename = str(i) + '.csv'
    df=pd.read_csv(filename,header=None,sep=',') 
    kind = df[6]
    series1 = df[11]
    series2 = df[12]
    num_up = 0
    num_low = 0
    pse_u = 0
    pse_l = 0
    for j in range(1, 41):
        if kind[j] == 'IncreaseSeries' :
            num_up = num_up + (float(series1[j]) - float(series2[j]))/2
            pse_u = pse_u + (float(series1[j]) + float(series2[j]))/2
        else:
            num_low = num_low + (float(series1[j]) - float(series2[j]))/2
            pse_l = pse_l + (float(series1[j]) + float(series2[j]))/2
    sum_up = sum_up + num_up
    sum_low = sum_low + num_low
    pse_up = pse_up + pse_u
    pse_low = pse_low + pse_l
average_up = sum_up / (20*30) #绝对阈限（增）
average_low = sum_low / (20*30) #绝对阈限（减）
pse_up_all = pse_up / (20*30)
pse_low_all = pse_low / (20*30)
print('pse_up = ', pse_up_all, ',', 'pse_low = ', pse_low_all)
print('average_up = ', average_up,',', 'average_low = ', average_low)