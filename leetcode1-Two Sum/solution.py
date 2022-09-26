#bruteforce
def twoSum(nums,target):
    for i in range(0, len(nums)):
        diff = target - nums[i]
        for j in range(i+1,len(nums)):
            if nums[j] == diff:
                return [i,j]
            

#array approach
arr=[]
def twoSum2(nums,target):
    for i in range(0, len(nums)):
        diff = target - nums[i]
        if nums[i] in arr:
            return [arr.index(nums[i]),i]
        else:
            arr.append(diff)


#hashmaps
hashmap = {}
def twoSum3(nums,target):
    for i in range(0, len(nums)):
        diff = target - nums[i]
        value = [key for key in hashmap if hashmap[key]==nums[i]]
        if value:
            return[value[0],i]
        else:
            hashmap[i]=diff

# nums=[1,3,15,5]
# nums=[3,3]
nums = [3,6,3]
nums = [2,7,11,15]

target= 9
print(twoSum3(nums, target))
print(twoSum(nums, target))
print(twoSum2(nums, target))

        

        