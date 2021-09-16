s = ["h","e","l","l","o"]

def reverseString(s):
    for i in range((int)(len(s)/2)):
        s[i], s[-i-1] = s[-i-1], s[i]
        print(s)

def reverseS(s):
    s[:] = s[::-1]

reverseString(s)