import pandas as pd


df = pd.read_excel('week4\dataProject4.xlsx',1, header = 4)

#print(df.loc[:,'Postal Code':'1c. Brand name'])

def remove_empty(df):
    data_only = df[df.loc[:,'HL':'HL.4'].sum(axis=1) == 0]
    for i in data_only.index:
        df.drop(i)
    ndf = df
    return ndf



print(len(df))
ndf = remove_empty(df)
print(len(ndf))

