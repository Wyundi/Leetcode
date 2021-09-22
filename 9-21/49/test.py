def groupAnagrams(strs):

    """
    >>> groupAnagrams(["eat","tea","tan","ate","nat","bat"])
    [["bat"],["nat","tan"],["ate","eat","tea"]]
    >>> groupAnagrams([""])
    [[""]]
    >>> groupAnagrams(["a"])
    [["a"]]
    >>> groupAnagrams(["cab","tin","pew","duh","may","ill","buy","bar","max","doc"])
    [["cab"],["tin"],["pew"],["duh","ill"],["may"],["buy"],["bar"],["max"],["doc"]]
    """

    dic = {}
    ord_List = []
    for string in strs:
        for i in string:
            ord_List.append(ord(i))
        ord_List.sort()
        ord_string = str(ord_List)
        if dic.get(ord_string, None) == None:
            dic[ord_string] = [string]
        else:
            dic[ord_string].append(string)
        ord_List = []

    List = []
    for key, value in dic.items():
        List.append(value)

    return List

# if __name__ == '__main__':
#     groupAnagrams(["eat","tea","tan","ate","nat","bat"])

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose = True)