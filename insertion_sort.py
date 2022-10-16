
class InsertionSort:
    def insertion_sort(A):
        for j in range(1, len(A)):
            value = A[j]
            i = j - 1
            while i > -1 and A[i] > value:
                A[i + 1] = A[i]
                i = i - 1
            A[i + 1] = value
        
        return A
