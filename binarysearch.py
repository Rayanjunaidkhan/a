# nums=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nums = [3,5,7,9,11,13,15,17,19]
key = int(input("what number do you want to search for: "))
found = False
upperbound = len(nums)
lowerbound = 0
mid = 0

while upperbound >= lowerbound:
    # // has same effect as int int((upperbound + lowerbound) / 2)
    # // is called integer division
    mid = (upperbound + lowerbound) // 2
    
    if key == nums[mid]:
        found = True
        break
    elif key > nums[mid]:
        lowerbound = mid + 1
    else:
        upperbound = mid - 1
if found == True:
    print("number found at ",mid + 1)
else:
    print("not found")
