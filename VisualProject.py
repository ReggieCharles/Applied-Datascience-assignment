#importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

#importing bike sales file
bike = pd.read_csv('Sales.csv')

#Replace the gender column to show 'Male' & 'Female' instead of 'M' & 'F' for clearer identification
bike['Customer_Gender'].replace('M','Male', inplace = True)
bike['Customer_Gender'].replace('F','Female', inplace = True)


def calculate_profit_by_year(data):
    """"created a function to calculate the profit and group by the year"""
    
    grouped_data = data.groupby('Year')['Profit'].sum()
    return grouped_data

yearly_profit = calculate_profit_by_year(bike)
print(yearly_profit)

def create_lineplot(data):
    """Create a function to plot a line graph shwowing the 
    profit over the years"""
    
    plt.figure(figsize = (9.0, 6.0))
    plt.plot(data, linestyle = '-', color = 'black', label = 'Profit', marker = 'o', mfc = 'r', mec = 'black')
    plt.yticks(np.arange(2e6, 8e6, step = 5e5))
    plt.xlabel('year')
    plt.ylabel('profit(million)')
    plt.title('Profit Trend by Year')
    plt.legend()
    plt.show()
    return

create_lineplot(yearly_profit)

monthly_rev = [['January', 7005895, 2618521], 
         ['February', 6834583, 2562322], 
         ['March', 7347164, 2761866], 
         ['April', 7602750, 2864719], 
         ['May', 8836763, 3326937], 
         ['June', 9043008, 3383583], 
         ['July', 5721459, 2139750], 
         ['August', 5711193, 2214204], 
         ['September', 5841885, 2249661], 
         ['October', 5995079, 2301312], 
         ['November', 6244298, 2388513], 
         ['December', 9086931, 3409712]]

print(monthly_rev)

monthly_revenue = pd.DataFrame(data = monthly_rev,
                 columns=('Month','Revenue', 'Profit'))

def create_lineplot2(x1, x2, x3):
    """Create a function to plot a line graph shwowing the 
    total revenue & profit accrued over the month"""
    
    plt.figure(figsize = (12.0, 4.0))
    plt.plot(x1, x2, linestyle = '-', color = 'blue', label = 'Revenue', 
             marker = 'o', mfc = 'b', mec = 'black')
    plt.plot(x3, linestyle = '-', color = 'pink', label = 'Profit', 
             marker = 'o', mfc = 'r', mec = 'black')
    plt.yticks(np.arange(2e6, 10e6, step = 5e5))
    plt.xlabel('Months')
    plt.ylabel('Amount($)')
    plt.title('Profit & Revenue by Month')
    plt.legend()
    plt.savefig("lineplot.png")
    plt.show()
    
    return

create_lineplot2(monthly_revenue['Month'], monthly_revenue['Revenue'], 
                 monthly_revenue['Profit'])



P = bike.groupby('Product_Category').sum()['Profit'].sort_values(ascending = False)
print(P)

Ag_dist = bike['Age_Group'].value_counts().sort_values(ascending = False)

def pie(x1):
    x1.plot(kind = 'pie', shadow = False, cmap = 'PuRd', 
    autopct='%.0f%%',figsize = (10,5),title = 'Age Distribution',
    ylabel = ' ')
    plt.savefig("piechart.png")
    plt.show()
    return

pie(Ag_dist)

P = bike.groupby('Product_Category').sum()['Profit'].sort_values(ascending = False)
print(P)

def barchart(x1, x2):
    plt.figure(figsize = (6.0, 6.0))
    plt.bar(P.index, P, fc='purple', ec='black', alpha = 0.4)
    plt.title('Profit by Category')
    plt.xlabel('Product Category')
    plt.ylabel('Profit')
    plt.savefig("barchart.png")
    plt.show()
    return

barchart(P.index, P)