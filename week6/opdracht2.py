import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from sklearn.metrics import r2_score

df = pd.read_csv("week6/homework data/winequality-red.csv") #data inladen

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
    """create a plot of the correlation between 2 lists of data

    Args:
        data (dataframe): dataframe you want to compare
        column_x (string): name of the column you want as explenation variable
        column_y (string): name of the column you want as explained variable
    """
    x_data = data[column_x]
    y_data = data[column_y]
    plt.bar(x_data, y_data)
    plt.xlabel(column_x)
    plt.ylabel(column_y)
    plt.show()

df = remove_duplicates(df) #duplicates verwijderen
headers = list(df.columns.values) #alle column namen uit de dataframe in een list zetten zodat er geen spelfouten kunnen optreden

for i in headers:
    show_correlation(df, i, headers[-1])

#create train and test dataset
df_train = df.iloc[:int((len(df)*80)/100)] #we willen de eerste 80% van de dataset gebruiken om te trainen 
df_test = df.iloc[int((len(df)*80)/100):] #we willen de laatste 20% van de dataset gebruiken om te testen 
df_test.reset_index() #dataset index reseten zodat er later geen problemen in de code kunnen voorkomen.


#model 1
print('model 1:')
X = sm.add_constant(df_train[headers[1]])  
model = sm.OLS(df_train[headers[-1]], X)
results = model.fit()
predicted_train_y = results.predict(X)
plt.scatter(df_train[headers[1]], df_train[headers[-1]])
plt.plot(df_train[headers[1]], predicted_train_y, color='red')
plt.xlabel('amount of volatile acidity in wine')
plt.ylabel('quality index of wine')
plt.title('Regression Model')
plt.show() #de correlatie laten zien
r_squared = results.rsquared #kijken hoeveel procent de dataset correct is 
print(r_squared)


#model 2
print()
print('model 2')
X = sm.add_constant(df_train[headers[4]])  
model = sm.OLS(df_train[headers[-1]], X)
results = model.fit()
predicted_train_y = results.predict(X)
plt.scatter(df_train[headers[4]], df_train[headers[-1]])
plt.plot(df_train[headers[4]], predicted_train_y, color='red')
plt.xlabel(headers[4])
plt.ylabel('quality index of wine')
plt.title('Regression Model')
plt.show()
r_squared = results.rsquared
print(r_squared)

print('the best model is ...')