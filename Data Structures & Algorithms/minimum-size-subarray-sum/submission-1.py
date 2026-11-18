class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_subarray = float('inf')
        l = 0
        cursum = 0
        counter = 0
        for r in range(len(nums)):
            cursum += nums[r]
            counter += 1
            while cursum >= target:
                min_subarray = min(counter, min_subarray)
                cursum -= nums[l]
                l += 1
                counter -=1
        return min_subarray if min_subarray != float('inf') else 0