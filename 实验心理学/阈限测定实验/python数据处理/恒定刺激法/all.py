import pandas as pd
import numpy as np

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
print('longer:',num, '\n','shorter:', num_shorter)

for m in range(0, 30):
    print(m+1, end=': ')
    for o in range(0, 6):
        if num[m][o] > 0.75:
            break
    for p in range(0, 6):
        if num_shorter[m][p] < 0.75:
            break
    x =  number[o -1] + 6* (0.75 - num[m][o -1])/(num[m][o] - num[m][o-1] )
    #print(x, end = ' ')
    # print(x)
    y = number[p - 1] + 6 * (num_shorter[m][p - 1] - 0.75)/(num_shorter[m][p - 1] - num_shorter[m][p])
    #print(y)
    print('pse = ', (x + y)/2, 'chabie = ', (x-y) /2 )