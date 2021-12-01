#Purpose: This program visualizes your stock portfolio 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

from pypfopt.base_optimizer import portfolio_performance

#load the data
df = pd.read_excel(r"C:\Users\heywo\OneDrive - Queen's University\Python\Projects\data science\Portfolio Visualization\data.xlsx")
print(df)

#get the total invested amount of money in the portfolio
Portfolio_Total_per_ETF = df['Amount']*df['Average_Price']
df['ortfolio_Total_per_ETF'] = Portfolio_Total_per_ETF

Portfolio_Total_Amount = sum(df['Amount']* df['Average_Price'])
Portfolio_Total_Amount = round(Portfolio_Total_Amount, 2)
Portfolio_Total_Amount

#visually show the portfolio and some additional information
stock_tickers = df['Ticker'].values 
sizes = df['Amount'] * df['Average_Price']

listOfZeros = [0]*df.shape[0]
n = random.randint(0, df.shape[0]-1)
listOfZeros[n]=0.1
explode = listOfZeros

#create a figure
fig1, ax1 = plt.subplots(figsize=(10,10))
#plot the pie chart
ax1.pie(sizes,explode=explode, labels = stock_tickers, autopct ='%.2f%%',shadow = 'True',startangle=360)

#set the title
ax1.set_title("Portfolio Pie Chart", color = "Purple",fontsize = 22)

#Add text to the visual
x = -1.75
y=1
ax1.text(x,y,'Overview:',fontsize=24, color='Purple')

y_counter = 0.12
ax1.text(x,y-y_counter,'Total: $'+str(Portfolio_Total_Amount) , fontsize = 15, color ='Blue')
for i in range(0,df.shape[0]):
     ax1.text(x,0.88 - y_counter, df['Ticker'][i]+': $'+str(round(df['Average_Price'][i]*df['Amount'][i],2)),fontsize=14, color='Black')
     y_counter = y_counter + 0.12
plt.show()