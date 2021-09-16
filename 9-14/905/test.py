nums = [3,1,2,4]

def sortArrayByParity(nums):
    List = []
    for i in nums:
        if i % 2 == 0:
            List.insert(0, i)
        else:
            List.append(i)

    return List