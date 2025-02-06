nums = [14,23,64,11,8,15,76]


n =len(nums)
for i in range(1,n):
    j = i - 1
    key = nums[i]
    while j >= 0 and nums[j] > key:
        nums[j+1] = nums[j]
        j = j - 1
    nums[j + 1] = key
    
        

print(nums)