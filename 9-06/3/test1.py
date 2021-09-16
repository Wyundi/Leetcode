s = "abcabcbb"

def lengthOfLongestSubstring(s:):
    List = []
    length = 0

    for n, ele in enumerate(s):
        if ele not in List:
            List.append(ele)
        else:
            index = List.index(ele)
            List = List[index+1:]
            List.append(ele)

        length = max(length, len(List))

    return length

print(lengthOfLongestSubstring(s))