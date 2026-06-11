from textblob import TextBlob

def analyze_sentiment(text):

    result = TextBlob(text).sentiment.polarity

    if result > 0:
        return "Positive"

    elif result < 0:
        return "Negative"

    else:
        return "Neutral"


text = input("Enter social media comment: ")

print(analyze_sentiment(text))