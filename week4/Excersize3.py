import pandas as pd

def SalesRaport(RetailData):
    Sales_Category = RetailData.groupby('Category').sum('Sales')
    Sales_Category['Percentage'] = Sales_Category['Sales'] / sum(RetailData['Sales']) * 100
    Sales_Month = RetailData.groupby('Month').sum('Sales')
    Sales_Month['Percentage'] = Sales_Month['Sales']/sum(RetailData['Sales']) * 100
    Sales_manager = RetailData.groupby('Sales Manager').sum('Sales')
    Sales_manager['Percentage'] = Sales_manager['Sales']/sum(RetailData['Sales']) * 100
    return Sales_Category, Sales_Month, Sales_manager
RetailData = pd.read_excel('week4/detailedRetail.xlsx')
Sales_Category, Sales_Month, Sales_manager = SalesRaport(RetailData)
print(Sales_Category, Sales_Month, Sales_manager)