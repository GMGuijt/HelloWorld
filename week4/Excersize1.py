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
    remove = []
    for i in range(len(data)):
        for j in range(i+1,len(data)):
            #if data[i].loc[:,'','HL.4'] == data[j].loc[:,'','HL.4']:
            if data.iloc[i] == data.iloc[j]:
                remove.append(i)
            else:
                continue
    print(remove)

def collapse_doubles(data):
    '''sommeer producten die tweemaal of vaker door dezelfde klant is gekocht'''

 
lijst = list(range(7))
lijst.append(4)
lijst.append(3)
lijst.append(6)
data = pd.DataFrame(lijst)
#ndf = remove_empty(df)
#print(len(df))
#print(len(ndf))
print(data)
#remove_dupes(data)
print(data.iloc[4])
print(data.iloc[7])
if data.iloc[4] == data.iloc[7]:
    print(True)
else:
    print(False)


