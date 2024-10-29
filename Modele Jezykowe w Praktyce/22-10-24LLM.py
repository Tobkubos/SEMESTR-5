import statistics
import urllib.request
from collections import Counter
import nltk
from nltk.corpus import stopwords
#nltk.download('stopwords')

from wordcloud import WordCloud
import matplotlib.pyplot as plt

import re

def zad1():
    with open('alice.txt', 'r', encoding='UTF-8') as file:
        data = file.read()
        data.lower()
        data = re.sub(r'[^\w\s]', '', data)

        bigram = nltk.ngrams(data.split(),2)
        
        counter = Counter(bigram).most_common(10)
        print(counter)

        

def zad2():
    with open('alice.txt', 'r', encoding='UTF-8') as file:
        data = file.read()
        data = re.sub(r'[^\w\s]', '', data)
        words = data.split()
        
    stop_words = set(stopwords.words('english'))
    slownik = {}
    for word in words:
        word = word.lower()
        if word not in stop_words:
            dlugosc = len(word)
            if dlugosc in slownik:
                slownik[dlugosc] += 1
            else:
                slownik[dlugosc] = 1
    sortslownik = sorted(slownik.items())

    print(sortslownik)



def zad3():
    with open('alice.txt', 'r', encoding='UTF-8') as file:
        data = file.read()
        data = re.sub(r'[^\w\s]', '', data)
        words = data.split()
        
    stop_words = set(stopwords.words('english'))
    slownik = {}
    
    for word in words:
        word = word.lower()
        if word not in stop_words:
            if word in slownik:
                slownik[word] += 1
            else:
                slownik[word] = 1
             
        
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(slownik)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.show()


def zad4_Analyzer(text1, ngram):
     with open(text1, 'r', encoding='UTF-8') as file:
        data = file.read()
        sentences = data.split('. ')
        total = 0
        for sentence in sentences:
            total += len(sentence)
        
        average = total/len(sentences)
        
        
        
        words = data.split()

        subdata = data = re.sub(r'[^\w\s]', '', data)
        bigram = nltk.ngrams(subdata.split(),ngram)
        counter = Counter(bigram).most_common(5)
        

        print('\n', "slowa: ", len(words))
        print('\n',"srednia zdania: " ,average)
        print('\n', "top n-gramy ", counter)
        
def zad4(text1, text2, ngram):
    zad4_Analyzer(text1, ngram)
    zad4_Analyzer(text2, ngram)
    
    
def zad5():
    with open('text1.txt', 'r', encoding='UTF-8') as file:
        data = file.read()
        data = re.sub(r'[^\w\s]', '', data)
    words = data.split()
    
    stop_words = set(stopwords.words('english'))    
    
    filtered_words = [word.lower() for word in words if word.lower() not in stop_words]
    counter = Counter(filtered_words).most_common(10)
    
    print("TOP SŁOWA:", counter)
    

zad1()
zad2()
zad3()
zad4('text1.txt', 'text2.txt', 3)
zad5()

def t():

    x1 = [2,2,0,-2,-2,0,4]
    x2 = [1,2,6,10,0,0,-20]
    d =  [1,1,1,-1,-1,-1,-1]

    w = [0,0,0]
    y = 0

    modify = True  
    while(modify):
        modify = False
        for i in range(0,7):
            s = x1[i]*w[1] + x2[i] * w[2] + w[0]
            if s >= 0:
                y = 1
            else:
                y =-1
            
            if y != d[i]:
                modify = True
                w[0] = w[0] + d[i]
                w[1] = w[1] + d[i] * x1[i]
                w[2] = w[2] + d[i] * x2[i]
            print(d[i], "  ", y)
        print("\n")
    print(w)


#t()          
            
    
    
