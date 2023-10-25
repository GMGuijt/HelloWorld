import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

np.random.seed(2)

x = np.random.uniform(0, 10, 200)
y = 2*x**2 - 5 * x + 3 + np.random.normal(0, 10, 200)

plt.scatter(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Dataset')

train_x = x[:160]
train_y = y[:160]

test_x = x[40:]
test_y = y[40:]

data_test = pd.DataFrame({
    'x' : test_x,
    'y' : test_y
})

plt.scatter(test_x,test_y)

X = sm.add_constant(data_test['x'])
Y = data_test['y']
model = sm.OLS(Y,X).fit()
predicted_Y = model.predict(X)
residuals = sum((predicted_Y - Y)**2)
R2 = 1 - residuals / sum((predicted_Y - np.mean(predicted_Y))**2)
MSE = residuals / (len(Y) - 2)
print(R2,MSE)

train_x = sm.add_constant(train_x)
predicted_Y = model.predict(train_x)
residuals = sum((predicted_Y - train_y)**2)
R2 = 1 - residuals / sum((predicted_Y - np.mean(predicted_Y))**2)
MSE = residuals / (len(train_y) - 2)
print(R2,MSE)