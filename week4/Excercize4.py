import pandas as pd

pip install langdetect
pip install textblob

from langdetect import detect
import textblob as tb


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
        language = detect(i)
        entity_language_dict.append(language, i)
    return entity_language_dict

detect_languages(df, 'Tweet')

def analyze_sentiment_english(entity):
        
   
def detect_sentiments(language_dict):
    language_dict 
    entity_sentiment_dict = {}
    for i in entities: 
        analyze_sentiment_english(entity)    
    