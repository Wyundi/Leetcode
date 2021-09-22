def slowestKey(releaseTimes, keysPressed):
     
    """
    >>> slowestKey(releaseTimes = [9,29,49,50], keysPressed = "cbcd")
    'c'
    >>> slowestKey(releaseTimes = [12,23,36,46,62], keysPressed = "spuda")
    'a'
    """

    releaseTimes.insert(0, 0)

    dic = {}
    for i in range(1, len(releaseTimes)):
        if dic.get(keysPressed[i-1], None) == None:
            dic[keysPressed[i-1]] = releaseTimes[i] - releaseTimes[i-1]
        else:
            dic[keysPressed[i-1]] = max(dic[keysPressed[i-1]], releaseTimes[i] - releaseTimes[i-1])

    maxTime = 0
    maxKey = []
    for key, value in dic.items():
        if maxTime < value:
            maxKey = [key]
            maxTime = value
        elif maxTime == value:
            maxKey.append(key)

    maxKey.sort()
    return maxKey[-1]


# if __name__ == '__main__':
#     slowestKey(releaseTimes = [12,23,36,46,62], keysPressed = "spuda")
#     slowestKey(releaseTimes = [1,2,3,4,5,6,7,8,9,10], keysPressed = "aabbbcddde")

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose = True)