class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_subarray = float('inf')
        for i in range(len(nums)):
            cursum = 0
            counter = 0
            for j in range(i, len(nums)):
                cursum += nums[j]
                counter += 1
                if cursum >= target:
                    min_subarray = min(min_subarray, counter)
                    break
        return min_subarray if min_subarray != float('inf') else 0