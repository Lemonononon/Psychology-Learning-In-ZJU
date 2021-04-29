import pandas as pd
import numpy as np
import numpy as np

right = [0]*6
fault = [0]*6
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
                right[0] += 1
            else:   fault[0] += 1
        elif kind[j] == '191':
            if series2[j] == 'Longer':
                right[1] += 1
            else:   fault[1] += 1
        elif kind[j] == '197':
            if series2[j] == 'Longer':
                right[2] += 1
            else:   fault[2] += 1
        elif kind[j] == '203':
            if series2[j] == 'Longer':
                right[3] += 1
            else:   fault[3] += 1
        elif kind[j] == '209':
            if series2[j] == 'Longer':
                right[4] += 1
            else:   fault[4] += 1
        else:
            if series2[j] == 'Longer':
                right[5] += 1
            else:   fault[5] += 1

for k in range(0, 6):
    beichu = right[k] + fault[k]
    right[k] /= beichu
    fault[k] /= beichu
print('right:',right, 'false:', fault)


x =  203 + 6* (0.75 - right[3])/(right[4] - right[3] )
print(x)
y = 191 + 6 * (fault[1] - 0.75)/(fault[1] - fault[2])
print(y)

print('pse = ', (x+y)/2, '\n', 'chabie = ', (x - y)/2)