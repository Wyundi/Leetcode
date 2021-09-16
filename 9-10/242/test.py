s = "ccac"
t = "ccaa"

def isAnagram(s, t):
    if len(s) != len(t):
        return False
    dic_s = {}
    for i in range(len(s)):
        if dic_s.get(s[i], None) == None:
            dic_s[s[i]] = 1
        else:
            dic_s[s[i]] += 1

    dic_t = {}
    for i in range(len(t)):
        if dic_t.get(t[i], None) == None:
            dic_t[t[i]] = 1
        else:
            dic_t[t[i]] += 1

    if dic_s == dic_t:
        return True
    else:
        return False

print(isAnagram(s, t))