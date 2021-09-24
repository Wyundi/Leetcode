def corpFlightBookings(bookings, n):

    """
    >>> corpFlightBookings(bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5)
    [10,55,45,25,25]
    >>> corpFlightBookings(bookings = [[1,2,10],[2,2,15]], n = 2)
    [10,25]
    """

    List = [0] * n

    for i in range(n):
        for j in bookings:
            if i in range(j[0]-1, j[1]):
                List[i] += j[2]

    # print(List)
    return List

# if __name__ == '__main__':
#     corpFlightBookings(bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5)

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose = True)