intervals = [[1,3],[2,6],[8,10],[15,18]]
intervals = [[1,4],[5,6]]

def merge(intervals):
    minStart = min(min(intervals))
    maxEnd = max(max(intervals))

    List = [0] * (maxEnd - minStart)
    
    for i in intervals:
        List[i[0]:i[1]+1] = [1] * (i[1]+1 - i[0])

    print(List)

    start = []
    end = []
    
    for i in range(1, len(List)):
        if List[i-1] == 0 and List[i] == 1:
            start.append(i)
        elif List[i-1] == 1 and List[i] == 0:
            end.append(i-1)
    
    if List[-1] == 1:
        end.append(len(List)-1)

    result = []
    for i in range(len(start)):
        result.append([start[i], end[i]])

    print(result)
    return result
    
merge(intervals)