nums = [1,2,3,4,5,6,7]
k = 3

def rotate(nums, k):
    k = k % (len(nums))
    nums[:] = nums[-k:] + nums[:-k]