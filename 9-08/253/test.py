def minMeetingRooms(intervals):

    """
    >>> minMeetingRooms(intervals = [[0,30],[5,10],[15,20]])
    2
    >>> minMeetingRooms(intervals = [[7,10],[2,4]])
    1
    """

    intervals.sort(key = lambda intervals: intervals[1])
    maxTime = intervals[-1][-1]
    
    List = [0] * maxTime
    
    for L in intervals:
        # 两个List对应位相加，如何用 O(1) 实现？
        # no way

    print(List)
    print(max(List))

if __name__ == '__main__':
    minMeetingRooms(intervals = [[0,30],[5,10],[15,20]])

# if __name__ == '__main__':
#     import doctest
#     doctest.testmod(verbose = True)