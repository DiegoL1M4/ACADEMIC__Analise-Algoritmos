
class BinarySort:
    def binary_sort_iterative(A, start, end, value):
        while(start < end):
            mid = (start + end) // 2
            if (A[mid] <= value):
                start = mid + 1
            else:
                end = mid
        
        return start

    def binary_sort_insertion_sort_iterative(A):
        for j in range(1, len(A)):
            value = A[j]
            i_value = BinarySort.binary_sort_iterative(A, 0, j, value)
            
            newList = []

            if(i_value - 1 >= 0):
                newList.extend(A[0:i_value])
            newList.extend([A[j]])
            newList.extend(A[i_value:j])
            if(j + 1 <= len(A) - 1):
                newList.extend(A[j + 1:len(A)])

            A = newList
        
        return A
