# 滑动窗口

nums = []
nums.append([-2,1,-3,4,-1,2,1,-5,4])
nums.append([1])
nums.append([5,4,-1,7,8])
nums.append([-2,-1])
nums.append([-1,-2])
nums.append([0,-3,1,1])


def maxSubArray(nums):
    maxSum = max(nums)
    start = 0
    for i in range(len(nums)):
        sumWindow = sum(nums[start:i+1])
        maxSum = max(maxSum, sumWindow)
        if sumWindow <= 0:
            start = i + 1

    print(maxSum)
    return maxSum


for i in nums:
    maxSubArray(i)