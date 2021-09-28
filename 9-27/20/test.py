def isValid(s):

    """
    >>> isValid(s = "()")
    True
    >>> isValid(s = "()[]{}")
    True
    >>> isValid(s = "(]")
    False
    >>> isValid(s = "([)]")
    False
    >>> isValid(s = "{[]}")
    True
    """

    List = []
    dic = {'(':')', '[':']', '{':'}'}
    for i in s:
        if i in ['(', '[', '{']:
            List.append(i)
        else:
            if List == []:
                return False
            elif dic[List[-1]] != i:
                return False
            else:
                List.pop()

    if List == []:
        return True
    else:
        return False

# if __name__ == '__main__':
#     isValid(s = "()[]{}")


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose = True)