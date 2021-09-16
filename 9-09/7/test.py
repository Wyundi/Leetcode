x = -2147483412

def reverse(x):
    if x == 0:
        return 0
    elif x > 0:
        label = 0
        string = str(x)
    else:
        label = 1
        string = str(x)[1:]

    string = string[::-1]
    for i in range(len(string)):
        if string[i] == '0':
            string = string[1:]
        if string[i] != '0':
            break

    if len(string) >= 10:
        List = [2, 1, 4, 7, 4, 8, 3, 6, 4, 8]
        for i, ele in enumerate(List):
            print(i, string[i], ele)
            if int(string[i]) < ele:
                break
            elif int(string[i]) > ele:
                return 0
            else:
                if (i == 9) and (label == 0):
                    return 0

    if label:
        string = '-' + string
    
    return int(string)

print(reverse(x))