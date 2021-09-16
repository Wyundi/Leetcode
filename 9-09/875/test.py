piles = [312884470]
h = 312884469

def minEatingSpeed(piles, h):
    if h == len(piles):
        return max(piles)
    else:
        k = max(piles)
        for i in range(k, 0, -1):
            h_test = 0
            for j in piles:
                if j%k != 0:
                    h_test += 1
                h_test += (j//i)

            if h_test == h:
                return i
            elif h_test > h:
                return i+1

print(minEatingSpeed(piles, h))