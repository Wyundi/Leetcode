List = [1, 1, 1, 2]

class Solution:
    def removeDuplicates(self, nums) -> int:
        i = 1
        while i < len(nums):
            if nums[i] == nums[i-1]:
                nums.pop(i)
                continue
            i += 1

        return len(nums), nums

def main():
    result = Solution()
    print(result.removeDuplicates(List))

if __name__ == '__main__':
    main()