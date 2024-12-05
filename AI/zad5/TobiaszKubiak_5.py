import random

w = [[0] * 7 for i in range(7)]  
    
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
    for epoch in range(200):
            randomQueue = list(range(7))
            random.shuffle(randomQueue)
            
            for i in randomQueue: 
                for j in range(7): 
                    input_sum = 0
                    for k in range(7):
                        input_sum += w[i][k] * test[k][j]
                    
                    test[i][j] = outputFunction(input_sum)
                    
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