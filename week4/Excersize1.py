import pandas as pd

def remove_empty(data):
    '''verwijder rijen waarvoor de totale inkoopheoveelheid 0 is'''
    ndf = df.copy
    data_only = data[data.loc[:,'HL':'HL.4'].sum(axis=1) == 0]
    for i in data_only.index:
        ndf.drop(i)
    return ndf

def remove_dupes(data):
    '''verwijder duplicate rijen'''
    data.drop_duplicates(keep='first',inplace=True)
    return data

def collapse_doubles(data):
    '''sommeer producten die tweemaal of vaker door dezelfde klant is gekocht'''
    ndf = data.groupby(['2f. Customer number','Postal Code	Customer Classification (CRM)','Horeca menu webshop','Prd. name Webshop	1c.','Brand name','Contents']).sum().reset_index()
    return ndf

def main(df):
    df = pd.read_excel('week4\dataProject4.xlsx',1, header = 4)
    df = remove_empty(df)
    df = remove_dupes(df)
    df = collapse_doubles(df)
    return df
