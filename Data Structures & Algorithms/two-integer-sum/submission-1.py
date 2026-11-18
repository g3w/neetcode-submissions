class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_dict = {}

        for i, e in enumerate(nums):
            remainder = target - e
            if remainder in sum_dict:
                return [i, sum_dict[remainder]] if i < sum_dict[remainder] else [sum_dict[remainder], i]
            else:
                sum_dict[e] = i
