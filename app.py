import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pickle as pk


btc_data = pd.read_csv('btc.csv', 
                       low_memory=False, 
                       thousands=',', 
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

vnumericdata = btc_data.astype({'Volume': 'float'})
vnewdata_mean = vnumericdata['Volume'].mean()
vnewdata_std = vnumericdata['Volume'].std()
vnewdata_max = vnumericdata['Volume'].max()
vnewdata_min = vnumericdata['Volume'].min()
vnewdata_median = vnumericdata['Volume'].median()

print('Volume mean:', vnewdata_mean)
print('Standard deviation:', vnewdata_std)
print('Max value:', vnewdata_max)
print('Min value:', vnewdata_min)
print('Median of Volume:', vnewdata_median)

snumericdata = btc_data.astype({'Size(B)' : 'float'})
snewdata_mean = snumericdata['Size(B)'].mean()
snewdata_std = snumericdata['Size(B)'].std()
snewdata_max = snumericdata['Size(B)'].max()
snewdata_min = snumericdata['Size(B)'].min()
snewdata_median = snumericdata['Size(B)'].median()

print('Size mean:', snewdata_mean)
print('Size standard deviation:', snewdata_std)
print('Size max value:', snewdata_max)
print('Size min value:', snewdata_min)
print('Size median:', snewdata_median)

btc_price_data = pd.read_csv('btcprice.csv', 
                             low_memory=False,  
                             names=["Date", 
                                    "Open",
                                    "High",
                                    "Low",
                                    "Close",
                                    "Adj Close",
                                    "Volume"])

