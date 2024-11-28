import math
import random
import matplotlib.pyplot as plt
import numpy as np

maxPointVal = 2
minPointVal = -2
biasVal = 1
resolution = 0.03
a = 3
l = 0.4

weights = []
weights.append(random.uniform(-1, 1))
weights.append(random.uniform(-1, 1))
random.shuffle(weights)

matrix = []
x_vals = []
y_vals = []
colors = []

def linear(x):
    return a * x

def prog_unipolar(x):
    if x >= 0:
         return 1
    if x < 0:
         return 0

def sigmoid_unipolar(x):
    return 1 / (1 + math.exp(-l * x))

def resetValues():
    x_vals.clear()
    y_vals.clear()
    colors.clear()
     
def showPlot(x_vals, y_vals, colors):
    plt.scatter(x_vals, y_vals, c=colors, s=10)
    plt.xlabel("x")
    plt.ylabel("y") 

def chooseColor(result, typeOfFunction):
    if(typeOfFunction == 0):     
        if result < -2:
            color = 'navy'
        elif -2 <= result < 0:
            color = 'blue'
        elif 0 <= result <= 2:
            color = 'green'
        else:
            color = 'red'
                
    if(typeOfFunction == 1):     
        if result == 1:
            color = 'red'
        elif result == 0:
            color = 'blue'
                
    if(typeOfFunction == 2):     
        if 0 <= result < 0.25:
            color = 'yellow'
        elif 0.25 <= result < 0.5:
            color = 'blue'
        elif 0.5 <= result < 0.75:
            color = 'green'
        elif 0.75 <= result <= 1:
            color = 'red'
    return color
    
def SimpleNeuron_Linear(IsBias, typeOfFunction):
    for i in np.arange(minPointVal, maxPointVal, resolution):
        for j in np.arange(minPointVal, maxPointVal, resolution):
            if(IsBias == True):
                if(typeOfFunction == 0):
                    result = linear(weights[0] * i + weights[1] * j + biasVal)
                if(typeOfFunction == 1):
                    result = prog_unipolar(weights[0] * i + weights[1] * j + biasVal)
                if(typeOfFunction == 2):
                    result = sigmoid_unipolar(weights[0] * i + weights[1] * j + biasVal)
                        
            else:
                if(typeOfFunction == 0):
                    result = linear(weights[0] * i + weights[1] * j)
                if(typeOfFunction == 1):
                    result = prog_unipolar(weights[0] * i + weights[1] * j)
                if(typeOfFunction == 2):
                    result = sigmoid_unipolar(weights[0] * i + weights[1] * j)
                
            color = 'white'
            color = chooseColor(result, typeOfFunction)
           

            x_vals.append(i)
            y_vals.append(j)
            colors.append(color)
    showPlot(x_vals, y_vals, colors)
    resetValues()
  
def main():
    #region SimpleNeuron
    plt.figure(figsize=(16, 8))
    plt.subplots_adjust(wspace = 0.2, hspace=0.5)
    plt.suptitle('Simple Neuron')
    plt.subplot(3, 2, 1) 
    plt.title("Bez Biasu")
    SimpleNeuron_Linear(False, 0)
    
    plt.subplot(3, 2, 2) 
    plt.title("Z Biasem")
    SimpleNeuron_Linear(True, 0)
    
    plt.subplot(3, 2, 3) 
    plt.title("Bez Biasu")
    SimpleNeuron_Linear(False, 1)
    
    plt.subplot(3, 2, 4) 
    plt.title("Z Biasem")
    SimpleNeuron_Linear(True, 1)
    
    plt.subplot(3, 2, 5) 
    plt.title("Bez Biasu")
    SimpleNeuron_Linear(False, 2)
    
    plt.subplot(3, 2, 6) 
    plt.title("Z Biasem")
    SimpleNeuron_Linear(True, 2)
    plt.show()
    #endregion

main()