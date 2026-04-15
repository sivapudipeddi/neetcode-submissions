class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        n = len(nums)
        d1 = {}
        d2 = {}
        
        for i in range(0, n + 1, 1):
            d1[i] = 1
            
        for j in nums:
            d2[j] = 1
            
        for i in range(0, n + 1, 1):
            # Check if the number from d1 exists in d2
            if i not in d2:
                return i