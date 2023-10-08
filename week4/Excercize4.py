#pip install langdetect
#pip install textblob
#pip install nltk

import pandas as pd
from langdetect import detect
import textblob as tb
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')

twitter_df = pd.read_excel(r"C:\Users\Gebruiker\Documents\school\DS\2_5\ds5_assignment_group7\week4\tweets.xlsx")
        
def analyze_sentiment_english(entity):
    """uses the polarity of Textblob sentiment detection to calculate the sentiment of the entered entity
    
    Args:
        entity (string): text that will be analysed

    Returns:
        string: sentiment of text, 'negative' 'positive' 'neutral'
    """
    polarity = tb.TextBlob(entity).sentiment.polarity
    if polarity < 0:
        return 'negative'
    if polarity > 0:
        return 'positive'
    else:
        return 'neutral'

def analyze_sentiment_other(entity):
    """analyzes the sentiment of the entered entity regardless of language using nltk vader.

    Args:
        entity (string): text that will be analysed

    Returns:
        string: sentiment of text, 'negative' 'positive' 'neutral'
    """
    txt = SentimentIntensityAnalyzer()
    sentiment_scores = txt.polarity_scores(entity)
    if sentiment_scores['compound'] >= 0.05:
        return 'positive'
    elif sentiment_scores['compound'] <= -0.05:
        return 'negative'
    else:
        return 'neutral'


def detect_languages_sentiment(dataframe, column_name):
    """detects the language and sentiment from all the entities in a particual column.

    Args:
        dataframe (pandas dataframe): data with the entities
        column_name (string): name of the column containing the entities 

    Returns:
        pandas dataframe: dataframe with the entity, language and sentiment of the entered column
    """
    entities = dataframe[column_name].values.tolist()
    data =[]
    for i in entities:
        itteration = [i]
        try:
            language = detect(i)
        except:
            language = 'None'       
        itteration.append(language)
        if language == 'en':
            itteration.append(analyze_sentiment_english(i))
        elif language == 'None':
            itteration.append('None')
        else:
            itteration.append(analyze_sentiment_other(i))
        data.append(itteration)      
    df_entity_language_sentiments = pd.DataFrame(data, columns=['entity', 'language', 'sentiment'])
    return df_entity_language_sentiments

df = detect_languages_sentiment(twitter_df, 'Tweet')
print(df.head(10))