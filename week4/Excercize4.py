import pandas as pd

#pip install langdetect
#pip install textblob
#pip install nltk

from langdetect import detect
import textblob as tb
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')

df = pd.read_excel(r"C:\Users\Gebruiker\Documents\school\DS\2_5\ds5_assignment_group7\week4\tweets.xlsx")
        
def analyze_sentiment_english(entity):
    polarity = tb.TextBlob(entity).sentiment.polarity
    if polarity < 0:
        return 'negative'
    if polarity > 0:
        return 'positive'
    else:
        return 'neutral'

def analyze_sentiment_other(entity):
    txt = SentimentIntensityAnalyzer()
    sentiment_scores = txt.polarity_scores(entity)
    if sentiment_scores['compound'] >= 0.05:
        return 'positve'
    elif sentiment_scores['compound'] <= -0.05:
        return 'negative'
    else:
        return 'neutral'

def detect_languages_sentiment(dataframe, column_name):
    entities = dataframe[column_name].values.tolist()
    languages = []
    sentiments = []S
    for i in entities:
        language = detect(i[1])
        languages.append(language)
        if language == 'en':
            sentiments.append(analyze_sentiment_english(i[1]))
        else:
            sentiments.append(analyze_sentiment_other(i[1]))
    properties_entities = list(zip(entities, languages, sentiments))        
    df_entity_language_sentiments = pd.DataFrame(properties_entities, columns=['entity', 'language', 'sentiment'])
    return df_entity_language_sentiments

df = detect_languages_sentiment(df, 'Tweet')
df.head()

        