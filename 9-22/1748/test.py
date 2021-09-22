def sumOfUnique(nums):

    """
    >>> sumOfUnique([1,2,3,2])
    4
    >>> sumOfUnique([1,1,1,1,1])
    0
    >>> sumOfUnique([1,2,3,4,5])
    15
    >>> sumOfUnique([])
    0
    """

    dic = {}
    for i in nums:
        if dic.get(i, None) == None:
            dic[i] = 1
        else:
            dic[i] += 1

    sum = 0
    for key, value in dic.items():
        if value == 1:
            sum += key

    return sum

# if __name__ == '__main__':
#     sumOfUnique([1,2,3,2])

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose = True)