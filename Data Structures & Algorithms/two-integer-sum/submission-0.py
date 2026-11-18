class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, e in enumerate(nums):
            remaining = target - e
            if remaining in hashmap:
                otherIndex = hashmap[remaining]
                return [otherIndex, i] if i> otherIndex else [i, otherIndex]
            else:
                hashmap[e]= i
        