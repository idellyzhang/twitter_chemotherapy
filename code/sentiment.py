import re
import codecs
from textblob import TextBlob
 

 
def clean_tweet(tweet):
        '''
        Utility function to clean tweet text by removing links, special characters
        using simple regex statements.
        '''
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])(\w+:\/\/\S+)", " ", tweet).split())
 
def get_tweet_sentiment(tweet):
        '''
        Utility function to classify sentiment of passed tweet
        using textblob's sentiment method
        '''
        analysis = TextBlob(clean_tweet(tweet))
        # set sentiment
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'

f = codecs.open("per_hairloss_tweets.txt", "r", encoding='utf-8', errors='ignore')
positive = []
neural = []
negative = []
for tweet in f:
    sent = get_tweet_sentiment(tweet)
    if(sent =='positive'):
        positive.append(sent)
    elif(sent =='negative'):
        negative.append(sent)
    else:
        neural.append(sent)

print("Positive tweets percentage: {} %".format(100*len(positive)/(len(positive)+len(negative)+len(neural))))
print("Negative tweets percentage: {} %".format(100*len(negative)/(len(positive)+len(negative)+len(neural))))
print("Neural tweets percentage: {} %".format(100*len(neural)/(len(positive)+len(negative)+len(neural))))

 
