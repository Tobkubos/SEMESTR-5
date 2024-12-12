import random
import math

learning_rate = 0.5
cMax = 200000
bias = 1
Error = 0
ErrorMax = 0.0001

w1 = [0]*6
w2 = [0]*3

weights = [random.uniform(-1, 1) for i in range(9)]
#print(weights)

p = [[-1,-1,1],
     [-1,1,1],
     [1,-1,1],
     [1,1,1]]

t = [0,1,1,0]

def f(x):
    return 1. / (1. + math.exp(-x))

def f_prim(x):
    sigmoid = 1. / (1. + math.exp(-x))
    return sigmoid * (1 - sigmoid)

def learn():
    for epoch in range(cMax):
        total_error = 0
        
        random_order = list(range(len(p)))
        random.shuffle(random_order)

        for o in random_order:
            #wyjscie neuronow warstwy 1
            net1 = sum(weights[i] * p[o][i] for i in range(3))
            net2 = sum(weights[i + 3] * p[o][i] for i in range(3))
            y1 = f(net1)
            y2 = f(net2)

            #wyjscie ostateczne z warstwy 2
            p2 = [y1, y2, bias]
            net = sum(weights[i + 6] * p2[i] for i in range(3))
            y = f(net)

            #sygnaly bledu
            d21 = (t[o] - y) * f_prim(net)
            d11 = d21 * weights[6] * f_prim(net1)
            d12 = d21 * weights[7] * f_prim(net2)

            # Aktualizacja wag
            for i in range(3):
                weights[i] += learning_rate * d11 * p[o][i]
                weights[i + 3] += learning_rate * d12 * p[o][i]
                weights[i + 6] += learning_rate * d21 * p2[i]

            #blad ostateczny
            total_error += (t[o] - y) ** 2 / 2

        if total_error < ErrorMax:
            return

def test():
    for i in range(len(p)):
        net1 = sum(weights[j] * p[i][j] for j in range(3))
        net2 = sum(weights[j + 3] * p[i][j] for j in range(3))
        y1 = f(net1)
        y2 = f(net2)

        p2 = [y1, y2, bias]
        net = sum(weights[j + 6] * p2[j] for j in range(3))
        y = f(net)

        print(f"Wejście: {p[i]} -> Oczekiwane: {t[i]} -> Otrzymane: {y}")

learn()
test()