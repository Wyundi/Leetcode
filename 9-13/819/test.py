paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

paragraph = "Bob"
banned = []

paragraph = "Bob. hIt, baLl"
banned = ["bob", "hit"]

paragraph = "a, a, a, a, b,b,b,c, c"
banned = ["a"]

def mostCommonWord(paragraph, banned):
    List = []
    dic = {}

    for i in range(len(paragraph)):
        if i == len(paragraph) - 1:
            List = checkCaptial(paragraph[i], List)
            checkList(List, dic, banned)
        if paragraph[i] in [' ', '!', '?', "'", ',', ';', '.']:
            if List == []:
                continue
            else:
                checkList(List, dic)


def checkCaptial(char, List):
    if ord(char) in range(65, 91):
        List.append(chr(ord(char) + 32))
    elif ord(char) in range(97, 123):
        List.append(char)

    return List

def checkList(List, dic, banned):
    string = str(List)
    if len(banned) != 0:
        for i in range(len(banned)):
            if string == banned[i]:
                List = []
                return List, dic
                
    if dic.get(string, None) == None:
        dic[string] = 1
    else:
        dic[string] += 1


mostCommonWord(paragraph, banned)
