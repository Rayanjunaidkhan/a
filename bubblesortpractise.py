nums = [32,13,142,213,65,453,231,786,564,1000]

def bubblesort(nums):
    n = len(nums)
    for i in range(n):
        for j in range(n-i-1):
            if nums[j] > nums[j + 1]:
                temp = nums[j]
                nums[j] = nums [j + 1]
                nums[j + 1] = temp

bubblesort(nums)
print(nums)
