import random
import numpy as np

w = np.zeros((7,7)) 
    
p = [   
    [
        [1,-1, 1, 1, 1,-1, 1],
        [1,-1, 1, 1, 1,-1, 1],
        [1, 1,-1, 1,-1, 1, 1],
        [1, 1, 1,-1, 1, 1, 1],
        [1, 1,-1, 1,-1, 1, 1],
        [1,-1, 1, 1, 1,-1, 1],
        [1,-1, 1, 1, 1,-1, 1]
    ],
    [
        [1,-1,-1,-1,-1,-1, 1],
        [1,-1, 1, 1, 1,-1, 1],
        [1,-1, 1, 1, 1,-1, 1],
        [1,-1, 1, 1, 1,-1, 1],
        [1,-1, 1, 1, 1,-1, 1],
        [1,-1, 1, 1, 1,-1, 1],
        [1,-1,-1,-1,-1,-1, 1]
    ]
    ]

test = [
        [1,-1, 1, 1, 1, -1, 1],
        [1,-1, 1, 1, 1,-1, 1],
        [1, 1, 1, 1,-1, 1, 1],
        [1, 1, 1,-1, 1, 1, 1],
        [1, 1,-1, 1,-1, 1, 1],
        [1, 1, 1, 1, 1,-1, 1],
        [1,-1, 1, 1, 1, -1, 1]
    ]
      
      
def Kronecker(i,j):
    if i==j:
        return 1
    else:
        return 0


def CalculateWeights(): 
    for i in range(7):
        for j in range(7):
            sum = 0
            for k in range(len(p)):
                sum += p[k][i][j] 
            w[i][j] = ((1 - Kronecker(i, j)) * sum)
    for i in range(len(w)):
        print(w[i])

    
def learn():
    print('\n')
    for epoch in range(10):
            randomQueue1 = list(range(7))
            randomQueue2 = list(range(7))
            random.shuffle(randomQueue1)
            random.shuffle(randomQueue2)
            
            randomNeuron = [(i, j) for i in range(7) for j in range(7)]
            for i, j in randomNeuron:
                net_input = 0
                for k in range(7):
                    for l in range(7):
                        if (i, j) != (k, l):
                            net_input += w[i][j] * test[k][l]
                new_state = outputFunction(net_input)
                test[i][j] = new_state
                    
            print(epoch+1, " EPOKA")
            for row in test:
                print(row)
            print('\n')
        
    
def outputFunction(net):
    if net >0:
        return 1
    if net == 0:
        return 0
    if net <0:
        return -1    
        
CalculateWeights()
learn()