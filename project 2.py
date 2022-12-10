import time
import random
import matplotlib.pyplot as plt
import numpy as np

from codes.rod_cut_iteractive import RodCutIteractive
from codes.rod_cut_recursive import RodCutRecursive

# Unit Test (Demonstration)
P = [1, 5, 8, 9] # 2 2
P = [2, 3, 7, 5] # 1 3
P = [2, 3, 7, 50] # 4
P = [20, 3, 7, 50] # 1 1 1 1

print("")
ex = RodCutIteractive.cutRod(P, len(P))
print("Custo Iterativo: " + str(ex[0]))
print("Tamanhos das barras: ", end="")
RodCutIteractive.showCut(ex[1], len(P))

print("")

ex = RodCutRecursive.cutRod(P, len(P))
print("Custo Recursivo: " + str(ex[0]))
print("Tamanhos das barras: ", end="")
RodCutRecursive.showCut(ex[1], len(P))
print("")

# Variables
amountArraySize = 10
listSet = []

# List size array (n)
listSizeArray = []
for i in range(amountArraySize):
    listSizeArray.append(random.randrange(10, 900 + 1)) # Array size: 10 ≤ n ≤ 1.000

listSizeArray = sorted(listSizeArray)
# listSizeArray = [10, 40, 80, 100, 150, 250, 400, 650, 850, 900]
# listSizeArray = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# listSizeArray = [100, 200, 300, 400, 500, 600, 700, 800, 850, 900]

# Generate total execution (m)
executions = []
for n in listSizeArray:
    m = 10
    executions.append([n, m])

# Generate lists
for execution in executions:
    listExecutions = []
    for m in range(execution[1]):
        list = []
        for n in range(execution[0]):
            list.append(random.uniform(1, n + 1)) # Array element: 1 ≤ A[i] ≤ n
        
        random.shuffle(list)
        listExecutions.append(list)
    listSet.append(listExecutions)

# Test: Rod Cut Iteractive
iteractiveTimes = []
for lists in listSet:
    totalTime = 0
    for list in lists:
        # Rod Cut Iteractive
        P = list.copy()
        begin = time.time()
        RodCutIteractive.cutRod(P, len(P))
        end = time.time()
        totalTime += (end - begin)

    iteractiveTimes.append(totalTime / len(lists))

# Test: Rod Cut Recursive 
recursiveTimes = []
for lists in listSet:
    totalTime = 0
    for list in lists:
        # Rod Cut Recursive Test
        P = list.copy()
        begin = time.time()
        RodCutRecursive.cutRod(P, len(P))
        end = time.time()
        totalTime += (end-begin)
        
    recursiveTimes.append(totalTime / len(lists))

print(listSizeArray)
print(executions)

# Generate graphics: Line
plt.plot(listSizeArray, iteractiveTimes, c='blue', ls='-', marker='o', label='Iteractive') # Rod Cut Iteractive
plt.plot(listSizeArray, recursiveTimes, c='red', ls='-.', marker='D', label='Recursive') # Rod Cut Recursive

plt.title("Rod Cut Iteractive x Rod Cut Recursive")
plt.xlabel("Tamanho do vetor")
plt.ylabel("Tempo de execução")
plt.legend(loc='upper left')

plt.xticks(listSizeArray)
plt.show()
