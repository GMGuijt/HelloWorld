import pandas as pd


df = pd.read_excel('week4\dataProject4.xlsx',1, header = 4)

#print(df.loc[:,'Postal Code':'1c. Brand name'])

def remove_empty(data):
    '''verwijder rijen waarvoor de totale inkoopheoveelheid 0 is'''
    ndf = df.copy
    data_only = data[data.loc[:,'HL':'HL.4'].sum(axis=1) == 0]
    for i in data_only.index:
        ndf.drop(i)
    return ndf

def remove_dupes(data):
    '''verwijder duplicate rijen'''
    for i in range(len(data)):
        for j in range(i+1,len(data)):
            if data[i].loc[:,'','HL.4']

def collapse_doubles(data):
    '''sommeer producten die tweemaal of vaker door dezelfde klant is gekocht'''


#def 

#ndf = remove_empty(df)
#print(len(df))
#print(len(ndf))
remove_dupes(range(6))

