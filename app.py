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








#read from the bitcoin price data (taken from Yahoo Finance)
yfdata = yf.download("BTC-USD", start = "2018-01-01", end = "2023-04-20", interval = "1d")
yfdata.to_csv("btcprice.csv")
btc_price_data = pd.read_csv('btcprice.csv',
                             index_col=False, 
                             low_memory=False,  
                             names=["Date", 
                                    "Open",
                                    "High",
                                    "Low",
                                    "Close",
                                    "Adj Close",
                                    "Volume"],
                                    skiprows=1)


#Analyze high data and low data
pricenumericdata = btc_price_data.astype({'High' : 'float', 'Low' : 'float'})
high_price_mean = pricenumericdata['High'].mean()
high_price_std = pricenumericdata['High'].std()
high_price_max = pricenumericdata['High'].max()
high_price_min = pricenumericdata['High'].min()
high_price_med = pricenumericdata['High'].median()

#Analyze Low data
low_price_mean = pricenumericdata['Low'].mean()
low_price_std = pricenumericdata['Low'].std()
low_price_max = pricenumericdata['Low'].max()
low_price_min = pricenumericdata['Low'].min()
low_price_med = pricenumericdata['Low'].median()



#print high data
#print("Average high price:", high_price_mean)
#print("High standard deviation:", high_price_std)
#print("High max price:", high_price_max)
#print("High min price:", high_price_min)
#print("Median high price:", high_price_med)

#print low data
#print("Average low price:", low_price_mean)
#print("Low standard deviation:", low_price_std)
#print("Low max price:", low_price_max)
#print("Low min price:", low_price_min)
#print("Median low price:", low_price_med)



#CLEAN YAHOO FINANCE DATA USING Z SCORE OF 3
btc_price_data['zscorehigh'] = (pricenumericdata.High - high_price_mean) / high_price_std
btc_price_data['zscorelow'] = (pricenumericdata.Low - low_price_mean) / low_price_std

#print(btc_price_data[btc_price_data['zscorehigh']>3])
#print(btc_price_data[btc_price_data['zscorehigh']<-3])

#print(btc_price_data[btc_price_data['zscorelow']>3])
#print(btc_price_data[btc_price_data['zscorelow']<-3])

btc_hprice_no_outliers = btc_price_data[(btc_price_data.zscorehigh < 3) & (btc_price_data.zscorehigh > -3)]
btc_lprice_no_outliers = btc_price_data[(btc_price_data.zscorelow < 3) & (btc_price_data.zscorelow > -3)]

cleaned_price_data_h = btc_hprice_no_outliers.astype({'High' : 'float'})
cleanhprice_mean = cleaned_price_data_h['High'].mean()
cleanhprice_std = cleaned_price_data_h['High'].std()
cleanhprice_min = cleaned_price_data_h['High'].min()
cleanhprice_max = cleaned_price_data_h['High'].max()
cleanhprice_med = cleaned_price_data_h['High'].median()


#print("Clean high price mean:", cleanhprice_mean)
#print("Clean high price std:", cleanhprice_std)
#print("Clean high price max:", cleanhprice_max)
#print("Clean high price min:", cleanhprice_min)
#print("Clean high price median:", cleanhprice_med)

cleaned_price_data_l = btc_lprice_no_outliers.astype({'Low' : 'float'})
cleanlprice_mean = cleaned_price_data_l['Low'].mean()
cleanlprice_std = cleaned_price_data_l['Low'].std()
cleanlprice_max = cleaned_price_data_l['Low'].max()
cleanlprice_min = cleaned_price_data_l['Low'].min()
cleanlprice_med = cleaned_price_data_l['Low'].median()

#print("Clean low price mean:", cleanlprice_mean)
#print("Clean low price std:", cleanlprice_std)
#print("Clean low price max:", cleanlprice_max)
#print("Clean low price min:", cleanlprice_min)
#print("Clean low price median:", cleanlprice_med)


#plt.plot(btc_hprice_no_outliers.index, btc_hprice_no_outliers.High)
#plt.ylabel('Price (high)')
#plt.xlabel('Days since 1/1/2018')
#plt.show()

#plt.plot(btc_lprice_no_outliers.index, btc_lprice_no_outliers.Low)
#plt.ylabel('Price (low)')
#plt.xlabel('Days since 1/1/2018')
#plt.show()






btc_high_only = pd.read_csv('btcprice.csv',
                            index_col=False,\
                            low_memory=False,
                            names=["Date", 
                                    "Open",
                                    "High",
                                    "Low",
                                    "Close",
                                    "Adj Close",
                                    "Volume"],
                            usecols=["High"],
                            skiprows=1
                            )
btc_high_only.insert(0, 'days', btc_high_only.index)
print(btc_high_only.head())





X = btc_high_only.iloc[:, 0].values.reshape(-1, 1)
Y = btc_high_only.iloc[:, 1].values.reshape(-1, 1)

model = LinearRegression()
model.fit(X, Y)



#plt.scatter(X, Y)
#plt.plot(X, Y_pred, color = 'red')
#plt.xlabel("Days Since 1/1/2018")
#plt.ylabel("Bitcoin Price (USD)")
#plt.title("Linear Regression Prediction (High)")
#plt.show()

pr = PolynomialFeatures(degree=4)
X_poly = pr.fit_transform(X)
pr.fit(X_poly, Y)
model2 = LinearRegression()
model2.fit(X_poly, Y)
plt.scatter(X, Y)
plt.xlabel("Days since 1/1/2018")
plt.ylabel("Bitcoin Price(USD)")
plt.title("Polynomial Regression Prediction (High)")
plt.scatter(X, model2.predict(X_poly))
#plt.show()

coeffecients = np.polyfit(btc_high_only.days, btc_high_only.High, 4)

predicted_y = np.polyval(coeffecients, btc_high_only.days)

SSE = np.sum((btc_high_only.High - predicted_y) ** 2)
SST = np.sum((btc_high_only.High - np.mean(btc_high_only.High)) ** 2)
R2 = 1 - (SSE / SST)
print("R-squared Value:", R2)


#X2 = sm.add_constant(X)
#est = sm.OLS(Y, X2)
#est2 = est.fit()
#print(est2.summary())
