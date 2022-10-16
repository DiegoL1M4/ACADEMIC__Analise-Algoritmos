import time
import random
import matplotlib.pyplot as plt
import numpy as np

from busca_binaria import BinarySearch
from insertion_sort import InsertionSort

# Variables
amountArraySize = 10
listSet = []

# List size array (n)
listSizeArray = []
for i in range(amountArraySize):
    listSizeArray.append(random.randrange(10, 10001)) # Array size: 10 ≤ n ≤ 10.000

listSizeArray = sorted(listSizeArray)

# Generate total execution (m)
executions = []
for n in listSizeArray:
    m = random.randrange(10, 21) # Total executions: 10 ≤ m ≤ 20
    executions.append([n, m])

# Generate lists
for execution in executions:
    listExecutions = []
    for m in range(execution[1]):
        list = []
        for n in range(execution[0]):
            list.append(random.uniform(-2*n, 2*n + 1)) # Array element: −2n ≤ A[i] ≤ 2n
        
        random.shuffle(list)
        listExecutions.append(list)
    listSet.append(listExecutions)

# Test: Insertion Sort
insertionTimes = []
for lists in listSet:
    totalTime = 0
    for list in lists:
        # Insertion Sort Test
        begin = time.time()
        InsertionSort. insertion_sort(list)
        end = time.time()
        totalTime += (end - begin)

    insertionTimes.append(totalTime / len(lists))

# Test: Binary Search
binaryTimes = []
for lists in listSet:
    totalTime = 0
    for list in lists:
        # Binary Search Test
        begin = time.time()
        BinarySearch.insertionsort_busca_binaria(list)
        end = time.time()
        totalTime += (end-begin)
        
    binaryTimes.append(totalTime / len(lists))

# Generate graphics: Line
plt.plot(listSizeArray, insertionTimes, c='blue', ls='-', lw='1', marker='o') # Insertion Sort
plt.plot(listSizeArray, binaryTimes, c='red', ls='-.', lw='1', marker='o') # Binary Search
plt.show()

# Generate graphics: Bars
# plt.bar(listSizeArray, insertionTimes, color='blue') # Insertion Sort
# plt.bar(listSizeArray, binaryTimes, color='red') # Binary Search



# barWidth = 0.10 #4legendas

# r1 = np.arange(2)
# r2 = [x + barWidth for x in r1]

# capsizevar = 6

# plt.bar(r1, insertionTimes, width=barWidth, capsize=capsizevar, color = 'royalblue', label='Insertion')
# plt.bar(r2, binaryTimes, width=barWidth, capsize=capsizevar, color = 'dodgerblue', label='Binary')
# plt.show()
