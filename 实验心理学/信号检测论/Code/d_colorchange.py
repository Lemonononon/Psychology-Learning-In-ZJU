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
        print('size:', m+2, end=' ')
        P_h = count[m][1] / count[m][0]
        P_h = min(P_h, 0.99)
        P_fa = count[m][3] / count[m][2]
        P_fa = max(P_fa, 0.01)
        Z_h = st.norm.ppf(P_h)
        Z_fa = st.norm.ppf(P_fa)
        d = Z_h - Z_fa
        if m+2 == 6:
            print( format(P_h,'.4f'),format(P_fa,'.5f'),format(Z_h,'.5f'), format(Z_fa,'.5f'), format(d,'.4f'),sep=' ')#,'%.4f',P_fa, '%.4f',Z_h, '%.4f',Z_fa,'%.4f', d), sep = '')
        else:
            print( format(P_h,'.4f'),format(P_fa,'.5f'),format(Z_h,'.5f'), format(Z_fa,'.5f'), format(d,'.4f'),sep=' ', end=' ')

    # print('size:',3)
    # P_h = count[1][1] / count[1][0]
    # P_fa = count[1][3] / count[1][2]
    # Z_h = st.norm.ppf(P_h)
    # Z_fa = st.norm.ppf(P_fa)
    # d = Z_h - Z_fa
    # print('P_h:', P_h, '\n', 'P_fa:',P_fa, '\n', 'Z_h:',
    # Z_h,'\n', 'Z_fa:', Z_fa, '\n', 'd:', d, sep = '')

    # print('size:',4)
    # P_h = count[2][1] / count[2][0]
    # P_fa = count[2][3] / count[2][2]
    # Z_h = st.norm.ppf(P_h)
    # Z_fa = st.norm.ppf(P_fa)
    # d = Z_h - Z_fa
    # print('P_h:', P_h, '\n', 'P_fa:',P_fa, '\n', 'Z_h:',
    # Z_h,'\n', 'Z_fa:', Z_fa, '\n', 'd:', d, sep = '')

    # print('size:',5)
    # P_h = count[3][1] / count[3][0]
    # P_fa = count[3][3] / count[3][2]
    # Z_h = st.norm.ppf(P_h)
    # Z_fa = st.norm.ppf(P_fa)
    # d = Z_h - Z_fa
    # print('P_h:', P_h, '\n', 'P_fa:',P_fa, '\n', 'Z_h:',
    # Z_h,'\n', 'Z_fa:', Z_fa, '\n', 'd:', d, sep = '')

    # print('size:',6)
    # P_h = count[4][1] / count[4][0]
    # P_fa = count[4][3] / count[4][2]
    # Z_h = st.norm.ppf(P_h)
    # Z_fa = st.norm.ppf(P_fa)
    # d = Z_h - Z_fa
    # print('P_h:', P_h, '\n', 'P_fa:',P_fa, '\n', 'Z_h:',
    # Z_h,'\n', 'Z_fa:', Z_fa, '\n', 'd:', d, sep = '')

    ##### RATE ############
    # for j in range(1, 389):
    #     if s_size[j] == '2':
    #         count[0] += 1
    #         if s_repeat[j] != '0':
    #             wrong[0] += 1
    #     elif s_size[j]== '3':
    #         count[1] += 1
    #         if s_repeat[j] != '0':
    #             wrong[1] += 1
 
    #     elif s_size[j] == '4':
    #         count[2] += 1
    #         if s_repeat[j] != '0':
    #             wrong[2] += 1

    #     elif s_size[j] == '5':
    #         count[3] += 1
    #         if s_repeat[j] != '0':
    #             wrong[3] += 1
    #     else:
    #         count[4] += 1
    #         if s_repeat[j] != '0':
    #             wrong[4] += 1
    # for size in range(0, 5):
    #     rate[size] =  (count[size] - wrong[size]) / count[size] * 1.0
    #     print('size:', size + 2, '正确率: ', rate[size], end = ' ')
    # print('\n')

    #### RT ####
    # for j in range(1, 389):
    #     if s_size[j] == '2':
    #         count[0] += 1
    #         time[0] += int(s_time[j])
    #     elif s_size[j] == '3':
    #         count[1] += 1
    #         time[1] += int(s_time[j])
    #     elif s_size[j] == '4':
    #         count[2] += 1
    #         time[2] += int(s_time[j])
    #     elif s_size[j] == '5':
    #         count[3] += 1
    #         time[3] += int(s_time[j])
    #     else:
    #         count[4] += 1
    #         time[4] += int(s_time[j])
    # for k in range(0, 5):
    #     time[k] = time[k] / count[k]
    #     print('size:', k + 2, 'rt:', time[k])