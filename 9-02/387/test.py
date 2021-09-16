string = 'aabb'

def firstUniqChar(string):
    List = []
    time = []
    for i in string:
        if i not in List:
            List.append(i)
            time.append(1)
        else:
            time[List.index(i)] += 1

    for j in range(len(time)):
        if time[j] == 1:
            return string.index(List[j])
    
    return -1

print(firstUniqChar(string))