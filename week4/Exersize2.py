import pandas as pd
import datetime
df = pd.read_excel("week4\hotelBookings.xlsx")

def clean_4(df):
    #vervang alle jaren hoger dan het huidig jaar door 2015, want dat is het enige jaar dat voorkomt
    nono = df[df.arrival_date_year > datetime.now().year].index
    df.loc[df.index.isin(nono),'arrival_date_year'] = 2015
    if len(df[df.arrival_date_year > datetime.now().year]) == 0:
        print("column arrival_date_year is clean")
        return df
def clean_5(df):
    #vervang alle rijen die niet in de lijst met maanden komen door de maand july
    nono = df[~df.arrival_date_month.isin(['Januari','Februari','March','April','May','June','July','August','September','October','November','December'])].index
    df.loc[df.index.isin(nono),'arrival_date_month'] = 'July'
    if len(df[df.arrival_date_year > datetime.now().year]) == 0:
        print("column arrival_date_month is clean")
        return df
    
def clear8(df):
    #We verwijderen alle rijen waar de overnachtingen niet integer zijn, want aan die rijen kunnen we de data niet vertrouwen
    df = df.drop(df[df['stays_in_week_nights']%1 != 0].index)
    if len(df[df['stays_in_week_nights']%1 != 0]):
        print("column stays_in_week_nights is clean")
        return df

def clear9(df):
    df = df.drop(df[df['adults'] > 50].index)
    df = df.drop(df[df['children'] > 50].index)
    if len(df[df['children'] > 50]) == 0 and len(df[df['adults'] > 50]) == 0:
        print("columns adults and children are clean")

