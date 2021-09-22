def isRobotBounded(instructions):

    """
    >>> isRobotBounded("GGLLGG")
    true
    >>> isRobotBounded("GG")
    false
    >>> isRobotBounded("GL")
    true
    >>> isRobotBounded("GLRLLGLL")
    true
    """

    direction = 0
    for i in instructions:
        if i == 'L':
            direction -= 1
        elif i == 'R':
            direction += 1

    if direction % 4 == 0:
        return False
    else:
        return True

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose = True)