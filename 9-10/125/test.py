s = "Z9z"

def isPalindrome(s):
    List = []
    for i in s:
        if ord(i) in range(65, 91):
            List.append(chr(ord(i) + 32))
        elif (ord(i) in range(97, 123)) or (ord(i) in range(48, 58)):
            List.append(i)
        else:
            continue

    for i in range(len(List)//2):
        if List[i] != List[-i-1]:
            return False

    return True

print(isPalindrome(s))