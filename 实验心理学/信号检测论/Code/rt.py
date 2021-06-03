import pandas as pd
import numpy as np
import os

path = 'male'
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
    count = [0]*5 #0-2个, 1-3, 2-4, 3-5, 4-6
    wrong = [0]*5
    rate = [0]*5
    time = [0]*5
    SubName = s_name[1]

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
    for j in range(1, 389):
        if s_size[j] == '2':
            count[0] += 1
            time[0] += int(s_time[j])
        elif s_size[j] == '3':
            count[1] += 1
            time[1] += int(s_time[j])
        elif s_size[j] == '4':
            count[2] += 1
            time[2] += int(s_time[j])
        elif s_size[j] == '5':
            count[3] += 1
            time[3] += int(s_time[j])
        else:
            count[4] += 1
            time[4] += int(s_time[j])
    for k in range(0, 5):
        time[k] = time[k] / count[k]
        if k == 4:
            print('size:', k + 2,' ', time[k], sep='')
        else:
            print('size:', k + 2,' ', time[k], sep='', end=' ')