import pandas as pd
import numpy as np
import statsmodels.api
from sklearn.linear_model import LogisticRegression

prediction = pd.read_excel("week6/homework data/predictions_training.xlsx")
training = pd.read_excel("week6/homework data/training.xlsx")

def Opdracht3_1 (training,prediction):
    training['opp'] = (training['max_r']-training['min_r'])*(training['max_c']-training['min_c'])
    prediction['opp'] = (prediction['max_r']-prediction['min_r'])*(prediction['max_c']-prediction['min_c'])
    merge = pd.merge(training,prediction, left_index=True, right_index=True)
    merge['intercept'] = (merge[['max_r_x','max_r_y']].min(axis = 1) - merge[['min_r_x','min_r_y']].max(axis = 1)) *  (merge[['max_c_x','max_c_y']].min(axis = 1) - merge[['min_c_x','min_c_y']].max(axis = 1))
    merge.loc[merge['intercept'] < 0,'intercept'] = 0
    merge['union'] = merge['opp_x'] + merge['opp_y'] - merge['intercept']
    merge['IOU'] = merge['intercept']/merge['union']
    mean_IOU = np.mean(merge['IOU'])
    print(mean_IOU)
    return merge

def Opdracht3_2(training,merge):
    from sklearn.linear_model import LogisticRegression
    X = np.array(merge['IOU'])
    X = X.reshape(-1,1)
    y = training['category']
    model = LogisticRegression()
    model.fit(X, y)
    input = np.array(merge['IOU'])
    input = input.reshape(-1,1)
    predictions = model.predict(input)
    df = pd.DataFrame({
        'predictions' : predictions,
        'True' : training['category']
    })
    R2 = 1-sum((df['True'] - df.predictions)**2)/sum((df['True'] - np.mean(df['True']))**2)
    return R2

merge = Opdracht3_1(training,prediction)
R2 = Opdracht3_2(training,merge)