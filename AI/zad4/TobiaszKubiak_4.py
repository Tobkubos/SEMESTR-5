import math
import random
import matplotlib.pyplot as plt
import numpy as np

maxPointVal = 2
minPointVal = -2
biasVal = 0.4
resolution = 0.01
a = 5
l = 1

weights = []
weights.append(random.uniform(-1, 1))
weights.append(random.uniform(-1, 1))
random.shuffle(weights)

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
    
def Neuron(IsBias, typeOfFunction):
    for i in np.arange(minPointVal, maxPointVal, resolution):
        for j in np.arange(minPointVal, maxPointVal, resolution):
            sum = weights[0] * i + weights[1] * j

            if(IsBias == True):
                if(typeOfFunction == 0):
                    result = linear(sum + biasVal)
                if(typeOfFunction == 1):
                    result = prog_unipolar(sum + biasVal)
                if(typeOfFunction == 2):
                    result = sigmoid_unipolar(sum + biasVal)
                        
            else:
                if(typeOfFunction == 0):
                    result = linear(sum)
                if(typeOfFunction == 1):
                    result = prog_unipolar(sum)
                if(typeOfFunction == 2):
                    result = sigmoid_unipolar(sum)
                
            color = 'white'
            color = chooseColor(result, typeOfFunction)
           

            x_vals.append(i)
            y_vals.append(j)
            colors.append(color)
    showPlot(x_vals, y_vals, colors)
    resetValues()
  
def NeuralNetwork(IsBias, typeOfFunction):
    for i in np.arange(minPointVal, maxPointVal, resolution):
        for j in np.arange(minPointVal, maxPointVal, resolution):
            sum = weights[0] * i + weights[1] * j
            

            if(IsBias == True):
                if(typeOfFunction == 0):
                    result = linear(linear(sum + biasVal)*weights[0] + linear(sum + biasVal)*weights[1] + biasVal)
                if(typeOfFunction == 1):
                    result = prog_unipolar(prog_unipolar(sum + biasVal)*weights[0] + prog_unipolar(sum + biasVal)*weights[1] + biasVal)
                if(typeOfFunction == 2):
                    result = sigmoid_unipolar(sigmoid_unipolar(sum + biasVal)*weights[0] + sigmoid_unipolar(sum + biasVal)*weights[1] + biasVal)
                        
            else:
                if(typeOfFunction == 0):
                    result = linear(linear(sum)*weights[0] + linear(sum)*weights[1])
                if(typeOfFunction == 1):
                    result = prog_unipolar(prog_unipolar(sum)*weights[0] + prog_unipolar(sum)*weights[1])
                if(typeOfFunction == 2):
                    result = sigmoid_unipolar(sigmoid_unipolar(sum)*weights[0] + sigmoid_unipolar(sum)*weights[1])
                
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
    plt.subplots_adjust(wspace = 1, hspace=0.5)
    plt.suptitle('Testowanie Neuronów/Sieci i różnych funkcji aktywacji')
    plt.subplot(3, 4, 1) 
    plt.title("Neuron - LINIOWA - Bez Biasu")
    Neuron(False, 0)
    
    plt.subplot(3, 4, 2) 
    plt.title("Neuron - LINIOWA - Z Biasem")
    Neuron(True, 0)
    
    plt.subplot(3, 4, 3) 
    plt.title("Neuron - PROGOWA UNIPOLARNA - Bez Biasu")
    Neuron(False, 1)
    
    plt.subplot(3, 4, 4) 
    plt.title("Neuron - PROGOWA UNIPOLARNA - Z Biasem")
    Neuron(True, 1)
    
    plt.subplot(3, 4, 5) 
    plt.title("Neuron - SIGMOIDALNA UNIPOLARNA - Bez Biasu")
    Neuron(False, 2)
    
    plt.subplot(3, 4, 6) 
    plt.title("Neuron - SIGMOIDALNA UNIPOLARNA - Z Biasem")
    Neuron(True, 2)
    #endregion

    #region NeuronNetwork
    plt.subplots_adjust(wspace = 0.4, hspace=0.5)
    plt.suptitle('Testowanie Neuronów/Sieci i różnych funkcji aktywacji')
    plt.subplot(3, 4, 7) 
    plt.title("Sieć - LINIOWA - Bez Biasu")
    NeuralNetwork(False, 0)
    
    plt.subplot(3, 4, 8) 
    plt.title("Sieć - LINIOWA - Z Biasem")
    NeuralNetwork(True, 0)
    
    plt.subplot(3, 4, 9) 
    plt.title("Sieć - PROGOWA UNIPOLARNA - Bez Biasu")
    NeuralNetwork(False, 1)
    
    plt.subplot(3, 4, 10) 
    plt.title("Sieć - PROGOWA UNIPOLARNA - Z Biasem")
    NeuralNetwork(True, 1)
    
    plt.subplot(3, 4, 11)
    plt.title("Sieć - SIGMOIDALNA UNIPOLARNA - Bez Biasu")
    NeuralNetwork(False, 2)
    
    plt.subplot(3, 4, 12) 
    plt.title("Sieć - SIGMOIDALNA UNIPOLARNA - Z Biasem")
    NeuralNetwork(True, 2)
    #endregion
    plt.show()

main()