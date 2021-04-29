import pandas as pd
import numpy as np
import os
data = [0]*15

all = 0
for i in range(1,31):
    #print(i, end=': ')
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
    all = all + num

pse = all/(96*30)
adc = 0
top = 0
for i in range(1,31):
    #print(i, end=': ')
    #print(':')
    filename = str(i) + '.csv'
    df=pd.read_csv(filename,header=None,sep=',') 
    series1 = df[8]
    series2 = df[9]
    for k in range(1, 97):
        adc = adc + abs( int(series2[k]) - pse)
        top = top + abs( int(series2[k]) - 200)

dis_200 = top/(30*96)
dis_pse = adc/(30*96)
print('pse:', pse)
print('差别阈限 dis_200：', dis_200, 'dis_pse: ', dis_pse)
    #print(200,end=' ')
    #result = 0
    #for k in range(1, 97):
    #    result = result + abs( int(series2[k]) - 200 )
    #print(result/96)