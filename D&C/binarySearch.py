def binarySearch(arr, low, high, x):
    if(low<=high):
        mid=(low+high)//2
        if(arr[mid]==x):
            return mid
        elif(arr[mid]>x):
            return binarySearch(arr, low, mid-1, x)
        else:
            return binarySearch(arr, mid+1, high, x)
    return -1

arr=[2,3,4,10,40]
x=10
result=binarySearch(arr, 0, len(arr)-1, x)
if(result != -1):
    print(f"Element is present at index {result}")
else:
    print(f"Element is not present in array")