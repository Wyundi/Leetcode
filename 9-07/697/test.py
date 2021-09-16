nums = [1,2,2,3,1]

def findShortestSubArray(nums):
    dic = {}
    for i in range(len(nums)):
        if dic.get(nums[i], None) == None:
            dic[nums[i]] = {}
            dic[nums[i]]['num'] = 1
            dic[nums[i]]['List'] = [i]
        else:
            dic[nums[i]]['num'] += 1
            dic[nums[i]]['List'].append(i)

    maxFreq = {'mF': 0, 'keys': []}
    for i in list(dic.keys()):
        if maxFreq['mF'] < dic[i]['num']:
            maxFreq['mF'] = dic[i]['num']
            maxFreq['keys'] = [i]
        elif maxFreq['mF'] == dic[i]['num']:
            maxFreq['keys'].append(i)
        else:
            continue

    smallestLength = {'num': 0, 'sL': 0}
    for i in maxFreq['keys']:
        length = dic[i]['List'][-1] - dic[i]['List'][0] + 1
        if smallestLength['num'] == 0:
            smallestLength['num'] += 1
            smallestLength['sL'] = length
        else:
            if smallestLength['sL'] == length:
                smallestLength['num'] += 1
            elif smallestLength['sL'] > length:
                smallestLength['num'] = 1
                smallestLength['sL'] = length
            else:
                continue

    return smallestLength['sL']


findShortestSubArray(nums)