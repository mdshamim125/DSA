"""একটি অ্যারে [3, 5, 1, 8, 2, 9, 0, 7] দেওয়া আছে, এবং আমাদের এই অ্যারেটি থেকে ম্যাক্সিমাম ও মিনিমাম এলিমেন্ট খুঁজে বের করতে হবে।"""


def findMaxMin(arr, low, high):
    if(low==high):
        return arr[low], arr[high]
    elif(high==low+1):
        if(arr[low]<arr[high]):
            return arr[low], arr[high]
        else:
            return arr[high], arr[low]
    mid=(low+high)//2

    min1, max1 = findMaxMin(arr, low, mid)
    min2, max2 = findMaxMin(arr, mid+1, high)

    finalMin = min(min1, min2)
    finalMax = max(max1, max2)
    
    return finalMin, finalMax

arr = list(map(int, input("Enter some numbers with white spaces: ").split()))
n = len(arr)
minVal, maxVale = findMaxMin(arr, 0, n-1)
print("Minimum value: ", minVal)
print("Maximum value: ", maxVale)