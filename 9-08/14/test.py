# 问题：边界条件考虑不充分

strs = []
strs.append(["flower","flow","flight"])
strs.append(["dog","racecar","car"])
strs.append([""])
strs.append(["a"])
strs.append(["ab", "a"])

def longestCommonPrefix(strs):
    char_n = 0
    string = ""
    while True:
        for i in range(len(strs)):
            if char_n > len(strs[i]) - 1:
                if char_n == len(string):
                    return string
                else:
                    return string[:-1]
            else:
                if char_n == len(string):
                    string += strs[i][char_n]
                else:
                    if strs[i][char_n] != string[-1]:
                        return string[:-1]

        char_n += 1

for i in strs:
    print(i, ": ", longestCommonPrefix(i))