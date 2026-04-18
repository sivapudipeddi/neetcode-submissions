class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # Sort in-place to group duplicates
        n = len(nums)
        result = []
        subset = []

        def dfs(i):
            if i == n:
                result.append(subset[:])
                return result # Exit once a leaf node is reached

            # All subsets that INCLUDE nums[i]
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop() # Backtrack

            # All subsets that EXCLUDE nums[i]
            # Skip all consecutive duplicates of the current number
            while i + 1 < n and nums[i] == nums[i + 1]:
                i += 1
            
            # Move to the next unique element
            dfs(i + 1)
        dfs(0)
        return result