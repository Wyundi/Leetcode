def maxSlidingWindow(nums, k):

    """
    >>> maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3)
    [3,3,5,5,6,7]
    >>> maxSlidingWindow(nums = [1], k = 1)
    [1]
    >>> maxSlidingWindow(nums = [1,-1], k = 1)
    [1,-1]
    >>> maxSlidingWindow(nums = [9,11], k = 2)
    [11]
    >>> maxSlidingWindow(nums = [4,-2], k = 2)
    [4]
    """

    if k == 1:
        return nums
    else:


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose = True)