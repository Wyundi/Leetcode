nums1 = [2,0]
m = 1
nums2 = [1]
n = 1

def merge(nums1, m, nums2, n):
    n1 = 0
    s = m + n

    if n != 0:
        for i in range(s):
            if nums1[i] >= nums2[n1]:
                nums1.pop()
                nums1.insert(i, nums2[n1])
                n1 += 1
                i -= 1
                
                if n1 == n:
                    break
        
        if n1 <= (n-1):
            s = m + n
            nums1[s-n+n1:s] = nums2[n1:n]

    print(nums1)

merge(nums1, m, nums2, n)