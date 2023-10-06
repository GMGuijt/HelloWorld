import pandas as pd

#pip install langdetect
#pip install textblob
#pip install nltk

from langdetect import detect
#import textblob as tb


df = pd.read_excel('tweets.xlsx')


def list_singular_entity(dataframe, column_name):
    enitities = []
    for i in range(dataframe):
        enitities.append(dataframe[column_name])
    return enitities
        


def detect_languages(dataframe, column_name):
    entities = list_singular_entity(dataframe, column_name)
    entity_language_dict = {'entity', 'language'}
    for i in entities:
        language = detect(i)
        entity_language_dict.append(language, i)
    df_entity_language = df(entity_language_dict)
    return df_entity_language

detect_languages(df, 'Tweet')

#def analyze_sentiment_english(entity):
   # subjectivity = TextBlob(entity).sentiment.subjectivity
    #polarity = TextBlob(entity).sentiment.polarity
    #if polarity < 0:
        #return 'negative'
    #if polarity > 0:
    #    return 'positive'
    #else:
    #    return 'neutral'
    
        
#def analyze_sentiment_other(entity):

       
#def detect_sentiments(df_entity_language):
#    sentiments = []
#    for i in range(len(df_entity_language))
#    entity_properties = df_entity_language[i]
#    if entity_properties[1] == 'en':
#        sentiment_entity = analyze_sentiment_english(entity_properties[0])
#        sentiment.append(sentiment_entity)
#    else:
#        sentiment_entity = analyze_sentiment_other(entity_properties[0])
#        sentiment.append(sentiment_entity)
#    df_entity_language['sentiment'] = sentiments
#    df_entity_language_sentiments = df_entity_language
#    return df_entity_language_sentiments
    
        