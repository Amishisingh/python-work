from textblob import TextBlob
text=input("enter text")
blob=TextBlob(text)
sentiment=blob.sentiment.polarity
if sentiment>0:
    print("positive")
elif sentiment<0:
    print("negitive")
else:
    print("neutral")
