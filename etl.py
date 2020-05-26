import datetime, warnings, scipy 
import pandas as pds
import numpy as npy
import time
import datetime



#read each csv files from 2018 to 2014
df0 = pds.read_csv('2014.csv',error_bad_lines=False)
df1 = pds.read_csv('2015.csv',error_bad_lines=False)
df2 = pds.read_csv('2016.csv',error_bad_lines=False)
df3 = pds.read_csv('2017.csv',error_bad_lines=False)
df4 = pds.read_csv('2018.csv',error_bad_lines=False)

#remove unwanted attributes from datasets that have insufficient data or do not help in estimating the output
unwanted_attributes = ['OP_CARRIER_FL_NUM', 'CRS_DEP_TIME', 'DEP_TIME', 'TAXI_OUT', 'TAXI_IN', 'WHEELS_ON', 'WHEELS_OFF','CRS_ARR_TIME', 'ARR_TIME','CRS_ELAPSED_TIME', 'AIR_TIME', 'CANCELLED', 'CANCELLATION_CODE','DISTANCE','CARRIER_DELAY','WEATHER_DELAY', 'NAS_DELAY', 'SECURITY_DELAY','LATE_AIRCRAFT_DELAY', 'Unnamed: 27']
df0.drop(unwanted_attributes, axis = 1, inplace = True)
df1.drop(unwanted_attributes, axis = 1, inplace = True)
df2.drop(unwanted_attributes, axis = 1, inplace = True)
df3.drop(unwanted_attributes, axis = 1, inplace = True)
df4.drop(unwanted_attributes, axis = 1, inplace = True)

#extra month from a column and add to the dataset
df0['Month'] = pds.DatetimeIndex(df0['FL_DATE']).month
df1['Month'] = pds.DatetimeIndex(df1['FL_DATE']).month
df2['Month'] = pds.DatetimeIndex(df2['FL_DATE']).month
df3['Month'] = pds.DatetimeIndex(df3['FL_DATE']).month
df4['Month'] = pds.DatetimeIndex(df4['FL_DATE']).month

#find the number of  rows in each csv
row_num= df0.shape[0]
x0=row_num/2
row_num= df1.shape[0]
x1=row_num/2
row_num= df2.shape[0]
x2=row_num/2
row_num= df3.shape[0]
x3=row_num/2
row_num= df4.shape[0]
x4=row_num/2

#split the dataframe into two dataframes to reduce the size
df0_1 = df0.iloc[:int(x0), :]
df0_2 = df0.iloc[int(x0):,:]
df1_1 = df1.iloc[:int(x1), :]
df1_2 = df1.iloc[int(x1):,:]
df2_1 = df2.iloc[:int(x2), :]
df2_2 = df2.iloc[int(x2):,:]
df3_1 = df3.iloc[:int(x3), :]
df3_2 = df3.iloc[int(x3):,:]
df4_1 = df4.iloc[:int(x4), :]
df4_2 = df4.iloc[int(x4):,:]

#read the dataframes to two new csvs of half the size to ensure successful upload of the data to the database wihtout facing timeout issue
df0_1.to_csv("2014_01.csv", index=False, encoding='utf8')
df0_2.to_csv("2014_02.csv", index=False, encoding='utf8')
df1_1.to_csv("2015_01.csv", index=False, encoding='utf8')
df1_2.to_csv("2015_02.csv", index=False, encoding='utf8')
df2_1.to_csv("2016_01.csv", index=False, encoding='utf8')
df2_2.to_csv("2016_02.csv", index=False, encoding='utf8')
df3_1.to_csv("2017_01.csv", index=False, encoding='utf8')
df3_2.to_csv("2017_02.csv", index=False, encoding='utf8')
df4_1.to_csv("2018_01.csv", index=False, encoding='utf8')
df4_2.to_csv("2018_02.csv", index=False, encoding='utf8')