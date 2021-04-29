import pandas as pd
import numpy as np

number = [0]*40
for i in range(1, 31):
    # print(i, end=': ')
    filename = str(i) + '.csv'
    df=pd.read_csv(filename,header=None,sep=',') 
    series = df[8]
    for j in range(0, 40):
        number[j] += int(series[j + 1])
print(number)
for k in range(0, 40):
    number[k] /= 30
print(number)