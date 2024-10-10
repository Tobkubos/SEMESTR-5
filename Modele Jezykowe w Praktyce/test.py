import statistics
import urllib.request
import re
url = "https://www.gutenberg.org/files/11/11-0.txt"
file_path = "alice.txt"
urllib.request.urlretrieve(url, file_path)
from collections import Counter


test = [1,2,-3,-4,5,-7,8,-9,21,-20,19,-18,6]

def zad1(lista, sortByReverse):
    print("\nzadanie 1")
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

    print("mediana ", statistics.median(lista))
    print("odchylenie standardowe ", statistics.stdev(lista))


def zad2(lista, prog):
    print("\nzadanie 2")
    lista2 = list(map(lambda x: abs(x) * 2, lista))
    print(lista2)
    
    evenList = list(filter(lambda x: x%2 == 0 and x>prog, lista))
    print("parzyste ", evenList)
    oddList = list(filter(lambda x: x%2 == 1 and x>prog, lista))
    print("nieparzyste ", oddList)

def zad3():
    print("\nzadanie 3")
    with open('alice.txt', 'r', encoding='UTF-8') as file:
        data = file.read()
    
    words = data.split()
    print("ilosc słów ", len(words))

    chars = len(data)

    print("ilosc znaków ", chars)

    with open('summary', 'w', encoding="UTF-8") as file:
        file.write("words: ")
        file.write(str(len(words)))
        file.write("\nchars: ")
        file.write(str(chars))


def zad4():
    text = "Hello, world. This is a test."
    tokens = re.findall(r'\w+|[^\w\s]', text)
    print(tokens)
    with open('alice.txt', 'r', encoding='UTF-8') as file:
        data = file.read()
    tokens = re.findall(r'\w+|[^\w\s]', data)
    print(tokens[:30])
    
zad1(test,1)
zad2(test, 6)
zad3()
zad4()

