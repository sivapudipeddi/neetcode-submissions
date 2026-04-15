class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = {}

        for i in range(len(nums)):
            if nums[i] in seen:
                seen[nums[i]] += 1
            else:
                seen[nums[i]] = 1

        for i in range(len(nums)):
            if seen[nums[i]] == 1:
                return nums[i]