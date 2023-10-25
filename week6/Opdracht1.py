#✓   a) Copy the following code to your own script 
#✓   b) Split the data: Divide the dataset into a training set and a test set.
#✓   c) Plot the data (this code is already given) and look at the plot, determine which relationship exists between the variables and define one of the regression models learned in this course
#✓   d) Train the model: fit the model to the training data
#   e) Evaluated the trained model by the 𝑅2 and the 𝑀𝑆𝐸
#   f) Evaluate the model: Assess the performance of the trained model on the test data by the 𝑅2 and the 𝑀𝑆𝐸
#   g) Refine and iterate: If the model's performance is not satisfactory, you may need to choose a different model. Iterate this process until you are satisfied with the model's performance.


import numpy as np
import matplotlib.pyplot as plt
import math as m
import statsmodels.api as sm

#genereer dataset
def generate_data(a,b,c):
    np.random.seed(2)
    x = np.random.uniform(a,b,c)
    y = 2 * x**2 - 5 * x + 3 + np.random.normal(a,b,c)
    return x,y
size = 200
x,y = generate_data(0,10,size)

#split training en test data
def split(size, x, y, percentile):
    testsize = m.ceil(size/percentile)
    testx = []
    testy = []
    for i in range(testsize):
        testx.append(x[0])
        x = np.delete(x,0)
        testy.append(y[0])
        y = np.delete(y,0)
    return testx,x,testy,y
testx,trainingx,testy,trainingy = split(size,x,y,20)
test = [testx,testy]
training = [trainingx,trainingy]

# Fit de data
def regressionline(training):
    X = sm.add_constant(training[0])
    model = sm.OLS(training[1], X)
    results = model.fit()
    predictiony = results.predict(X)
    return predictiony

# Plot de dataset
def scatterplot(x,y):
    plt.scatter(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Dataset')
    plt.show()

# plot alles
def plot(training):
    lijn = regressionline(training)
    plt.plot(training[0],lijn,color='yellow')
    scatterplot(training[0],training[1])

plot(training)
