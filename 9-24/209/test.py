def minSubArrayLen(target, nums):

    """
    >>> minSubArrayLen(target = 7, nums = [2,3,1,2,4,3])
    2
    >>> minSubArrayLen(target = 4, nums = [1,4,4])
    1
    >>> minSubArrayLen(target = 11, nums = [1,1,1,1,1,1,1,1])
    0
    """

    start = 0
    minLength = 

    for i in nums:
        Sum = sum(nums[start, end])
        if Sum >= target:
            length = end - start + 1

if __name__ == '__main__':
    minSubArrayLen(target = 7, nums = [2,3,1,2,4,3])

# if __name__ == '__main__':
#     import doctest
#     doctest.testmod(verbose = True)