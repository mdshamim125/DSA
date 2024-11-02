def partition(arr, low, high):
    pivot = arr[high]  # Step 1: সর্বশেষ উপাদানটিকে পিভট হিসেবে বেছে নেয়।
    i = low - 1  # Step 2: সূচক i কে low - 1 দিয়ে ইনিশিয়ালাইজ করা হয়.
   
    # Step 3: পিভটের তুলনায় ছোট উপাদানগুলিকে বাঁ দিকে নিয়ে আসে।
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # ছোট উপাদানকে বামে সরানো হয়.


    # Step 4: পিভটকে তার সঠিক অবস্থানে নিয়ে আসে।
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1  # পিভটের নতুন অবস্থান রিটার্ন করে।


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)  # Step 5: partition ফাংশন ব্যবহার করে পিভটের অবস্থান নির্ধারণ করা হয়।
        quick_sort(arr, low, pi - 1)    # Step 6: বাম দিকে পুনরায় `quick_sort` ডাকা হয়।
        quick_sort(arr, pi + 1, high)   # Step 7: ডান দিকে পুনরায় `quick_sort` ডাকা হয়।


arr = [10, 7, 8, 9, 1, 5]
quick_sort(arr, 0, len(arr) - 1)
print("Sorted array is:", arr)