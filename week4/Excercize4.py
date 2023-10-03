import pandas as pd

#import textblob as tb



df = pd.read_excel('tweets.xlsx')


def list_singular_entity(dataframe, column_name):
    enitities = []
    for i in range(dataframe):
        enitities.append(dataframe[column_name])
    return enitities
        


def detect_languages(dataframe, column_name):
    entities = list_singular_entity(dataframe, column_name)
    entity_language_dict = {}
    for i in entities:
        language = tb.TextBlob(i)
        entity_language_dict.append(language, i)
    return entity_language_dict

detect_languages(df, 'Tweet')
    