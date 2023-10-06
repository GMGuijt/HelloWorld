import pandas as pd
from datetime import datetime
def main():
    df = pd.read_excel("week4\hotelBookings.xlsx")
    df = clear4(df)
    df = clear5(df)
    df = clear8(df)
    df = clear9(df)
    df = clear10(df)
    df = clear11(df)
    df.to_excel('Clean_hotelBookings.xlsx')

def clear4(df):
    #vervang alle jaren hoger dan het huidig jaar door 2015, want dat is het enige jaar dat voorkomt
    nono = df[df.arrival_date_year > datetime.now().year].index
    df.loc[df.index.isin(nono),'arrival_date_year'] = 2015
    if len(df[df.arrival_date_year > datetime.now().year]) == 0:
        print("column arrival_date_year is clean")
        return df

def clear5(df):
    #vervang alle rijen die niet in de lijst met maanden komen door de maand july
    nono = df[~df.arrival_date_month.isin(['Januari','Februari','March','April','May','June','July','August','September','October','November','December'])].index
    df.loc[df.index.isin(nono),'arrival_date_month'] = 'July'
    if len(df[df.arrival_date_year > datetime.now().year]) == 0:
        print("column arrival_date_month is clean")
        return df
    
def clear8(df):
    #We verwijderen alle rijen waar de overnachtingen niet integer zijn, want aan die rijen kunnen we de data niet vertrouwen
    df.drop(df[df['stays_in_week_nights']%1 != 0].index,inplace = True)
    if len(df[df['stays_in_week_nights']%1 != 0]) == 0:
        print("column stays_in_week_nights is clean")
        return df

def clear9(df):
    df.drop(df[df['adults'] > 50].index,inplace = True)
    df.drop(df[df['children'] > 50].index,inplace = True)
    c = len(df[df['children'] > 50]) == 0
    a = len(df[df['adults'] > 50]) == 0
    if c and a:
        print("columns adults and children are clean")
        return df

def clear10(df):
    df.reset_index(inplace = True)
    df.drop('index',axis = 1,inplace = True)
    print(df[df.meal.index == 19]['meal'])
    for i in range(len(df)):
        if len(df.loc[i,'meal']) != 2:
            df.loc[i,'meal'] = df.loc[i,'meal'].replace(' ','')
    print('column meal is clean')
    return df

def clear11(df):
    for i in range(len(df)):
        if type(df.loc[i,'country']) == int:
            df.loc[i,'country'] = None
        elif type(df.loc[i,'country']) == float:
            df.loc[i,'country'] = None
            continue
        elif df.loc[i,'country'] == None:
            'Okay'
        elif len(df.loc[i,'country']) != 2:
            df.loc[i,'country'] = df.loc[i,'country'].replace(' ','')
    print('column country is clean')
    return df

main()