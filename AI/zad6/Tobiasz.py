import random
import math

learning_rate = 0.5
cMax = 200000
bias = 1
Error = 0
ErrorMax = 0.0001

w1 = [0]*6
w2 = [0]*3

for i in range(6):
    w1[i] = random.uniform(-1, 1)
for i in range(3):
    w2[i] = random.uniform(-1, 1)
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
    for i in range(0,cMax):
        Error = 0
        random_order = list(range(len(p)))
        random.shuffle(random_order)
        for i in random_order:
            y11 = p[i][0]*w1[0] + p[i][1]*w1[2] + p[i][2]*w1[4]
            y12 = p[i][0]*w1[1] + p[i][1]*w1[3] + p[i][2]*w1[5]
            
            y21 = y11 * w2[0] + y12 * w2[1] + bias * w2[2]
            
            d21 = (t[i] - f(y21))*f_prim(y21)
            d11 = d21*w2[0]*f_prim(y11)
            d12 = d21*w2[1]*f_prim(y12)
            
            #wagi
            w1[0] += learning_rate*d11*p[i][0]
            w1[1] += learning_rate*d12*p[i][0]
            w1[2] += learning_rate*d11*p[i][1]
            w1[3] += learning_rate*d12*p[i][1]
            w1[4] += learning_rate*d11*p[i][2]
            w1[5] += learning_rate*d12*p[i][2]

            w2[0] += learning_rate*d21*f(y11)
            w2[1] += learning_rate*d21*f(y12)
            w2[2] += learning_rate*d21*bias
            
            #błędy
            Error += ((t[i] - y21)**2) / 2
            
        if(Error < ErrorMax):
            return
     
for i in range(len(p)):
        y11 = p[i][0]*w1[0] + p[i][1]*w1[2] + p[i][2]*w1[4]
        y12 = p[i][0]*w1[1] + p[i][1]*w1[3] + p[i][2]*w1[5]
        
        y21 = y11 * w2[0] + y12 * w2[1] + bias * w2[2]
        print(y21, "DLA ", p[i], " GDZIE ", t[i])