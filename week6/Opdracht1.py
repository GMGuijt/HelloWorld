#✓   a) Copy the following code to your own script 
#✓   b) Split the data: Divide the dataset into a training set and a test set.
#✓   c) Plot the data (this code is already given) and look at the plot, determine which relationship exists between the variables and define one of the regression models learned in this course
#✓   d) Train the model: fit the model to the training data
#   e) Evaluated the trained model by the 𝑅2 and the 𝑀𝑆𝐸
#   f) Evaluate the model: Assess the performance of the trained model on the test data by the 𝑅2 and the 𝑀𝑆𝐸
#   g) Refine and iterate: If the model's performance is not satisfactory, you may need to choose a different model. Iterate this process until you are satisfied with the model's performance.


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math as m
import statsmodels.api as sm
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split


#genereer dataset
def generate_data(a,b,c):
    np.random.seed(2)
    x1 = np.random.uniform(a,b,c)
    y1 = 2 * x1**2 - 5 * x1 + 3 + np.random.normal(a,b,c)
    x = x1.tolist()
    y = y1.tolist()
    return x,y
size = 200
x,y = generate_data(0,10,size)

#split training en test data
def split(x, y, percentile):
    trainx, testx, trainy, testy = train_test_split(x,y,test_size=percentile, random_state=42)
    training = {
        'x': trainx,
        'y': trainy
    }
    train = pd.DataFrame(training)

    testing = {
        'x': testx,
        'y': testy
    }
    test = pd.DataFrame(testing)
    return train, test
train, test = split(x,y,0.2)

# voeg meer polynomiale termen toe
def polynomify(train):
    trainx = train['x']
    trainx2 = train['x']**2
    #trainx3 = train['x']**3
    #trainx4 = train['x']**4
    trainXpoly = pd.concat([trainx, trainx2], axis = 1)

    testx = test['x']
    testx2 = test['x']**2
    #testx3 = test['x']**3
    #testx4 = test['x']**4
    testXpoly = pd.concat([testx, testx2], axis = 1)
    return trainXpoly, testXpoly
trainXpoly, testXpoly = polynomify(train)


# Fit de data
def regressionline(train):
    X = sm.add_constant(trainXpoly)
    model = sm.OLS(train['y'], X)
    results = model.fit()
    return X,results
X,results = regressionline(train)
lijn = results.predict(X)

# evalueer test data
def testline(testXpoly, results):
    Xtest = sm.add_constant(testXpoly)
    predictedYtest = results.predict(Xtest)
    return predictedYtest

# Evalueer data
def eval(results, test):
    r2training = results.rsquared
    
    pred = testline(testXpoly, results)
    r2test = r2_score(test['y'],pred)
    
    print(r2training)
    print(r2test)

    if r2test >= r2training:
        print('goede fit')
    else:
        print('kies een ander model')

# Plot de dataset
def scatterplot(x,y):
    plt.scatter(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Dataset')
    plt.show()

# plot alles
def plot(train, test, lijn):
    plt.scatter(train['x'],lijn,color='red')
    scatterplot(train['x'],train['y'])

    plt.scatter(train['x'],lijn,color='red')
    scatterplot(test['x'],test['y'])

eval(results, test)
plot(train, test, lijn)

