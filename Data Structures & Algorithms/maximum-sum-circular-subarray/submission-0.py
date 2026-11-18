class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        def kadane(arr):
            cursum = float('-inf')
            maxsum = float('-inf')
            for  num in arr:
                cursum = num + max(cursum, 0)
                maxsum = max(cursum, maxsum)
            return maxsum
        
        max_kadane = kadane(nums)
        total_sum = sum(nums)
        min_kadane = kadane([-x for x in nums])
        circular_max = total_sum + min_kadane
        
        if circular_max == 0 and max_kadane < 0:
            return max_kadane

        return max(max_kadane, circular_max)
