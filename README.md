# twitter_chemotherapy
Using data from social media to analyze cancer treatment
## Installation
```
pip install tweepy
```
## Create acc ess token
```
import tweepy

CONSUMER_KEY = 'your_consumer_key'
CONSUMER_SECRET = 'your_consumer_secret'
ACCESS_TOKEN = 'your_access_token'
ACCESS_TOKEN_SECRET = 'your_access_token_secret'
```

## Description about codes
```
Cowo.jar -- Co-occurence network
bi_gram.py -- n-gram analysis
extract_tweets.py -- download tweets based on Twitter accounts
get_account.py -- getting Twitter's accounts based on keywords in their description
sentiment.py -- sentiment analysis (positive, negative, neural)
topic_modelr.py -- topic model 
```
