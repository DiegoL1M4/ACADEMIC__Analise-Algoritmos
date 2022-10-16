import time

from busca_binaria import BinarySearch
from insertion_sort import InsertionSort

# Variables
list = [1, 5, 10, 3, 21, 20, 4, 7, 15, 2]

# Binary Search Test
print("\nBinary Search:")
begin = time.time()
print(BinarySearch.insertionsort_busca_binaria(list))
end = time.time()
print((end - begin) * 100000)

# Insertion Sort Test
print("\nInsertion Sort:")
begin = time.time()
print(InsertionSort. insertion_sort(list))
end = time.time()
print((end - begin) * 100000)
