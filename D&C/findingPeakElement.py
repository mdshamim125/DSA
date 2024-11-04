"""এখানে আমাদের এমন একটি এলিমেন্ট খুঁজে বের করতে হবে যা তার আশেপাশের (বা প্রতিবেশী) এলিমেন্টগুলোর চেয়ে বড়।"""


def findPeak(arr, low, high ):
    if(low<=high):
        mid=(low+high)//2
        if(mid==low or arr[mid]>=arr[mid-1]) and (mid==high or arr[mid]>=arr[mid+1]):
            return arr[mid]
        elif(mid>low and arr[mid-1]>arr[mid]):
            return findPeak(arr, low, mid-1)
        else:
            return findPeak(arr, mid+1, high)
        
arr=list(map(int, input("Enter an array with spacing: ").split()))
n = len(arr)
print(f"peak element: {findPeak(arr, 0, n-1)}")