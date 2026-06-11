def predict_trend(hashtag):

    trends=[
        "High engagement expected",
        "Growing popularity",
        "Low engagement"
    ]

    return trends[0]


tag=input("Enter hashtag:")

print(predict_trend(tag))