def selection_sort(A):
    for current in range(len(A)):
        minIndex = current
        for i in range(current + 1, len(A)):
            if A[i] < A[minIndex]:
                minIndex = i
        A[current], A[minIndex] = A[minIndex], A[current]

# Example usage
A = [64, 25, 12, 22, 11]
selection_sort(A)
print("Sorted array:", A)

