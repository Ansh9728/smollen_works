
# uncomment to use textblob for sentiment analysis
# from textblob import TextBlob

# def analyze_sentiment(text):
#     blob = TextBlob(text)
#     sentiment_score = blob.sentiment.polarity
    
#     if sentiment_score > 0:
#         return "Positive"
#     elif sentiment_score < 0:
#         return "Negative"
#     else:
#         return "Neutral"

# transformer for sentiment analysis
from transformers import pipeline

def analyze_sentiment(text):
    # Initialize the sentiment analysis pipeline
    sentiment_analyzer = pipeline("sentiment-analysis")
    result = sentiment_analyzer(text)
    # print(result)
    result = {
        "label": result[0]["label"],
        "score": result[0]["score"]
    }
    return result
    return ""

    