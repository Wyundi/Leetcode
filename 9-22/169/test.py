def majorityElement(nums):

    """
    >>> majorityElement([3,2,3])
    3
    >>> majorityElement([2,2,1,1,1,2,2])
    2
    """

    dic = {}
    for i in nums:
        if dic.get(i, None) == None:
            dic[i] = 1
        else:
            dic[i] += 1

    for key, value in dic.items():
        if value > (len(nums)/2):
            return key

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose = True)