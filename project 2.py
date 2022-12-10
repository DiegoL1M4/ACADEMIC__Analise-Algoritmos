import time
import random
import matplotlib.pyplot as plt
import numpy as np

from codes.rod_cut_iteractive import RodCutIteractive
from codes.rod_cut_recursive import RodCutRecursive

P = [2, 3]
P = [2, 3, 7, 5]
P = [1, 5, 8, 9]
print("")
print("Custo Iterativo: " + str(RodCutIteractive.cutRod(P, len(P))))
print("")
print("Custo Recursivo: " + str(RodCutRecursive.cutRod(P, len(P))))
print("")

# Variables
amountArraySize = 10
listSet = []

# List size array (n)
listSizeArray = []
for i in range(amountArraySize):
    listSizeArray.append(random.randrange(10, 1000 + 1)) # Array size: 10 ≤ n ≤ 10.000

listSizeArray = sorted(listSizeArray)
# listSizeArray = [10, 40, 80, 100, 150, 250, 350, 450, 550, 650]
# listSizeArray = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
# listSizeArray = [80, 500, 1000, 2000, 3000, 4000, 5000, 7000, 9000, 10000]

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
            list.append(random.uniform(1, n + 1)) # Array element: −2n ≤ A[i] ≤ 2n
        
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
