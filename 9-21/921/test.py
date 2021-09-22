def minAddToMakeValid(s):

    """
    >>> minAddToMakeValid("())")
    1
    >>> minAddToMakeValid("(((")
    3
    >>> minAddToMakeValid("()")
    0
    >>> minAddToMakeValid("()))((")
    4
    """

    label = 0
    moveRequired = 0
    for i in s:
        if i == '(':
            label += 1
        elif i == ')':
            if label != 0:
                label -= 1
            else:
                moveRequired += 1

    return label + moveRequired

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose = True)