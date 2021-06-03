import pandas as pd
import numpy as np
import os
import scipy.stats as st

path = 'female'
file_list = os.listdir(path) # get file name

for i in file_list:
    # print(i, end=': ')
    filename = i
    df=pd.read_csv(path+'/'+filename, header = None, encoding = 'gbk') 
    s_name = df[1]
    s_size = df[4]
    s_colorChange = df[6]
    s_rt = df[16]
    s_time = df[16]
    s_repeat = df[19]
    s_shapeChange = df[5]
    count = [[0 for col in range(4)] for row in range(5)]
    wrong = [0]*5
    rate = [0]*5
    time = [0]*5
    SubName = s_name[1]

    #### d #######
    for j in range(1, 389):
        if s_size[j] == '2':
            if s_shapeChange[j] == 'NOChanged' and s_colorChange[j] == 'NOChanged':
                count[0][0] += 1
                if s_repeat[j] == '0':
                    count[0][1] += 1 # Hit
            elif s_shapeChange[j] == 'Changed' and s_colorChange[j] == 'NOChanged':
                count[0][2] += 1
                if s_repeat[j] != '0':
                    count[0][3] += 1 # False Alarm
             
        elif s_size[j] == '3':
            if s_shapeChange[j] == 'NOChanged' and s_colorChange[j] == 'NOChanged':
                count[1][0] += 1
                if s_repeat[j] == '0':
                    count[1][1] += 1 # Hit
            elif s_shapeChange[j] == 'Changed' and s_colorChange[j] == 'NOChanged':
                count[1][2] += 1
                if s_repeat[j] != '0':
                    count[1][3] += 1 # False Alarm
            

        elif s_size[j] == '4':
            if s_shapeChange[j] == 'NOChanged' and s_colorChange[j] == 'NOChanged':
                count[2][0] += 1
                if s_repeat[j] == '0':
                    count[2][1] += 1 # Hit
            elif s_shapeChange[j] == 'Changed' and s_colorChange[j] == 'NOChanged':
                count[2][2] += 1
                if s_repeat[j] != '0':
                    count[2][3] += 1 # False Alarm
            

        elif s_size[j] == '5':
            if s_shapeChange[j] == 'NOChanged' and s_colorChange[j] == 'NOChanged':
                count[3][0] += 1
                if s_repeat[j] == '0':
                    count[3][1] += 1 # Hit
            elif s_shapeChange[j] == 'Changed' and s_colorChange[j] == 'NOChanged':
                count[3][2] += 1
                if s_repeat[j] != '0':
                    count[3][3] += 1 # False Alarm

        else:
            if s_shapeChange[j] == 'NOChanged' and s_colorChange[j] == 'NOChanged':
                count[4][0] += 1
                if s_repeat[j] == '0':
                    count[4][1] += 1 # Hit
            elif s_shapeChange[j] == 'Changed' and s_colorChange[j] == 'NOChanged':
                count[4][2] += 1
                if s_repeat[j] != '0':
                    count[4][3] += 1 # False Alarm
            
    for m in range(0, 5):
        print('size:', m+2, sep='', end=' ')
        P_h = count[m][1] / count[m][0]
        P_h = min(P_h, 0.99)
        P_fa = count[m][3] / count[m][2]
        P_fa = max(P_fa, 0.01)
        Z_h = st.norm.ppf(P_h)
        Z_fa = st.norm.ppf(P_fa)
        O_h = st.norm.pdf(Z_h)
        O_fa = st.norm.pdf(Z_fa)
        beta = O_h / O_fa
        if m+2 == 6:
            print( format(P_h,'.4f'),format(P_fa,'.5f'),format(Z_h,'.5f'), format(Z_fa,'.5f'), format(beta,'.4f'),sep=' ')#,'%.4f',P_fa, '%.4f',Z_h, '%.4f',Z_fa,'%.4f', d), sep = '')
        else:
            print( format(P_h,'.4f'),format(P_fa,'.5f'),format(Z_h,'.5f'), format(Z_fa,'.5f'), format(beta,'.4f'),sep=' ', end=' ')