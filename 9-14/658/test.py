arr = [1,2,3,4,5]
k = 4
x = 3

def findClosestElements(arr, k, x):
    List = []
    dic = {}
    for i in range(len(arr)):
        value = abs(arr[i]-x)
        List.append(value)
        if dic.get(value, None) == None:
            dic[value] = [i]
        else:
            dic[value].append(i)
        List.sort()

    result = []
    for j in List[:k]:
        result.append(arr[dic[j][0]])
        dic[j].pop(0)
    result.sort()
    return result

print(findClosestElements(arr, k, x))