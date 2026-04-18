class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        perm = []
        checklist = [False] * n
        
        def dfs(i):
            if i == n:
                result.append(perm[:])
            if i < n:
                for j in range(n):
                    if not checklist[j]:
                        perm.append(nums[j])
                        checklist[j] = True

                        dfs(i + 1)

                        checklist[j] = False
                        perm.pop()

        dfs(0)
        return result