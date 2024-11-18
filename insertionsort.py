def insertion_sort(A):
    # Start from the second element (index 1) since the first element is trivially sorted
    for i in range(1, len(A)):
        # Store the current element to be placed
        key = A[i]
        # Initialize the variable to track the position to place the current element
        j = i - 1
        
        # Shift elements of the sorted segment that are greater than the current element to the right
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j -= 1
            
        # Place the current element at its correct position
        A[j + 1] = key

# Example usage
A = [12, 11, 13, 5, 6]
insertion_sort(A)
print("Sorted array:", A)
