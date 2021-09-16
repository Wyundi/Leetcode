# 类似滑动窗口？

intervals = [[1,3],[2,6],[8,10],[15,18]]
intervals = [[1,4],[5,6]]
# intervals = [[1,4],[4,5]]
# intervals = [[1,4],[2,3]]
intervals = [[2,3],[4,5],[6,7],[8,9],[1,10]]

def merge(intervals):
    if len(intervals) == 1:
        return intervals

    intervals.sort()
    print(intervals)

    current_intervals = intervals[0]
    result = []
    for i in range(1, len(intervals)):
        if current_intervals[1] >= intervals[i][0]:
            if current_intervals[1] < intervals[i][1]:
                current_intervals[1] = intervals[i][1]
        else:
            result.append(current_intervals)
            current_intervals = intervals[i]

    result.append(current_intervals)

    print(result)
    return result

    
merge(intervals)