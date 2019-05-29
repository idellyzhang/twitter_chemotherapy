import re
import csv
from nltk.tokenize import sent_tokenize, word_tokenize
import codecs


#def search(word, sentences):
 #      return [i for i in sentences if re.search(r'\b%s\b' % word, i)]
    

with codecs.open("professional_account_all.csv", "r", encoding='utf-8', errors='ignore') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        #if(('chemotherapy' in row['text'].lower() or 'chemo' in row['text'].lower()) and ('headache' in row['text'].lower() or 'fatigue' in row['text'].lower() or
        #                                                                                 'weakness' in row['text'].lower() or 'hair loss' in row['text'].lower() or
        #                                                                                 'alopecia' in row['text'].lower()
        #                                                                                  or 'nausea' in row['text'].lower() or 'vomiting' in row['text'].lower() or
        #                                                                                  'diarrhea' in row['text'].lower() or 'cramps' in row['text'].lower() or
        #                                                                                  'insomnia' in row['text'].lower() or 'mouth sores' in row['text'].lower()
        #                                                                                  or 'dry mouth' in row['text'].lower()
        #                                                                                  or 'Neuropathy' in row['text'].lower() or 
        #                                                                                  'constipation' in row['text'].lower() or 'anemia' in row['text'].lower() or
        #                                                                                  'numbness' in row['text'].lower() or 'lymphedema' in row['text'].lower())):
        if(('chemotherapy' in row['Description'].lower() or 'chemo' in row['Description'].lower()) and 'surgery' in row['Description'].lower()): # or ('womb' in row['Description'].lower())): #or ('lymphoma' in row['Description'].lower())): #or 'chemo' in row['text'].lower()) and ('weakness' in row['text'].lower())):# or 'radiation' in row['text'].lower() or
        #                rapy                                                                 # 'hormone therapy' in row['text'].lower())):
            print(row['Description'])
