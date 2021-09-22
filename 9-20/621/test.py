def leastInterval(tasks, n):

    """
    >>> leastInterval(tasks = ["A","A","A","B","B","B"], n = 2)
    8
    >>> leastInterval(tasks = ["A","A","A","B","B","B"], n = 0)
    6
    >>> leastInterval(tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2)
    16
    """

    dic = {}
    for i in taska:
        if dic.get(i, None) == None:
            dic[i] = 1
        else:
            dic[i] += 1
    
    for key, value in dic.item():
        pass

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose = True)