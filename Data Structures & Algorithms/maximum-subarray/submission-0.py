class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        cursum = 0

        for num in nums:
            cursum = max(cursum, 0)
            cursum += num
            maxSum = max(maxSum, cursum)
        
        return maxSum
        