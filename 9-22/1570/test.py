class SparseVector:
    def __init__(self, nums: List[int]):
        self.length = len(nums)
        self.data = nums

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        sum = 0
        for i in range(self.length):
            sum += self.data[i] * vec.data[i]
            
        return sum