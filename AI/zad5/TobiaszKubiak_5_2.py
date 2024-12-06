import random
import numpy as np
    
patterns = [   
        [-1, 1, 1, 1,-1,
         -1, 1, 1, 1,-1,
          1,-1, 1,-1, 1,
          1, 1,-1, 1, 1,
          1,-1, 1,-1, 1,
         -1, 1, 1, 1,-1,
         -1, 1, 1, 1,-1],
         
        [-1,-1,-1,-1,-1,
         -1, 1, 1, 1,-1,
         -1, 1, 1, 1,-1,
         -1, 1, 1, 1,-1,
         -1, 1, 1, 1,-1,
         -1, 1, 1, 1,-1,
         -1,-1,-1,-1,-1],

        [-1, 1, 1, 1,-1,
         -1, 1, 1, 1,-1,
          1,-1, 1,-1, 1,
          1, 1,-1, 1, 1,
          1, 1,-1, 1, 1,
          1, 1,-1, 1, 1,
          1, 1,-1, 1, 1]
    ]

test = [
         -1, 1, 1, 1, 1,
         -1, 1, 1, 1, -1,
         1, 1, 1, 1, 1,
         1, 1, -1, 1, 1,
         1, 1, 1, 1, 1,
         1, 1, 1, 1, 1,
         -1, 1, 1, 1, -1
    ]
      

def CalcWeights():
    matrixSize = len(patterns[0])
    #print(matrixSize)
    w = np.zeros((matrixSize,matrixSize))
    for i in range(matrixSize):
        for j in range(matrixSize):
            for p in patterns:
                if i!= j:
                    w[i][j] += p[i] * p[j]

    #for i in range(len(w)):
        #print(w[i])
    
    output = test.copy()
    previous_output = output.copy()

    maxIterations = 10
    for i in range(maxIterations):
        randomOrder = list(range(matrixSize))
        random.shuffle(randomOrder)
        for i in randomOrder:
            net = 0
            for j in range(matrixSize):
                net += w[i][j] * output[j]
            output[i] = outputFunction(net)

        if np.array_equal(output, previous_output):
            break

        previous_output = output.copy()

        for i in range(35):
            if output[i] == 1:
                print(" ", end=' ')
            else:
                print("O", end=' ') 

            if (i + 1) % 5 == 0:
                print()
        print()

   
def outputFunction(net):
    if net >0:
        return 1
    if net == 0:
        return 0
    if net <0:
        return -1    
        
CalcWeights()