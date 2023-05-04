import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import statsmodels.api as sm
from sklearn.preprocessing import PolynomialFeatures


#read from prof zhangs data, using only data after 2018
btc_data = pd.read_csv('btc.csv', 
                       low_memory=False, 
                       thousands=',', 
                       index_col=False,
                       skiprows=501976, 
                       names=["Height", 
                              "Host", 
                              "Volume", 
                              "Stripped Size(B)", 
                              "Size(B)", "Weight", 
                              "Average Trans Fee_Per_transaction", 
                              "Block Reward 1", 
                              "BlocK Reward_Tips", 
                              "Time"])

#perform basic analysis of the volume
vnumericdata = btc_data.astype({'Volume': 'float'})
vnewdata_mean = vnumericdata['Volume'].mean()
vnewdata_std = vnumericdata['Volume'].std()
vnewdata_max = vnumericdata['Volume'].max()
vnewdata_min = vnumericdata['Volume'].min()
vnewdata_median = vnumericdata['Volume'].median()

#print the volume analysis information
#print('Volume mean:', vnewdata_mean)
#print('Standard deviation:', vnewdata_std)
#print('Max value:', vnewdata_max)
#print('Min value:', vnewdata_min)
#print('Median of Volume:', vnewdata_median)




#CLEAN PROF ZHANG DATA USING Z SCORE OF 3 
btc_data['zscore'] = (vnumericdata.Volume - vnewdata_mean) / vnewdata_std
#print(btc_data[btc_data['zscore']>3])
#print(btc_data[btc_data['zscore']<-3])
btc_data_no_outliers = btc_data[(btc_data.zscore < 3) & (btc_data.zscore > -3)]
cleaned_data = btc_data_no_outliers.astype({'Volume' : 'float'})
cleaned_data_mean = cleaned_data['Volume'].mean()
cleaned_data_std = cleaned_data['Volume'].std()
cleaned_data_max = cleaned_data['Volume'].max()
cleaned_data_min = cleaned_data['Volume'].min()
cleaned_data_med = cleaned_data['Volume'].median()

#print('Volume mean:', cleaned_data_mean)
#print('Standard deviation:', cleaned_data_std)
#print('Max value:', cleaned_data_max)
#print('Min value:', cleaned_data_min)
#print('Median of Volume:', cleaned_data_med)


#HOST DATA
btc_data_2018 = pd.read_csv('btc.csv', 
                       thousands=',', 
                       engine='python',
                       index_col=False,
                       skiprows=501976 ,
                       skipfooter= 110141,
                       names=["Height", 
                              "Host", 
                              "Volume", 
                              "Stripped Size(B)", 
                              "Size(B)", "Weight", 
                              "Average Trans Fee_Per_transaction", 
                              "Block Reward 1", 
                              "BlocK Reward_Tips", 
                              "Time"])
#print(btc_data_2018['Host'].value_counts()[:5])
#btc_data_2018['Host'].value_counts()[:5].plot(kind='barh', figsize = (8,6))
#btc_data_no_outliers['Host'].value_counts()[:5].plot(kind='barh', figsize=(8, 6))
#plt.xlabel("Count", labelpad=14)
#plt.ylabel("Host", labelpad=14)
#plt.title("Top Hosts for Mining Bitcoin 2018")
#plt.show()


btc_data_2019 = pd.read_csv('btc.csv', 
                       thousands=',', 
                       engine='python',
                       index_col=False,
                       skiprows=556475 ,
                       skipfooter= 55909,
                       names=["Height", 
                              "Host", 
                              "Volume", 
                              "Stripped Size(B)", 
                              "Size(B)", "Weight", 
                              "Average Trans Fee_Per_transaction", 
                              "Block Reward 1", 
                              "BlocK Reward_Tips", 
                              "Time"])
#print(btc_data_2019['Host'].value_counts()[:5])
#btc_data_2019['Host'].value_counts()[:5].plot(kind='barh', figsize = (8,6))
#plt.xlabel("Count", labelpad=14)
#plt.ylabel("Host", labelpad=14)
#plt.title("Top Hosts for Mining Bitcoin 2019")
#plt.show()


btc_data_2020_2021 = pd.read_csv('btc.csv', 
                       thousands=',', 
                       engine='python',
                       index_col=False,
                       skiprows=610708 ,
                       names=["Height", 
                              "Host", 
                              "Volume", 
                              "Stripped Size(B)", 
                              "Size(B)", "Weight", 
                              "Average Trans Fee_Per_transaction", 
                              "Block Reward 1", 
                              "BlocK Reward_Tips", 
                              "Time"])
#print(btc_data_2020_2021['Host'].value_counts()[:5])
btc_data_2020_2021['Host'].value_counts()[:5].plot(kind='barh', figsize = (8,6))
plt.xlabel("Count", labelpad=14)
plt.ylabel("Host", labelpad=14)
plt.title("Top Hosts for Mining Bitcoin 2020-2021")
#plt.show()


