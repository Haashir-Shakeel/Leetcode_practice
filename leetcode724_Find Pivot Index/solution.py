def pivotIndex(nums):
    total_sum=0
    for i in range(0, len(nums)):
        total_sum = total_sum + nums[i]
   
    left_sum = 0
    for i in range(0, len(nums)):
        if (total_sum - left_sum - nums[i] == left_sum):
            return i
        else:
            left_sum = left_sum + nums[i]
    return -1
            
def pivotIndex2(nums):
    total_sum=0
    for i in range(0, len(nums)):
        total_sum = total_sum + nums[i]
   
    left_sum = 0
    for i in range(0, len(nums)):
        if (i !=0):
            left_sum = left_sum + nums[i-1]
        if (total_sum - left_sum - nums[i] == left_sum):
            return i
    return -1

nums = [1,7,3,6,5,6]
print(pivotIndex(nums))
print(pivotIndex2(nums))
