def wordPattern(pattern, s):
    
    """
    >>> wordPattern(pattern = "abba", s = "dog cat cat dog")
    True
    >>> wordPattern(pattern = "abba", s = "dog cat cat fish")
    False
    >>> wordPattern(pattern = "aaaa", s = "dog cat cat dog")
    False
    >>> wordPattern(pattern = "abba", s = "dog dog dog dog")
    False
    """

    List = []
    sub_s = ''
    for i in s:
        if i != ' ':
            sub_s += i
        else:
            List.append(sub_s)
            sub_s = ''

    List.append(sub_s)

    if len(pattern) != len(List):
        return False

    dic_p = {}
    dic_s = {}
    for i in range(len(pattern)):
        if dic_p.get(pattern[i], None) == None:
            dic_p[pattern[i]] = List[i]
        else:
            if dic_p.get(pattern[i], None) != List[i]:
                return False

        if dic_s.get(List[i], None) == None:
            dic_s[List[i]] = pattern[i]
        else:
            if dic_s.get(List[i], None) != pattern[i]:
                return False

    return True

# if __name__ == '__main__':
#     wordPattern(pattern = "abba", s = "dog cat cat dog")

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose = True)