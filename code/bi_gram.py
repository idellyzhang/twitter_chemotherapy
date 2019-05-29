from nltk.corpus import stopwords
import string
import codecs
import operator 
import json
from collections import Counter
from nltk.tokenize import word_tokenize
import re
import preprocessor as p
from nltk import bigrams
from nltk.util import ngrams

emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""
 
regex_str = [
    emoticons_str,
    r'<[^>]+>', # HTML tags
    r'(?:@[\w_]+)', # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs
 
    r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
    r'(?:[\w_]+)', # other words
    r'(?:\S)' # anything else
]
    
tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)
 
def tokenize(s):
    return tokens_re.findall(s)
 
def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens
 

count_all = Counter()
f = codecs.open("orgnization_chemo_tweets.txt", "r", errors='ignore') # encoding='utf-8',

for tweet in f:
    punctuation = list(string.punctuation)
    stop = stopwords.words('english') + punctuation + ['rt', 'via', 'I', 'RT', 'a','b','c','d','e','f','g','h','i',
                                                       'j','k','l','m','n','o','p','q','r','t','u','v','w','x','y','z', '0', '1',
                                                       '2','3','4','5','6','7','8','9', '13']#, 'Chemo', 'Chemotherapy', 'chemotherapy', 'chemo']
    #print(p.clean(tweet))
    tweet_r = re.sub(r'(\\x(.){2})', '',tweet.lower())
    terms_stop = [term for term in preprocess(tweet_r) if term.isalnum() and term not in stop and not term.startswith(('#', '@', 'http', 'nhttp', 'nhttps'))]
    terms_bigram = bigrams(terms_stop)
    #terms_trigram = ngrams(terms_stop, 3)
    count_all.update(terms_bigram)
print(count_all.most_common(100))



