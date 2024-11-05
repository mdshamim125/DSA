def sum_array(arr, n):
    # Base case: if array is empty
    if n == 0:
        return 0
    # Recursive case: sum of last element and sum of remaining array
    return arr[n - 1] + sum_array(arr, n - 1)

# Example usage
arr = [1, 2, 3, 4, 5]
result = sum_array(arr, len(arr))
print("Sum of array elements:", result)
