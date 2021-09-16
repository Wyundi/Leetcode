paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

paragraph = "Bob"
banned = []

paragraph = "Bob. hIt, baLl"
banned = ["bob", "hit"]

paragraph = "a, a, a, a, b,b,b,c, c"
banned = ["a"]

def mostCommonWord(paragraph, banned):
    pass

mostCommonWord(paragraph, banned)
