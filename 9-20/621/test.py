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
    for i in tasks:
        if dic.get(i, None) == None:
            dic[i] = 1
        else:
            dic[i] += 1
    
    List =  []
    label = []

    while dic != {}:
        print(dic)
        for key, value in dic.items():
            List.append(key)
            dic[key] -= 1
            if dic[key] == 0:
                label.append(key)

        for key in label:
            dic.pop(key)

        label = []

    print(List)
    sum = 0


if __name__ == '__main__':
    leastInterval(tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2)

# if __name__ == '__main__':
#     import doctest
#     doctest.testmod(verbose = True)