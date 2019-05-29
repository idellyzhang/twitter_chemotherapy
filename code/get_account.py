import tweepy
import time
import csv
from nltk.tokenize import sent_tokenize, word_tokenize

key1 = "XXXXX"
key2 = "XXXXX"
key3 = "XXXXX"
key4 = "XXXXXX"

accountvar = input("Account name: ")

auth = tweepy.OAuthHandler(key1, key2)
auth.set_access_token(key3, key4)

api = tweepy.API(auth, wait_on_rate_limit=True) #, wait_on_rate_limit=True

users = tweepy.Cursor(api.followers, screen_name=accountvar).items()

while True:
    try:
        user = next(users)
    except tweepy.TweepError:
        print("My god, I have no enough time")
        time.sleep(60*15)
        print ("wake up")
        user = next(users)
    except StopIteration:
        break
    
    sentence = sent_tokenize(user.description)
    words = word_tokenize(user.description)

    
    if ( 'cancer' in words or 'tumor' in words or 'leukemia' in words or 'lymphoma' in words or 'cholangiocarcinoma' in words
                                      or 'myeloma' in words):
        print ("@" + user.screen_name)
        print ("#" + user.description)
        print ("friends: ",  user.friends_count)
        print ("statuses: " , user.statuses_count)
        print ( user.created_at)                      
        print ("lists: " , user.listed_count)
        print ("name: " + user.name)
        print ("id: " , user.id)
        print ("location: " + user.location)
        print ("favourites: " , user.favourites_count)
        print ("followers: " , user.followers_count)
        print ("Found Time : %s" % time.ctime())
        print ("------------------------------------------------------")

    
      
        
    