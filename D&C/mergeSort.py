"""def mergeSort(arr):
    if(len(arr)>1):
        mid=len(arr)//2
        left_half=arr[:mid]
        right_half=arr[mid:]

        mergeSort(left_half)
        mergeSort(right_half)

        i=j=k=0
        while(i<len(left_half) and j<len(right_half)):
            if(left_half[i]<right_half[j]):
                arr[k]=left_half[i]
                i+=1
            else:
                arr[k]=right_half[j]
                j+=1
            k+=1

        while(i<len(left_half)):
            arr[k]=left_half[i]
            i+=1
            k+=1

        while(j<len(right_half)):
            arr[k]=right_half[j]
            j+=1
            k+=1
arr=[38, 27, 43, 3, 9, 82, 10]
mergeSort(arr)
print("Sorted array is: ", arr)"""


def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursively split and sort both halves
        mergeSort(left_half)
        mergeSort(right_half)

        i = j = k = 0

        # Merge the sorted halves
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Copy any remaining elements of left_half
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Copy any remaining elements of right_half
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Taking input from the user
arr = list(map(int, input("Enter the elements of the array, separated by spaces: ").split()))
mergeSort(arr)
print("Sorted array is:", arr)
