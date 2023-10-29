import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from sklearn.metrics import r2_score

df = pd.read_csv("week6/homework data/winequality-red.csv")

def remove_duplicates(data):
    """romuve duplicates in data

    Args:
        data (pd_dataframe): data you want to checo
    Returns:
        dataframe: data without duplicates
    """
    data.drop_duplicates(keep='first',inplace=True)
    return data

def show_correlation(data, column_x, column_y):
    x_data = data[column_x]
    y_data = data[column_y]
    plt.bar(x_data, y_data)
    plt.xlabel(column_x)
    plt.ylabel(column_y)
    plt.show()

df = remove_duplicates(df)
headers = list(df.columns.values)
y_data = df[headers[-1]]

for i in headers:
    x_data = df[i]
    plt.scatter(x_data, y_data)
    plt.xlabel(i)
    plt.ylabel("quality")
    plt.show()




