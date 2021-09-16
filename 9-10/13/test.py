s = "III"

def romanToInt(s):
    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    List = []

    for i in s:
        List.append(dic[i])

    num = 0
    if len(List) == 1:
        num = List[0]
    else:
        for i in range(len(List)-1):
            if List[i] >= List[i+1]:
                num += List[i]
            else:
                num -= List[i]
            
        num += List[-1]

    return num
        
print(romanToInt(s))