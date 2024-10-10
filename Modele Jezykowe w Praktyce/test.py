import statistics
import urllib.request
import re
url = "https://www.gutenberg.org/files/11/11-0.txt"
file_path = "alice.txt"
urllib.request.urlretrieve(url, file_path)
from collections import Counter


test = [1,2,-3,-4,5,-7,8,-9,21,-20,19,-18,6]

def zad1_AB(lista, sortByReverse):
    print("\nzadanie 1_AB")
    average = sum(lista) / len(lista)

    aboveAverage = []
    belowOrEqualAverage = []

    for x in lista:
        if(x > average):
            aboveAverage.append(x)
        if(x <= average):
            belowOrEqualAverage.append(x)

    aboveAverage.sort(reverse = sortByReverse)
    belowOrEqualAverage.sort(reverse = sortByReverse)

    print("srednia " , average)
    print("powyzej sredniej ", aboveAverage)
    print("ponizej lub rowne ", belowOrEqualAverage)

def zad1_C(lista):
    print("\nzadanie 1_C")
    print("mediana ", statistics.median(lista))
    print("odchylenie standardowe ", statistics.stdev(lista))

def zad2_AB(lista):
    print("\nzadanie 2_AB")
    lista2 = list(map(lambda x: abs(x) * 2, lista))
    print(lista2)

def zad2_CD(lista, prog):
    evenList = list(filter(lambda x: x%2 == 0 and x>prog, lista))
    print("parzyste ", evenList)
    oddList = list(filter(lambda x: x%2 == 1 and x>prog, lista))
    print("nieparzyste ", oddList)
    
def zad3(data):
    print("\nzadanie 3")
    
    words = data.split()
    print("ilosc słów ", len(words))

    chars = len(data)

    print("ilosc znaków ", chars)

    with open('summary', 'w', encoding="UTF-8") as file:
        file.write("words: ")
        file.write(str(len(words)))
        file.write("\nchars: ")
        file.write(str(chars))


def zad4(data):
    print("\nzadanie 4")
    # text = "Hello, world. This is a test."
    # tokens = re.findall(r'\w+|[^\w\s]', text)
    # print(tokens)
    tokens = re.findall(r'\w+|[^\w\s]', data)
    print(tokens[:30])
    startFromT = re.findall(r'\bT\w*', data)
    print(startFromT)
    return tokens
    
def zad5(tokens):
    print("\nzadanie 5")
    CountedWords = {}
    for token in tokens:
        if re.match(r'\w+', token):
            word = token.lower()
            if word in CountedWords:
                CountedWords[word] += 1
            else:
                CountedWords[word] = 1
    sorted_by_count = dict(sorted(CountedWords.items(), key=lambda item: item[1], reverse=True))

    for i, (word, count) in enumerate(sorted_by_count.items()):
        if i < 10:
            print(word , " ", count)
        else:
            break

def zad6(data):
    print("\nzadanie 6")
    splitted = data.split()
    print(splitted)
    longest = splitted[0]

    for s in splitted:
        if len(s) > len(longest):
            longest = s

    print("najdluzsze slowo: ", longest, " dlugosc: ", len(longest))
    
    
def zad7(data):
    print("\nzadanie 7")
    
    stopWords = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
    data = re.sub(r'[^\w\s]', '', data)
    splitted = data.split()
    filteredWords = [] 
    for word in splitted:
        if word.lower() not in stopWords:
            filteredWords.append(word.lower())
    
    cnt = Counter(filteredWords)

    print(cnt.most_common(10))


def zad8(data, n):
    print("\nzadanie 8")
    
    data = re.sub(r'[^\w\s]', '', data)
    tokens = data.split()

    ngrams = [tuple(tokens[i:i+n]) for i in range(len(tokens) - n + 1)]
    ngram_counts = Counter(ngrams)
    sorted_by_count = dict(sorted(ngram_counts.items(), key=lambda item: item[1], reverse=True))
    for i, (ngram, count) in enumerate(sorted_by_count.items()):
        if i < 10:
            print(ngram , " ", count)
        else:
            break
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def main():
    with open('alice.txt', 'r', encoding='UTF-8') as file:
        text = file.read()
    
    zad1_AB(test, True)
    zad1_C(test)
    zad2_AB(test)
    zad2_CD(test, 6)
    
    zad3(text)
    tokens = zad4(text)
    zad5(tokens)
    zad6(text)
    zad7(text)
    zad8(text, 2)
main()