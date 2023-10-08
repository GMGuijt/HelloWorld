import pandas as pd


df = pd.read_excel('week4\dataProject4.xlsx',1, header = 4)

#print(df.loc[:,'Postal Code':'1c. Brand name'])

<<<<<<< HEAD
def remove_empty(df):
    ndf = df.copy()
    data_only = df[df.loc[:,'HL':'HL.4'].sum(axis=1) == 0]
    for i in data_only.index:
        df.drop(i)
=======
def remove_empty(data):
    '''verwijder rijen waarvoor de totale inkoopheoveelheid 0 is'''
    ndf = df.copy
    data_only = data[data.loc[:,'HL':'HL.4'].sum(axis=1) == 0]
    for i in data_only.index:
        ndf.drop(i)
>>>>>>> d39967629f80c11f60f84e410b0655cf7d4fc8c4
    return ndf

def remove_dupes(data):
    '''verwijder duplicate rijen'''
    remove = []
    for i in range(len(data)):
        for j in range(i+1,len(data)):
            if list(data.loc[i]) == list(data.loc[j]):
                remove.append(i)
            else:
                continue
    print(remove)

def collapse_doubles(data):
    '''sommeer producten die tweemaal of vaker door dezelfde klant is gekocht'''

<<<<<<< HEAD
re
print(len(df))
print(len(ndf))
=======
 

remove_dupes(df)

>>>>>>> d39967629f80c11f60f84e410b0655cf7d4fc8c4
