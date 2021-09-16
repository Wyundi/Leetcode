nums = [2, 0, 0]
nums = [3,2,1,0,4]


def canJump(nums):
    sumStep = 0
    if len(nums) <= 1:
        return True
    for i in range(len(nums)):
        sumStep = max((nums[i] + i), sumStep)
      
        if sumStep == len(nums) - 1:
            return True

        if sumStep == i:
            return False

    return True

print(canJump(nums))