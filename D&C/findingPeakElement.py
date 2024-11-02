def findPeak(arr, low, high, n):
    if(low<=high):
        mid=(low+high)//2
        if(mid==0 or arr[mid]>=arr[mid-1]) and (mid==n-1 or arr[mid]>=arr[mid+1]):
            return arr[mid]
        elif(mid>0 and arr[mid-1]>arr[mid]):
            return findPeak(arr, low, mid-1, n)
        else:
            return findPeak(arr, mid+1, high, n)
        
arr=list(map(int, input("Enter an arra with spacing: ").split()))
n = len(arr)
print(f"peak element: {findPeak(arr, 0, n-1, n)}")