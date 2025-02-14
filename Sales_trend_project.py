import pandas as pd
import matplotlib.pyplot as plt

def loadData(fileName):
    data = pd.read_csv(fileName)
    return data

def analyzeSales(data):
    maxSales = data['Sales'].max()
    minSales = data['Sales'].min()
    totalSales = data['Sales'].sum()
    averageSales = data['Sales'].mean()

    return maxSales, minSales, totalSales, averageSales

def plotSales(data):
    data['Date'] = pd.to_datetime(data['Date'])
    data.sort_values('Date', inplace = True)  # Sort by date and modify existing dataframe directly

    plt.plot(data['Date'], data['Sales'], marker = 'o', color = 'b')
    plt.xlabel('Date')
    plt.ylabel('Sales')
    plt.title('Sales Trends')
    plt.grid(True)
    
    plt.show()


def main():
    fileName = 'sales_data.csv'
    data = loadData(fileName)

    result = analyzeSales(data)
    
    maxVal = result[0]
    minVal = result[1]
    total = result[2]
    average = result[3]

    print("Max Sales: %d" % maxVal)
    print("Min Sales: %d" % minVal)
    print("Total sales: %d" % total)
    print("Average sales: %d" % average)

    plotSales(data)

main()










