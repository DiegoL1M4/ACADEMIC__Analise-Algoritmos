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
    listSizeArray.append(random.randrange(10, 10000 + 1)) # Array size: 10 ≤ n ≤ 10.000

listSizeArray = sorted(listSizeArray)
# listSizeArray = [10, 40, 80, 100, 150, 250, 350, 450, 550, 650]
# listSizeArray = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
# listSizeArray = [80, 500, 1000, 2000, 3000, 4000, 5000, 7000, 9000, 10000]

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
        listCopy = list.copy()
        begin = time.time()
        InsertionSort. insertion_sort(listCopy)
        end = time.time()
        totalTime += (end - begin)

    insertionTimes.append(totalTime / len(lists))

# Test: Binary Search
binaryTimes = []
for lists in listSet:
    totalTime = 0
    for list in lists:
        # Binary Search Test
        listCopy = list.copy()
        begin = time.time()
        BinarySearch.binary_search_insertion_sort_iterative(listCopy)
        end = time.time()
        totalTime += (end-begin)
        
    binaryTimes.append(totalTime / len(lists))

print(listSizeArray)
print(executions)

# Generate graphics: Line
plt.plot(listSizeArray, insertionTimes, c='blue', ls='-', marker='o', label='Insertion-sort') # Insertion Sort
plt.plot(listSizeArray, binaryTimes, c='red', ls='-.', marker='D', label='Binary-insertion-sort') # Binary Search

plt.title("Insertion Sort x Binary Search")
plt.xlabel("Tamanho do vetor")
plt.ylabel("Tempo de execução")
plt.legend(loc='upper left')

plt.xticks(listSizeArray)
plt.show()
