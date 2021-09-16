nums = [2, 7, 11, 15]
target = 9

def twoSum(nums, target):
    dic = {}
    for n, ele in enumerate(nums):
        dic[ele] = n

    for i in range(len(nums)):
        index = dic.get(target - nums[i], -1)
        if (index != -1) and (index != i):
            return [i, index]

print(twoSum(nums, target))