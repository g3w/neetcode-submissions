class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        subset = []


        def dfs(i):

            # reached end
            if i >= len(nums):
                res.append(subset.copy())
                return

            # include nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # backtrack
            subset.pop()
            # skip duplicates
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            # exclude nums[i]
            dfs(i + 1)

        dfs(0)

        return res