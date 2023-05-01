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

btc_price_data = pd.read_csv('btcprice.csv', 
                             low_memory=False,  
                             names=["Date", 
                                    "Open",
                                    "High",
                                    "Low",
                                    "Close",
                                    "Adj Close",
                                    "Volume"],skiprows=1)

pricenumericdata_high = btc_price_data.astype({'High' : 'float'})
high_price_mean = pricenumericdata_high['High'].mean()
high_price_std = pricenumericdata_high['High'].std()
high_price_max = pricenumericdata_high['High'].max()
high_price_min = pricenumericdata_high['High'].min()
high_price_med = pricenumericdata_high['High'].median()


pricenumericdata_low = btc_price_data.astype({'Low' : 'float'})
low_price_mean = pricenumericdata_low['Low'].mean()
low_price_std = pricenumericdata_low['Low'].std()
low_price_max = pricenumericdata_low['Low'].max()
low_price_min = pricenumericdata_low['Low'].min()
low_price_med = pricenumericdata_low['Low'].median()


print("Average high price:", high_price_mean)
print("High standard deviation:", high_price_std)
print("High max price:", high_price_max)
print("High min price:", high_price_min)
print("Median high price:", high_price_med)


print("Average low price:", low_price_mean)
print("Low standard deviation:", low_price_std)
print("Low max price:", low_price_max)
print("Low min price:", low_price_min)
print("Median low price:", low_price_med)