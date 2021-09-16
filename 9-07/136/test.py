nums = [-1,-1,2]

def singleNumber(nums):
    dic = {}
    for i in range(len(nums)):
        if dic.get(nums[i], None) == None:
            dic[nums[i]] = nums[i]
        else:
            dic.pop(nums[i])

    print(list(dic.keys())[0])
    return list(dic.keys())[0]

singleNumber(nums)