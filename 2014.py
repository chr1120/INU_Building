#!/usr/bin/env python
# coding: utf-8

# In[3]:


# https://blog.naver.com/chromatic_365/222657670527
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import pymysql
#전체 출력
#pd.set_option('display.max_seq_items', None)
#pd.set_option('display.max_rows', None)

# mysql db 연동
db = pymysql.connect(host='127.0.0.1',password='gkftndlTek!!',user='root',db='tp',charset='utf8', 
    cursorclass=pymysql.cursors.DictCursor)

cursor = db.cursor()

query = "select * from wholeData where DATETIME between '2014-05-01 00:00:00' and '2014-08-31 23:00:00'"
cursor.execute(query)
db_export = cursor.fetchall()

tp=pd.DataFrame(db_export)

# columns 리스트 전부 출력
# print(tp.columns)

#표준편차 계산
#std=np.std(tp,axis=0)
#print(std)

# https://blog.naver.com/moongda0404/222729519749
# scaling
def standard_scaling(df, scale_columns):
    for col in scale_columns:
        series_mean = df[col].mean()
        series_std = df[col].std()
        df[col] = df[col].apply(lambda x: (x-series_mean)/series_std)
    return df

scale_columns = ['FM', 'PU1', 'PU2', 'TE1', 'TE2', 'TE3', 'P1', 'P2', 'P3','P4', 
        'FM_[0]', 'PU1_[0]', 'PU2_[0]', 'TE1_[0]', 'TE2_[0]', 'TE3_[0]', 'P1_[0]', 'P2_[0]', 'P3_[0]','P4_[0]',
        'FM_[1]', 'PU1_[1]', 'PU2_[1]', 'TE1_[1]', 'TE2_[1]', 'TE3_[1]', 'P1_[1]', 'P2_[1]', 'P3_[1]',
       'P4_[1]', 'PU1_[2]', 'PU2_[2]', 'TE1_[2]', 'TE2_[2]', 'TE3_[2]', 'P1_[2]', 'P2_[2]', 'P3_[2]',
       'P4_[2]', 'FM_[3]', 'PU1_[3]', 'PU2_[3]', 'TE1_[3]', 'TE2_[3]', 'TE3_[3]', 'P1_[3]', 'P2_[3]', 'P3_[3]',
       'P4_[3]', 'FM_[4]', 'PU1_[4]', 'PU2_[4]', 'TE1_[4]', 'TE2_[4]', 'TE3_[4]', 'P1_[4]', 'P2_[4]', 'P3_[4]',
       'P4_[4]', 'PU1_[5]', 'PU2_[5]', 'TE1_[5]', 'TE2_[5]', 'TE3_[5]', 'P1_[5]', 'P2_[5]', 'P3_[4]',
       'P4_[5]', 'PU1_[6]', 'PU2_[6]', 'TE1_[6]', 'TE2_[6]', 'TE3_[6]', 'P1_[6]', 'P2_[6]', 'P3_[4]',
       'P4_[6]','FM_[7]', 'PU1_[7]', 'PU2_[7]', 'TE1_[7]', 'TE2_[7]', 'TE3_[7]', 'P1_[7]', 'P2_[7]', 'P3_[4]',
       'P4_[7]','FM_[8]', 'PU1_[8]', 'PU2_[8]', 'TE1_[8]', 'TE2_[8]', 'TE3_[8]', 'P1_[8]', 'P2_[8]', 'P3_[4]',
       'P4_[8]','FM_[9]', 'PU1_[9]', 'PU2_[9]', 'TE1_[9]', 'TE2_[9]', 'TE3_[9]', 'P1_[9]', 'P2_[9]', 'P3_[4]',
       'P4_[9]','FM_[10]', 'PU1_[10]', 'PU2_[10]', 'TE1_[10]', 'TE2_[10]', 'TE3_[10]', 'P1_[10]', 'P2_[10]', 'P3_[10]',
       'P4_[10]','FM_[11]', 'PU1_[11]', 'PU2_[11]', 'TE1_[11]', 'TE2_[11]', 'TE3_[11]', 'P1_[11]', 'P2_[11]', 'P3_[11]',
       'P4_[11]', 'PU1_[12]', 'PU2_[12]', 'TE1_[12]', 'TE2_[12]', 'TE3_[12]', 'P1_[12]', 'P2_[12]', 'P3_[12]',
       'P4_[12]','FM_[13]', 'PU1_[13]', 'PU2_[13]', 'TE1_[13]', 'TE2_[13]', 'TE3_[13]', 'P1_[13]', 'P2_[13]', 'P3_[13]',
       'P4_[13]','FM_[14]', 'PU1_[14]', 'PU2_[14]', 'TE1_[14]', 'TE2_[14]', 'TE3_[14]', 'P1_[14]', 'P2_[14]', 'P3_[14]',
       'P4_[14]','PU1_[15]', 'PU2_[15]', 'TE1_[15]', 'TE2_[15]', 'TE3_[15]', 'P1_[15]', 'P2_[15]', 'P3_[15]',
       'P4_[15]', 'PU1_[16]', 'PU2_[16]', 'TE1_[16]', 'TE2_[16]', 'TE3_[16]', 'P1_[16]', 'P2_[16]', 'P3_[16]',
       'P4_[16]','FM_[17]', 'PU1_[17]', 'PU2_[17]', 'TE1_[17]', 'TE2_[17]', 'TE3_[17]', 'P1_[17]', 'P2_[17]', 'P3_[17]',
       'P4_[17]','PU1_[18]', 'PU2_[18]', 'TE1_[18]', 'TE2_[18]', 'TE3_[18]', 'P1_[18]', 'P2_[18]', 'P3_[18]',
       'P4_[18]']
tp_df = standard_scaling(tp, scale_columns)
tp_df


# In[ ]:




