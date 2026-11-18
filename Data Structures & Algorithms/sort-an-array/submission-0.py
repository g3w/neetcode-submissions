class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n-1):
            mini = i
            for j in range(mini+1, n):
                if nums[j] < nums[i]:
                    mini = j
                    nums[i], nums[mini] = nums[mini], nums[i]
        
        return nums
        