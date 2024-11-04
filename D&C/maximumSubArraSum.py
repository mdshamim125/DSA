"""Divide and Conquer (D&C) পদ্ধতি ব্যবহার করে Maximum Subarray Sum সমস্যাটি সমাধান করতে পারি। সমস্যা অনুযায়ী, একটি অ্যারের এমন একটি সাবঅ্যারে খুঁজে বের করতে হবে যেটির উপাদানের যোগফল সর্বোচ্চ হবে।"""


def max_crossing_sum(arr, low, mid, high):
    # Find the maximum sum on the left side
    left_sum = float('-inf')
    total = 0
    for i in range(mid, low - 1, -1):
        total += arr[i]
        if total > left_sum:
            left_sum = total

    # Find the maximum sum on the right side
    right_sum = float('-inf')
    total = 0
    for i in range(mid + 1, high + 1):
        total += arr[i]
        if total > right_sum:
            right_sum = total

    # Return the maximum sum across the left and right parts
    return left_sum + right_sum

def max_subarray_sum_dnc(arr, low, high):
    # Base Case: If there is only one element
    if low == high:
        return arr[low]

    # Find the midpoint
    mid = (low + high) // 2

    # Recursively find the maximum sum in the left, right, and crossing subarrays
    left_sum = max_subarray_sum_dnc(arr, low, mid)
    right_sum = max_subarray_sum_dnc(arr, mid + 1, high)
    cross_sum = max_crossing_sum(arr, low, mid, high)

    # Return the maximum of the three sums
    return max(left_sum, right_sum, cross_sum)

# Example usage
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = max_subarray_sum_dnc(arr, 0, len(arr) - 1)
print("Maximum Subarray Sum:", result)
