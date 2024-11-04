"""সমস্যা: একটি নির্দিষ্ট যোগফল পাওয়ার জন্য উপাদানগুলোর subset বের করতে হবে।"""


def subset_sum(nums, target, path=[]):
    if target == 0:
        print(path)
        return
    if not nums or target < 0:
        return
    subset_sum(nums[1:], target - nums[0], path + [nums[0]])  # Include nums[0]
    subset_sum(nums[1:], target, path)  # Exclude nums[0]


nums = [3, 1, 2, 7]
target = 3
subset_sum(nums, target)