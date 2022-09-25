
def runningSum(nums):
    sum=0
    for i in range(0, len(nums)):
        temp = nums[i]
        nums[i]=nums[i]+sum
        sum = temp + sum
            
    return nums


def runningSum2(nums):
    sum=0
    arr = []
    for i in range(0,len(nums)):
        sum += nums[i]
        arr.append(sum)
    return(arr)

nums=[1,2,3,4]
print(runningSum(nums))
nums=[1,2,3,4]
print(runningSum2(nums))

