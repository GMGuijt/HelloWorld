import pandas as pd

#pip install langdetect
#pip install textblob
#pip install nltk

from langdetect import detect
#import textblob as tb

df = pd.read_excel(r"C:\Users\Gebruiker\Documents\school\DS\2_5\ds5_assignment_group7\week4\tweets.xlsx")


def list_singular_entity(dataframe, column_name):
    enitities = []
    for i in range(len(dataframe)):
        enitities.append(dataframe[column_name])
    return enitities
        
def analyze_sentiment_english(entity):
    subjectivity = TextBlob(entity).sentiment.subjectivity
    polarity = TextBlob(entity).sentiment.polarity
    if polarity < 0:
        return 'negative'
    if polarity > 0:
        return 'positive'
    else:
        return 'neutral'

def analyze_sentiment_other(entity):

def detect_languages_sentiment(dataframe, column_name):
    entities = list_singular_entity(dataframe, column_name)
    languages = []
    sentiments = []
    for i in entities:
        language = detect(i[1])
        languages.append(language)
        if language == 'en':
            sentiments.append(analyze_sentiment_english(i[1]))
        else:
            sentiments.append(analyze_sentiment_other(i[1]))
    properties_entities = list(zip(entities, languages, sentiments))        
    df_entity_language_sentiments = pd.DataFrame(properties_entities, columns=['entity', 'language', 'sentiment'])
    return df_entity_language

df = detect_languages(df, 'Tweet')
df.head()

        