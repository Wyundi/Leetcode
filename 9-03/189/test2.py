nums = [1,2,3,4,5,6,7]
k = 3

def rotate(nums, k):
    k = k % (len(nums))
    for i in range(k):
        nums = [nums[-1]] + nums[:-1]

    print(nums)

rotate(nums, k)