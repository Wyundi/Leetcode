def isHappy(n):

    """
    >>> isHappy(19)
    true
    >>> isHappy(2)
    false
    """

    num = n
    List = []
    digit = 10
    ListNum = [num]
    
    while (True):

        while (num != 0):
            mod = int(num % digit)
            List.insert(0, mod)
            num = (num - mod) / digit

        sumN = 0
        for i in List:
            sumN += (i*i)
        List = []

        if sumN == 1:
            return True
        elif sumN in ListNum:
            return False
        else:
            num = sumN
            ListNum.append(sumN)
        

# if __name__ == '__main__':
#     isHappy(27)

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose = True)