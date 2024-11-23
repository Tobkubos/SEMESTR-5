import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

Dirtness_of_clothes = ctrl.Antecedent(np.arange(0,100,1), 'Dirtness_of_clothes')
Type_of_dirt   = ctrl.Antecedent(np.arange(0,100,1), 'Type_of_dirt') 
Wash_time = ctrl.Consequent(np.arange(0, 60, 1), 'Wash_time')

Dirtness_of_clothes['small'] = fuzz.trimf(Dirtness_of_clothes.universe, [0, 0, 50])
Dirtness_of_clothes['medium'] = fuzz.trimf(Dirtness_of_clothes.universe, [0, 50, 100])
Dirtness_of_clothes['large'] = fuzz.trimf(Dirtness_of_clothes.universe, [50, 100, 100])

Type_of_dirt['not Greasy'] = fuzz.trimf(Type_of_dirt.universe, [0, 0, 50])
Type_of_dirt['medium'] = fuzz.trimf(Type_of_dirt.universe, [0, 50, 100])
Type_of_dirt['greasy'] = fuzz.trimf(Type_of_dirt.universe, [50, 100, 100])

Wash_time['VeryShort'] = fuzz.trimf(Wash_time.universe, [0, 8, 12])
Wash_time['Short'] = fuzz.trimf(Wash_time.universe, [8, 12, 20])
Wash_time['Medium'] = fuzz.trimf(Wash_time.universe, [12, 20, 40])
Wash_time['Long'] = fuzz.trimf(Wash_time.universe, [20, 40, 60])
Wash_time['VeryLong'] = fuzz.trimf(Wash_time.universe, [40, 60, 60])

rule1 = ctrl.Rule(Dirtness_of_clothes['large']  & Type_of_dirt['greasy'], Wash_time['VeryLong'])
rule2 = ctrl.Rule(Dirtness_of_clothes['medium'] & Type_of_dirt['greasy'], Wash_time['Long'])
rule3 = ctrl.Rule(Dirtness_of_clothes['small']  & Type_of_dirt['greasy'], Wash_time['Long'])
rule4 = ctrl.Rule(Dirtness_of_clothes['large']  & Type_of_dirt['medium'], Wash_time['Long'])
rule5 = ctrl.Rule(Dirtness_of_clothes['medium'] & Type_of_dirt['medium'], Wash_time['Medium'])
rule6 = ctrl.Rule(Dirtness_of_clothes['small']  & Type_of_dirt['medium'], Wash_time['Medium'])
rule7 = ctrl.Rule(Dirtness_of_clothes['large']  & Type_of_dirt['not Greasy'], Wash_time['Medium'])
rule8 = ctrl.Rule(Dirtness_of_clothes['medium'] & Type_of_dirt['not Greasy'], Wash_time['Short'])
rule9 = ctrl.Rule(Dirtness_of_clothes['small']  & Type_of_dirt['not Greasy'], Wash_time['VeryShort'])



washing_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9])
washing_sim = ctrl.ControlSystemSimulation(washing_ctrl)

x = np.arange(0, 101, 2)
y = np.arange(0, 101, 2)
X, Y = np.meshgrid(x, y)
Z = np.zeros_like(X)


for i in range(X.shape[0]):
    for j in range(X.shape[1]):
        print(i, " ", j, "\n");        
        washing_sim.input['Dirtness_of_clothes'] = X[i, j]
        washing_sim.input['Type_of_dirt'] = Y[i, j]
        washing_sim.compute()
        Z[i, j] = washing_sim.output['Wash_time']

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

surf = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='k')
ax.set_xlabel('Dirtness of Clothes')
ax.set_ylabel('Type of Dirt')
ax.set_zlabel('Wash Time')
ax.set_title('Wash Time Surface')

fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5)
plt.show()